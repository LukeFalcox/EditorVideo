import os
import json
from google.generativeai import genai
import moviepy.editor as mp
from src.config import GEMINI_API_KEY
from src.utils.logger import log_error

genai.configure(api_key=GEMINI_API_KEY)

def transcribe_and_save(video_path: str, output_json_path: str) -> bool:
    """Extrai áudio, gera transcrição com timestamps via Gemini API e salva em JSON."""
    audio_path = "assets/temp_audio.mp3"
    uploaded_file = None
    
    try:
        # 1. Extrair áudio do vídeo
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path, logger=None)
        video.close()
        
        # 2. Upload do áudio para a API do Gemini
        uploaded_file = genai.upload_file(path=audio_path)
        
        # 3. Configurar o modelo (Flash é mais rápido e ideal para esta tarefa)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = """
        Ouça este áudio e transcreva tudo o que é falado.
        Você deve atuar como um gerador de legendas de precisão.
        
        Retorne APENAS um JSON válido e estruturado exatamente assim:
        {
            "text": "texto completo aqui",
            "segments": [
                {"start": 0.0, "end": 2.5, "text": "texto da frase"}
            ],
            "words": [
                {"word": "palavra", "start": 0.0, "end": 0.5}
            ]
        }
        Certifique-se de que os valores 'start' e 'end' sejam números (floats) em segundos.
        Não inclua formatação markdown (como ```json) na resposta, apenas o JSON puro.
        """
        
        # 4. Gerar o conteúdo
        response = model.generate_content([prompt, uploaded_file])
        
        # 5. Limpar e processar o texto da resposta para garantir que é um JSON
        response_text = response.text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:-3].strip()
        elif response_text.startswith("```"):
            response_text = response_text[3:-3].strip()
            
        data = json.loads(response_text)
        
        # 6. Salvar em arquivo local
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            
        return True

    except Exception as e:
        log_error(f"Falha na transcrição com Gemini: {e}")
        return False
        
    finally:
        # Limpeza: apagar áudio local e o arquivo temporário na API do Gemini
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if uploaded_file:
            try:
                genai.delete_file(uploaded_file.name)
            except Exception as e:
                log_error(f"Erro ao deletar arquivo remoto do Gemini: {e}") 
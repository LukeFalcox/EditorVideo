from src.config import GEMINI_API_KEY
from src.core.video_processor import process_video

try:
    process_video("assets/input.mp4", "output/output.mp4")
    print("✅ Pipeline executado com sucesso")
except Exception as e:
    print(f"❌ Erro: {str(e)}")
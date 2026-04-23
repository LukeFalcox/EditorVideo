from moviepy.editor import VideoFileClip

input_path = "assets/input.mp4"
output_path = "output/output.mp4"

# Carrega o vídeo
video = VideoFileClip(input_path)

# Corta os primeiros 10 segundos
clip = video.subclip(0, 10)

# Exporta
clip.write_videofile(output_path)

print("Vídeo processado com sucesso 🚀")
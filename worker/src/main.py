from services.video_loader import load_video

input_path = "assets/input.mp4"
output_path = "output/output.mp4"

video = load_video(input_path)

clip = video.subclip(0, 10)
clip.write_videofile(output_path)

print("Vídeo processado com sucesso 🚀")
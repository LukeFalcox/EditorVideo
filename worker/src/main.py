from services.video_loader import load_video

input_path = "assets/input.mp4"
output_path = "output/output.mp4"

video = load_video(input_path)

clip = video.subclip(0, 10)

expected_duration = 10
actual_duration = clip.duration

print(f"Duração esperada: {expected_duration}s")
print(f"Duração real: {actual_duration}s")

if abs(actual_duration - expected_duration) < 0.1:
    print("✅ Duração válida")
else:
    print("❌ Duração incorreta")
clip.write_videofile(output_path)

print("Vídeo processado com sucesso 🚀")
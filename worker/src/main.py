from services.video_loader import load_video
from services.text_overlay import add_text_overlay  
import moviepy.config as cfg

cfg.change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})
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
    
final = add_text_overlay(clip, "Hello World 🚀")

final.write_videofile(output_path)

print("Vídeo processado com sucesso 🚀")
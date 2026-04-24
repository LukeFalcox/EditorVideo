import config
from core.video_processor import process_video

input_path = "assets/input.mp4"
output_path = "output/output.mp4"

process_video(input_path, output_path)

print("Pipeline completo executado 🚀")
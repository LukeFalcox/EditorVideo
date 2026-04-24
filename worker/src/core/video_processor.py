from moviepy.editor import VideoFileClip
from services.video_loader import load_video
from services.text_overlay import add_text_overlay
import os


class VideoProcessorError(Exception):
    pass


def process_video(input_path: str, output_path: str):
    """
    Full video processing pipeline:
    - Load video
    - Cut first 10 seconds
    - Apply text overlay
    - Export final video
    """

    try:
        # 1. Load
        video = load_video(input_path)

        # 2. Cut
        clip = video.subclip(0, 10)

        # 3. Overlay
        final = add_text_overlay(clip, "Hello World 🚀")

        # 4. Ensure output folder exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 5. Export
        final.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac"
        )

        return output_path

    except Exception as e:
        raise VideoProcessorError(f"Processing failed: {str(e)}")
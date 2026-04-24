from services.video_loader import load_video
from services.text_overlay import add_text_overlay
from utils.logger import log_error
import os


class VideoProcessorError(Exception):
    pass


def process_video(input_path: str, output_path: str):

    try:
        video = load_video(input_path)

        clip = video.subclip(0, 10)

        final = add_text_overlay(clip, "Hello World 🚀")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        final.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac"
        )

        return output_path

    except Exception as e:
        log_error(f"Pipeline failed: {str(e)}")
        raise VideoProcessorError(f"Processing failed: {str(e)}")
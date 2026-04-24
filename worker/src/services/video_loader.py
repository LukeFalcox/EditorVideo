from moviepy.editor import VideoFileClip
import os
from utils.logger import log_error


class VideoLoaderError(Exception):
    pass


def load_video(file_path: str) -> VideoFileClip:

    if not file_path:
        log_error("Empty file path provided")
        raise VideoLoaderError("File path cannot be empty")

    if not os.path.exists(file_path):
        log_error(f"File not found: {file_path}")
        raise VideoLoaderError(f"File not found: {file_path}")

    if not file_path.endswith((".mp4", ".mov", ".avi")):
        log_error(f"Invalid format: {file_path}")
        raise VideoLoaderError("Unsupported file format")

    try:
        return VideoFileClip(file_path)
    except Exception as e:
        log_error(f"Failed to load video: {str(e)}")
        raise VideoLoaderError(str(e))
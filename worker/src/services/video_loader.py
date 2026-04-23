from moviepy.editor import VideoFileClip
import os


class VideoLoaderError(Exception):
    pass


def load_video(file_path: str) -> VideoFileClip:
    """
    Load a video file and return a VideoFileClip instance.

    :param file_path: Path to the video file
    :return: VideoFileClip object
    :raises VideoLoaderError: if file is invalid or cannot be loaded
    """

    # 1. Validate path
    if not file_path:
        raise VideoLoaderError("File path cannot be empty")

    # 2. Check if file exists
    if not os.path.exists(file_path):
        raise VideoLoaderError(f"File not found: {file_path}")

    # 3. Try loading video
    try:
        video = VideoFileClip(file_path)
        return video
    except Exception as e:
        raise VideoLoaderError(f"Failed to load video: {str(e)}")
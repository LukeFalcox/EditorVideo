from moviepy.editor import TextClip, CompositeVideoClip
from utils.logger import log_error


class TextOverlayError(Exception):
    pass


def add_text_overlay(video, text: str):

    if not text:
        log_error("Empty text provided")
        raise TextOverlayError("Text cannot be empty")

    try:
        txt_clip = (
            TextClip(
                text,
                fontsize=50,
                color="white",
                method="caption",
                size=video.size
            )
            .set_position("center")
            .set_duration(video.duration)
        )

        return CompositeVideoClip([video, txt_clip])

    except Exception as e:
        log_error(f"Text overlay failed: {str(e)}")
        raise TextOverlayError(str(e))
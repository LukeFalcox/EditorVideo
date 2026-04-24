from moviepy.editor import TextClip, CompositeVideoClip


class TextOverlayError(Exception):
    pass


def add_text_overlay(video, text: str):
    """
    Adds a centered text overlay to a video.

    :param video: VideoFileClip
    :param text: Text to display
    :return: CompositeVideoClip
    """

    if not text:
        raise TextOverlayError("Text cannot be empty")

    try:
        txt_clip = (
            TextClip(
                text,
                fontsize=50,
                color="white",
                method="caption",  # melhor compatibilidade
                size=video.size
            )
            .set_position("center")
            .set_duration(video.duration)
        )

        final_video = CompositeVideoClip([video, txt_clip])
        return final_video

    except Exception as e:
        raise TextOverlayError(f"Failed to add text overlay: {str(e)}")
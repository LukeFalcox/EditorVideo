import os
from dotenv import load_dotenv
import moviepy.config as cfg

load_dotenv()

cfg.change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})



GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY não encontrada. Verifique seu arquivo .env")
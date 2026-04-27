import moviepy.config as cfg

cfg.change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})

import os
from dotenv import load_dotenv
import moviepy.config as cfg

# Carrega variáveis de ambiente de um arquivo .env (crie um na raiz do projeto)
load_dotenv()

cfg.change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.x.x\magick.exe"
})

# Configuração da IA
GEMINI_API_KEY = os.getenv("AIzaSyCKZvR2k_aLY3DTPuX-qtSswB0hChi6tEE")
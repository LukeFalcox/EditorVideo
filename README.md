# 🎬 Intelligent Video Editing Platform (MVP)

## 📌 Overview

This project is a prototype of a SaaS platform that automates video editing using AI-driven workflows.

The system processes a raw video, applies transformations (cut + overlay), and exports a final video ready for publishing.

---

## 🧠 Features (Current MVP)

* 🎥 Load video from local file
* ✂️ Automatic cut (first 10 seconds)
* 📝 Text overlay (centered)
* 🎞️ Video export (MP4 format)
* ⚠️ Error handling and logging

---

## 🏗️ Tech Stack

* Python 3.11
* MoviePy
* FFmpeg
* ImageMagick

---

## 📁 Project Structure

```bash
worker/
├── src/
│   ├── core/
│   │   └── video_processor.py
│   ├── services/
│   │   ├── video_loader.py
│   │   └── text_overlay.py
│   ├── utils/
│   │   └── logger.py
│   ├── config.py
│   └── main.py
├── assets/
│   └── input.mp4
├── output/
│   └── output.mp4
├── logs/
│   └── app.log
└── venv/  (ignored)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd worker
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install moviepy
```

---

### 4. Install FFmpeg

Download and install FFmpeg and ensure it's added to your system PATH.

Test:

```bash
ffmpeg -version
```

---

### 5. Install ImageMagick

Download and install ImageMagick.

During installation:

* ✅ Check **"Add to PATH"**
* ✅ Check **"Install legacy utilities"**

Test:

```bash
magick -version
```

---

### 6. Configure ImageMagick path

Edit:

```bash
src/config.py
```

```python
import moviepy.config as cfg

cfg.change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.x.x\magick.exe"
})
```

---

## 🚀 Running the Project

```bash
python src/main.py
```

---

## 🎬 Input / Output Example

### 📥 Input

```bash
assets/input.mp4
```

* Any short video file (10–30 seconds recommended)

---

### 📤 Output

```bash
output/output.mp4
```

---

### 🎯 Expected Result

* Video trimmed to ~10 seconds
* "Hello World 🚀" displayed in center
* Audio preserved
* MP4 file playable

---

## 🧪 Logs

Errors are stored in:

```bash
logs/app.log
```

---

## ⚠️ Common Issues

### ❌ ImageMagick not detected

Fix:

* Verify installation
* Check PATH
* Set path manually in `config.py`

---

### ❌ FFmpeg not found

Fix:

* Add FFmpeg to PATH
* Restart terminal

---

### ❌ Video not found

Fix:

* Check `assets/input.mp4` exists

---

## 📊 Current Status

✅ MVP Core Engine Completed
🚧 AI Integration (Next Step)

---

## 🚀 Next Steps

* AI-based editing (Gemini / Claude)
* Dynamic subtitles
* Cloud storage (S3)
* Async processing (Celery)
* Web interface (React)

---

## 💬 Author Notes

This project demonstrates a modular and scalable approach to automated video editing using Python-based tooling.

---

## 📄 License

MIT License

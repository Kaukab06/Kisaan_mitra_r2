# speech_to_text_free.py
import whisper
import torch
import librosa

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🎤 STT using device: {device}")

whisper_model = None

def load_whisper():
    global whisper_model
    if whisper_model is None:
        print("⏳ Loading Whisper LARGE-V3...")
        whisper_model = whisper.load_model("large-v3", device=device)
    return whisper_model

async def transcribe_audio_local(audio_path: str) -> str:
    """
    Transcribe audio using Whisper LARGE-V3
    """
    try:
        model = load_whisper()
        print("🎤 Transcribing with Whisper LARGE-V3...")
        result = model.transcribe(audio_path, language="hi", fp16=(device=="cuda"))
        text = result.get("text", "").strip()
        print(f"✅ Transcribed Text: {text}")
        return text
    except Exception as e:
        print(f"❌ STT error: {e}")
        return None

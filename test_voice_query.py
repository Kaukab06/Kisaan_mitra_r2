
# test_voice_query

'''
import asyncio
import shutil
import os

from speech_to_text_free import transcribe_audio_local
from text_to_speech_free import synthesize_speech
from ollama_llm import call_mistral


async def test_voice_pipeline():
    audio_path = "temp_audio/test.wav"  # your input audio

    if not os.path.exists(audio_path):
        print("❌ Test audio not found")
        return

    print("🎤 STT: Transcribing...")
    user_text = await transcribe_audio_local(audio_path)
    print("User Text:", user_text)

    print("🧠 LLM: Ollama responding...")
    bot_text = call_mistral(user_text)
    print("Bot Text:", bot_text)

    print("🔊 TTS: Generating voice...")
    audio_out = await synthesize_speech(bot_text)

    print("✅ Voice response saved at:", audio_out)


if __name__ == "__main__":
    asyncio.run(test_voice_pipeline())
'''
import asyncio
from ollama_llm import call_mistral
from text_to_speech_free import synthesize_speech

async def main():
    text = "मेरी फसल बाढ़ में खराब हो गई है, कृपया मुझे संबंधित सरकारी योजनाओं के बारे में बताइए।"

    print("🧠 Sending text to Ollama...")
    bot_text = call_mistral(text)
    print("Bot Text:", bot_text)

    print("🔊 Generating voice...")
    audio_path = await synthesize_speech(bot_text)

    print("✅ Voice saved at:", audio_path)

asyncio.run(main())

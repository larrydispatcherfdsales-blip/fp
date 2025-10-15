import whisper
import os

print("--- Starting Speech-to-Text (STT) Script ---")

# Audio file ka path
audio_file_path = "test_audio.mp3"

if not os.path.exists(audio_file_path):
    print(f"!!! ERROR: Audio file not found at '{audio_file_path}' !!!")
else:
    try:
        # Whisper ka chota, tez model load karna (base model)
        print("Loading Whisper model (base)...")
        model = whisper.load_model("base")
        print("Model loaded successfully.")

        # Audio file ko transcribe karna
        print(f"Transcribing '{audio_file_path}'...")
        result = model.transcribe(audio_file_path)
        
        # Nateeja print karna
        transcribed_text = result["text"]
        print("\n" + "="*50)
        print("TRANSCRIPTION RESULT:")
        print(transcribed_text)
        print("="*50 + "\n")

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        import traceback
        traceback.print_exc()


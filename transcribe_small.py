import whisper

model = whisper.load_model("tiny")
result = model.transcribe("/Users/sathvik/Project/Whisper/harvard.wav")
print(result["text"])

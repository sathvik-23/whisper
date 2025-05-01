# 🎙️ Whisper Transcription Analysis

This project uses [OpenAI Whisper](https://github.com/openai/whisper) to transcribe audio files and evaluate the accuracy of different transcription outputs. The main goal is to analyze how Whisper handles subtle variations in pronunciation, clarity, and accent.

---

## 📌 Project Purpose

- Transcribe a given `.wav` audio file (`harvard.wav`) using the `small` Whisper model.
- Compare transcription output with expected/reference text.
- Identify minor and major differences in phrases or words (e.g., "Tacos al pastor" vs "Tuckles all pastora").
- Understand Whisper's behavior in edge cases and soft errors (homophones, regional terms, mispronunciations).

---

## 🔧 Setup Instructions

### 1. Clone and navigate

```bash
cd /Users/sathvik/Project/Whisper
```

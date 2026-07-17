# 🎙️ Meeting Minutes Voice Assistant

A **notebook-based pipeline** that turns a recorded meeting into structured minutes: **Hugging Face Whisper** transcribes the audio, then **OpenAI (gpt-4o-mini)** turns the transcript into a markdown summary with discussion points, takeaways, and action items.

---

## ✨ Features

- 🗣️ **Speech-to-text** — Hugging Face Inference API running `openai/whisper-large-v3`
- 📝 **Structured minutes** — OpenAI generates a summary, key discussion points, takeaways, and action items with owners
- 🔁 **Retry with backoff** — both API calls are wrapped with `tenacity` retries for transient failures
- 🧪 **Unit tested** — HF and OpenAI calls are mocked in tests, so the suite runs free and offline
- 📊 **Logged** — each pipeline step logs progress via the standard `logging` module

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Transcription | Hugging Face Inference API — `openai/whisper-large-v3` |
| Summarization | OpenAI API — `gpt-4o-mini` |
| Retries | tenacity |
| Testing | pytest + unittest.mock |
| Interface | Jupyter Notebook |

---

## 📁 Project Structure

```
08_meeting_minutes_voice_assistant/
├── meeting_minutes_voice_agent.ipynb   # Notebook driver — loads env, calls pipeline, displays minutes
├── pipeline.py                         # Reusable transcribe_audio() / generate_minutes() functions
├── denver_extract.mp3                  # Sample meeting recording
├── tests/
│   └── test_pipeline.py                # Mocked unit tests for both API calls
├── conftest.py                         # Makes pipeline.py importable from tests/
├── requirements.txt                    # Python dependencies
├── .env                                # Environment variables (NOT committed to Git)
└── .env.example                        # Template for environment variables
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/chandra-vv/genai_portfolio.git
cd genai_portfolio/08_meeting_minutes_voice_assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
HF_TOKEN=your_huggingface_api_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

> 🔑 Get a free Hugging Face token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and an OpenAI key at [platform.openai.com](https://platform.openai.com/api-keys)

### 5. Run the notebook

Open `meeting_minutes_voice_agent.ipynb` in Jupyter/VS Code and run all cells.

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `HF_TOKEN` | Hugging Face API token, used for Whisper transcription |
| `OPENAI_API_KEY` | OpenAI API key, used for minutes generation |

---

## 🚀 Usage

1. Run the setup cell — it loads credentials and fails fast if either key is missing
2. Run the transcription cell — transcribes `denver_extract.mp3` via HF Whisper
3. Run the minutes generation cell — sends the transcript to OpenAI and renders the minutes as markdown in the notebook

To run against your own recording, replace `AUDIO_FILE` with the path to your `.mp3`/`.wav` file.

---

## 🧪 Running Tests

```bash
pytest -v
```

Both the Hugging Face and OpenAI clients are mocked, so tests run without network access or API cost — including a case that verifies retry-then-succeed behavior.

---

## 🗺️ Roadmap

- [ ] Structured output (Pydantic schema) instead of freeform markdown minutes
- [ ] Speaker diarization — attribute each line to a speaker
- [ ] Gradio UI for uploading audio and viewing minutes
- [ ] Export minutes to PDF / Notion / Slack
- [ ] Agentic tool-calling — auto-create calendar events / send follow-ups from action items

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co) — hosted Whisper inference
- [OpenAI](https://platform.openai.com) — meeting minutes generation
- [tenacity](https://github.com/jd/tenacity) — retry logic

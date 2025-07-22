# 👧🏼 HELLA – Your Personal AI Assistant

HELLA is a **real-time multimodal AI agent** that listens, thinks, looks, and responds like a human.  
It combines **LLMs, speech, and vision** to create a seamless AI assistant experience.

---

## **🚀 Features**

| Function | Tech Used |
|-----------|-----------|
| **Talk to You (Speech-to-Text)** | **Whisper Large V3 (Groq API)** |
| **Talk Back (Text-to-Speech)** | **ElevenLabs API** |
| **Answer Questions & Reasoning** | **Gemini-2.0-Flash (Google Generative AI)** |
| **See Through Camera** | **LLaMA-4 Maverick Vision Model (Groq Vision API)** |
| **Real-Time UI** | **Gradio Interface** |
| **Agentic Decision Making** | **LangGraph ReAct Agent** |

---

## **🧠 How It Works**

1. **Continuous Listening**  
   HELLA listens to your voice input using **Whisper STT**.

2. **Agentic Reasoning**  
   Uses a **ReAct Agent (LangGraph)** with **Gemini-2.0-Flash** to process the query.

3. **Vision Capabilities**  
   If the query needs visual input (like "Do I have my phone in my hand?"), HELLA:
   - Captures an image via webcam  
   - Sends it to **LLaMA-4 Maverick Vision LLM** via Groq

4. **Natural Speech Output**  
   Responds with human-like audio using **ElevenLabs TTS**.

---

## **🧰 Tech Stack**

- **LLMs**: Gemini-2.0-Flash, LLaMA-4 Maverick  
- **Speech-to-Text**: Whisper Large V3 via Groq API  
- **Text-to-Speech**: ElevenLabs  
- **Vision**: Groq Vision API  
- **Framework**: Gradio  
- **Environment & Package Management**: `uv` (Rust-based Python tool)

---

## **📦 Why `uv`?**

Instead of `pip + venv`, this project uses **`uv`** for:

- ⚡ **10x faster package installs**  
- 🔒 **Deterministic builds** with lockfiles  
- 🚀 **Modern tooling**, no venv setup hassle  
- 🦀 **Rust-powered speed**

---

## **📂 Project Structure**
HELLA-AI-ASSISTANT/
│
├── ai_agent.py              # LangGraph ReAct agent setup with Gemini & Vision tools
├── tools.py                  # Webcam capture + Vision Q&A (LLaMA-4 Maverick)
├── speech_to_text.py         # Whisper-based STT using Groq API
├── text_to_speech.py         # ElevenLabs API for TTS
├── main.py                   # Gradio UI and continuous interaction loop
├── .env                      # API keys (not shared publicly)
├── pyproject.toml            # Project config
├── uv.lock                   # Lockfile for reproducibility

---

## **🔑 API Keys (Add to `.env` file)**
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key


---

## **🖥️ Run Locally**

1️⃣ Install [uv](https://github.com/astral-sh/uv)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh

python main.py


📸 Example Use Cases
	•	Ask general knowledge questions
	•	Ask visual queries (e.g., “Do I have a phone in my hand?”)
	•	Smart home conversational agent
	•	Multimodal AI demos




---

### **Next Step:**

- Copy this into your repo’s `README.md`  
- Commit & push:

```bash
git add README.md
git commit -m "Added professional README"
git push

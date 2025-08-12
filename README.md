# 🎶 AI Song Writer 🎤

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/) [![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-blue.svg)](https://ai.google.dev/)

**AI Song Writer** is a Python CLI tool that uses the [Google Gemini API](https://ai.google.dev/) to generate fully original song lyrics based on your preferences. Instantly create lyrics by choosing genre, mood, subject, and more—perfect for musicians, songwriters, or anyone looking for creative inspiration!

---

## ✨ Features
- Select **genre**, **subject**, and **mood**
- Add **reference artists** for inspiration (optional)
- Control **song length**, **perspective**, and **language**
- Generates unique, high-quality lyrics in seconds


## 📦 Installation

1. **Clone the repository**
	```bash
	git clone https://github.com/your-username/ai-song-writer.git
	cd ai-song-writer
	```

2. **Create a virtual environment**
	*Windows:*
	  ```bash
	  python -m venv venv
	  venv\Scripts\activate
	  ```
	*Mac/Linux:*
	  ```bash
	  python3 -m venv venv
	  source venv/bin/activate
	  ```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```

4. **Configure your API key and model**
	Create a `.env` file in the project root with the following content:
	  ```env
	  GOOGLE_API_KEY=<your_google_gemini_api_key>
	  AI_MODEL=models/gemini-1.5-pro
	  ```

---

## 🚀 Usage

Run the app from your terminal:

```bash
python ai-song-writer.py
```

You will be prompted for song details (all fields are optional):

```
🎸 Genre (e.g. pop, rock): pop
💘 Subject (e.g. love, heartbreak): summer romance
😊 Mood (e.g. happy, sad): happy
🎤 Reference artists (comma-separated, e.g. Adele, Coldplay): Lady Gaga
⏳ Song length (e.g. short, medium, long): medium
👀 Perspective (e.g. first person, second person): first person
🌍 Language (e.g. English, Spanish): English
```

The AI will generate your custom song lyrics, for example:

```
🎉✨ Your AI-generated song lyrics are ready! 🎶📝

[Verse 1]
Chrome city, neon bleed, the rain is glass, a weeping deed
Another night, another chase, a hunter's glare upon my face
Heard your laughter, silver chime, a phantom pulse across the time
Across the velvet, smoke-filled space, I saw the fire in your grace.
...
```

---

## ⚙️ Requirements

- Python 3.12+
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [google-genai](https://pypi.org/project/google-genai/)

---

## ⚙️ Configuration

Set your Google Gemini API key and model in a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
AI_MODEL=models/gemini-1.5-pro
```

---

## 🛠️ Troubleshooting

- **Missing API key:** Make sure your `.env` file is present and contains a valid `GOOGLE_API_KEY`.
- **Dependency errors:** Run `pip install -r requirements.txt` after activating your virtual environment.
- **Python version issues:** Ensure you are using Python 3.12 or newer (`python --version`).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).


## 👥 Contributors

- [Alberto Pérez Dávila](https://github.com/albertopd)

---

<div align="center">
	<sub>Made with ❤️ using Python & Google Gemini API</sub>
</div>
# 🎶 AI Song Writer 🎤

AI Song Writer is a Python CLI app that uses the **Google Gemini API** to generate custom song lyrics based on your input.

## ✨ Features
- Choose **genre**, **subject**, and **mood**
- Optionally add **reference artists** for inspiration
- Control **song length**, **perspective**, and **language**
- Generates fully original lyrics in seconds

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-song-writer.git
cd ai-song-writer
```

### 2. Create a virtual environment

```bash 
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

```
GOOGLE_API_KEY=your_google_gemini_api_key
AI_MODEL=models/gemini-1.5-pro
```

## 🚀 Usage

Run the script:

```bash
python song_writer.py
```

Answer the questions in the terminal (they are all optional)

```
🎸 Genre (e.g. pop, rock): pop
📝 Subject (e.g. love, heartbreak): summer romance
😊 Mood (e.g. happy, sad): happy
🎤 Reference artists (comma-separated, e.g. Adele, Coldplay): Lady Gaga
⏳ Song length (e.g. short, medium, long): medium
👀 Perspective (e.g. first person, second person): first person
🌍 Language (e.g. English, Spanish): English
```

The AI will generate your custom song lyrics:

```
🎉✨ Your AI-generated song lyrics are ready! 🎶📝

(Verse 1)
Sun is blearing, skin is gleaming, walking down the boardwalk bright
Headphones on, feel the rhythm, dancing in the golden light
Saw you laughing, ice cream melting, chocolate smeared across your face
Suddenly the world stopped spinning, found my smile in a happy place

(Pre-Chorus)
Never thought a summer day could hold a love so brand new
Burning with a neon glow, just me and just you

(Chorus)
This is summer love, electric buzz, like a Gaga anthem's high
Sunglasses on, we're untouchable, beneath the turquoise sky
Every beat is a heart attack, a rhythm only we can hear
This summer love, ain't going back, washing away all doubt and fear

(Verse 2)
Salty kisses, ocean breezes, stealing moments hand in hand
Building castles on the shoreline, grains of sand across the land
Sharing secrets, late night bonfires, embers dancing in the air
Whispered promises of forever, banishing all trace of care

(Pre-Chorus)
Never thought a summer day could hold a love so brand new
Burning with a neon glow, just me and just you

(Chorus)
This is summer love, electric buzz, like a Gaga anthem's high
Sunglasses on, we're untouchable, beneath the turquoise sky
Every beat is a heart attack, a rhythm only we can hear
This summer love, ain't going back, washing away all doubt and fear

(Bridge)
Maybe it's the heat, maybe it's the thrill
But in this moment, I can't stand still
Want to scream it loud, from the mountain top
This feeling's real, and it won't stop!

(Chorus)
This is summer love, electric buzz, like a Gaga anthem's high
Sunglasses on, we're untouchable, beneath the turquoise sky
Every beat is a heart attack, a rhythm only we can hear
This summer love, ain't going back, washing away all doubt and fear

(Outro)
Oh, summer love, yeah, summer love
Forever in my heart, above, above
This summer love, oh-oh-oh
This summer love.
```

## ⚙️ Requirements

- python 3.12+
- python-dotenv
- google-genai

## 📄 License

[MIT License](LICENSE)

## 👥 Contributors

[Alberto Pérez Dávila](https://github.com/albertopd)
from dotenv import load_dotenv
import os
from google import genai

def build_prompt(
    genre=None, subject=None, mood=None, reference_artists=None,
    song_length=None, perspective=None, language=None
):
    """
    Build a text prompt for the AI to generate song lyrics.

    Parameters:
        genre (str, optional): The genre of the song (e.g., pop, rock).
        subject (str, optional): The subject or theme of the song.
        mood (str, optional): The mood of the song (e.g., happy, sad).
        reference_artists (list[str] or str, optional): Reference artists to inspire style.
        song_length (str, optional): Desired length of the song ('short', 'medium', 'long').
        perspective (str, optional): Narrative perspective ('first person', 'second person', etc.).
        language (str, optional): Language of the lyrics.

    Returns:
        str: The formatted prompt for the AI model.
    """
    if isinstance(reference_artists, list):
        reference_artists = ", ".join(reference_artists) if reference_artists else "none"

    prompt = "Generate song lyrics based on the following details:\n\n"
    prompt += f"- Genre: {genre or 'any'}\n"
    prompt += f"- Subject: {subject or 'any'}\n"
    prompt += f"- Mood: {mood or 'neutral'}\n"
    prompt += f"- Reference artists: {reference_artists or 'none'}\n"
    prompt += f"- Song length: {song_length or 'medium'}\n"
    prompt += f"- Perspective: {perspective or 'first person'}\n"
    prompt += f"- Language: {language or 'English'}\n\n"
    prompt += "Please create original lyrics that fit the above criteria."

    return prompt


def generate_song_lyrics(client, model, genre, subject, mood, reference_artists, song_length, perspective, language):
    """
    Generate song lyrics using the given AI client and model.

    Parameters:
        client (genai.Client): The initialized Gemini API client.
        model (str): The AI model name.
        genre, subject, mood, reference_artists, song_length, perspective, language: Same as in build_prompt().

    Returns:
        str: The generated song lyrics.
    """
    prompt = build_prompt(
        genre=genre, 
        subject=subject, 
        mood=mood,
        reference_artists=reference_artists, 
        song_length=song_length,
        perspective=perspective, 
        language=language
    )

    response = client.models.generate_content(
        model=model, 
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    API_KEY = os.getenv("GOOGLE_API_KEY")
    if not API_KEY:
        raise Exception("GOOGLE_API_KEY not found. Please set it in your .env file.")

    AI_MODEL = os.getenv("AI_MODEL")
    if not AI_MODEL:
        raise Exception("AI_MODEL not found. Please set it in your .env file.")

    # Initialize the GenAI client
    client = genai.Client(api_key=API_KEY)

    # CLI for user input
    print("🎶🎤 Welcome to the AI Song Writer! 🎵✨\n")
    print("Please provide the following details to generate your song lyrics (they are all optional):\n")

    genre = input("🎸 Genre (e.g. pop, rock): ")
    subject = input("📝 Subject (e.g. love, heartbreak): ")
    mood = input("😊 Mood (e.g. happy, sad): ")
    reference_artists_input = input("🎤 Reference artists (comma-separated, e.g. Adele, Coldplay): ")
    reference_artists = [artist.strip() for artist in reference_artists_input.split(",")] if reference_artists_input else []
    song_length = input("⏳ Song length (e.g. short, medium, long): ")
    perspective = input("👀 Perspective (e.g. first person, second person): ")
    language = input("🌍 Language (e.g. English, Spanish): ")

    print("\n⏳ Thank you! Just hum some melody while I generate your song lyrics...\n")

    lyrics = generate_song_lyrics(
        client, AI_MODEL,
        genre, subject, mood, reference_artists,
        song_length, perspective, language
    )

    print("\n🎉✨ Your AI-generated song lyrics are ready! 🎶📝\n")
    print(lyrics)
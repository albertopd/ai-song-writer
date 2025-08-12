import textwrap
from dotenv import load_dotenv
import os
from google import genai

def build_prompt(
    genre : str | None = None, 
    subject : str | None = None, 
    mood : str | None = None, 
    reference_artists : str | list[str] | None = None,
    song_length : str | None = None, 
    perspective : str | None = None, 
    language : str | None = None
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

    prompt = f"""
    You are a professional songwriter. Your task is to create completely original song lyrics that meet the exact specifications below.

    [SONG PARAMETERS — must be followed exactly]
    - Genre: {genre or 'any'}
    - Subject/Theme: {subject or 'any'}
    - Mood/Emotion: {mood or 'neutral tone'}
    - Stylistic Influence: {reference_artists or 'none'}
    - Song length: {song_length or 'medium'}
    - Perspective: {perspective or 'first person'}
    - Language: {language or 'English'}

    [WRITING RULES — these are strict requirements]
    1. Use vivid, concrete imagery; avoid all clichés.
    2. Ensure lyrics flow naturally when sung.
    3. Create an emotional progression that matches the mood.
    4. Make choruses memorable and easy to sing.
    5. Maintain a consistent meter and natural rhythm.
    6. Include internal rhymes and wordplay where appropriate.

    [OUTPUT FORMAT]
    Follow a natural song structure for the chosen genre, including verses, choruses, and other sections as appropriate.”

    [FINAL REQUIREMENTS — must be followed exactly]
    - All lyrics must be completely original.
    - Maintain thematic and mood consistency throughout.
    - Ensure syllable counts work for singing.
    - Create a clear narrative or emotional arc.
    - End with a satisfying conclusion.
    - Do not include explanations or commentary — only the lyrics.
    """
    return textwrap.dedent(prompt).strip()

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
    print("\n🎶🎤 Welcome to the AI Song Writer! 🎵✨\n")
    print("Please provide the following details to generate your song lyrics (they are all optional):\n")

    genre = input("🎸 Genre (e.g. pop, rock): ")
    if not genre:
        genre = "any"
    subject = input("💘 Subject (e.g. love, heartbreak): ")
    if not subject:
        subject = "any"
    mood = input("😊 Mood (e.g. happy, sad): ") 
    if not mood:
        mood = "neutral"
    reference_artists = input("🎤 Stylistic Influence (comma-separated list of artis, e.g. Madonna, Lady Gaga): ")
    if not reference_artists:
        reference_artists = "none"
    song_length = input("⏳ Song length (e.g. short, medium, long): ")
    if not song_length:
        song_length = "medium"
    perspective = input("👀 Perspective (e.g. first person, second person): ")
    if not perspective:
        perspective = "first person"
    language = input("🌍 Language (e.g. English, Spanish): ")
    if not language:
        language = "English"

    print("\nThank you! I will use the following parameters:\n")
    print(f"🎸 Genre: {genre}")
    print(f"💘 Subject: {subject}")
    print(f"😊 Mood: {mood}")
    print(f"🎤 Stylistic Influence: {reference_artists}")
    print(f"⏳ Song Length: {song_length}")
    print(f"👀 Perspective: {perspective}")
    print(f"🌍 Language: {language}")

    print("\n⏳ Just hum some melody while I generate your song lyrics...\n")

    lyrics = generate_song_lyrics(
        client, 
        AI_MODEL,
        genre, 
        subject, 
        mood, 
        reference_artists,
        song_length, perspective, 
        language
    )

    print("\n🎉✨ Your AI-generated song lyrics are ready! 🎶📝\n")
    print(lyrics)
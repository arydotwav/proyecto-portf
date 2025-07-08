from newspaper import Article
from gtts import gTTS
import nltk

nltk.download('punkt')

def extract_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def text_to_speech(text, output_filename="output.mp3", lang="es"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_filename)
    print(f"✅ audio guardado como {output_filename}")


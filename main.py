from text_to_speech import extract_article_text, text_to_speech
from speech_to_text import speech_to_text_from_mic

#link del articulo que utilize para el audio: http://infobae.com/entretenimiento/2025/06/25/blackpink-se-reunio-para-volver-a-los-escenarios-despues-de-casi-dos-anos/

def main():
    print("\nque deseas hacer? \n1 - TEXT TO SPEECH\n2 - SPEECH TO TEXT")
    option = int(input("--> "))
    if option == 1:
        url = input("ingresa la URL del articulo: ")
        try:
            print("extrayendo el articulo...")
            article_text = extract_article_text(url)
            print("convirtiendo en audio...")
            text_to_speech(article_text)
            print("reproduccion del archivo: output.mp3")
        except Exception as e:
            print(f"⚠️ ERROR: {e}")
    elif option == 2:
        print("iniciando el reconocimiento de voz")
        speech_to_text_from_mic(output_file="transcripcion.txt", lang="es-ES")
    else:
        print("ERROR!")


if __name__ == "__main__":
    main()
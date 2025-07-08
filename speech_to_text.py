import speech_recognition as sr

def speech_to_text_from_mic(output_file="transcripcion.txt", lang="es-ES"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nhabla ahora.. (esperando audio)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("reconociendo el texto..")
        text = recognizer.recognize_google(audio, language=lang)
        print(f"texto detectado: {text}")

        with open(output_file, "a", encoding="utf-8") as file:
            file.write("- " + text + "\n")

        print(f"✅ se guardo el texto en '{output_file}'.\n")

        return text

    except sr.UnknownValueError:
        print("❌ no se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"❌ ERROR: {e}")

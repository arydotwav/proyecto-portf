# 🎙️ Speech-to-Text (y Text-to-Speech :D)

Este proyecto te permite:
- usar un artículo web y convertirlo en un archivo de voz (Text-to-Speech)
- usar tu voz, escucharla desde el micrófono y convertirla a texto (Speech-to-Text)

---

## 🚀 Requisitos

- Python 3.8 o superior
- Sistema operativo: Windows, Linux (hecho en este ultimo SO)
- Acceso a Internet (para `gTTS` y `newspaper3k`)

---

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/arydotwav/proyecto-portf.git
cd proyecto-portf
````

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate      # en windows
````

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
````

### 4. Probarlo
Solo tenes que correr el archivo main.py y seguir los pasos (dependiendo de lo que quieras hacer!)

## 📁 Estructura
proyecto-portf/
├── main.py
├── speech_to_text.py
├── text_to_speech.py
├── requirements.py
└── output.mp3

from langdetect import detect

def detect_language(text: str) -> str:
    try:
        language = detect(text)
        return language
    except Exception as e:
        return f'No se pudo detectar el idioma: {str(e)}'
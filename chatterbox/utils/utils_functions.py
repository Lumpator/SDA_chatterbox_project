import unicodedata


def text_to_unicode(text: str):
    return unicodedata.normalize("NFD", text).encode("ASCII", "ignore").decode("utf-8", "ignore")

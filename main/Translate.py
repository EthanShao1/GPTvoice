import fileOpen as FO
from translate import Translator

async def translate_text():
    text = FO.fileRead("text/text.txt")
    if len(text) > 1:
        a = 1
    else:
        a = 0

    translator = Translator(from_lang= "zh-TW", to_lang= "ja")  # 設置目標語言

    result = translator.translate(text[a])

    FO.fileWrite("text/text.txt", result)

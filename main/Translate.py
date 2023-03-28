import fileOpen as FO
from translate import Translator

async def translate_text():
    text = FO.fileRead("text/text.txt")

    translator = Translator(from_lang= "zh-TW", to_lang= "ja")  # 設置目標語言

    result = translator.translate(text)

    FO.fileWrite("text/text.txt", result)

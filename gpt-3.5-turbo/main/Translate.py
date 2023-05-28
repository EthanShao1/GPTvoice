import fileOpen as FO
from translate import Translator

async def translate_text():
    text = FO.fileRead("text/text.txt").strip("*").split("*")
    if len(text) > 1:
        for a in range(len(text)):
            if (" " in text[a]) == False:
                text.remove(text[a])
        usetext = "".join(text)
    else:
        # usetext = str(text)
        usetext = "".join(text)

    translator = Translator(from_lang= "zh-TW", to_lang= "ja")  # 設置目標語言

    result = translator.translate(usetext)

    FO.fileWrite("text/read.txt", result)
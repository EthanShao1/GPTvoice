import fileOpen as FO
from translate import Translator

async def translate_text():
    text = FO.fileRead("text/text.txt").strip("*").split("*")
    if len(text) > 1:
<<<<<<< HEAD
        a = 1
    else:
        a = 0

    translator = Translator(from_lang= "zh-TW", to_lang= "ja")  # 設置目標語言

    result = translator.translate(text[a])
=======
        for a in range(len(text)):
            if (" " in text[a]) == False:
                text.remove(text[a])
        usetext = "".join(text)
    else:
        # usetext = str(text)
        usetext = "".join(text)

    translator = Translator(from_lang= "zh-TW", to_lang= "ja")  # 設置目標語言

    result = translator.translate(usetext)
>>>>>>> 716af02f14a265ab14dd9a42e6067990eb3aadbb

    FO.fileWrite("text/read.txt", result)

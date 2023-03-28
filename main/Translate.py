from translate import Translator

async def translate_text():
    with open("text/text.txt", mode= "r", encoding= "utf-8") as file:
        text = file.read()

    translator = Translator(from_lang= "zh-TW", to_lang= "ja")  # 設置目標語言

    result = translator.translate(text)

    with open("text/text.txt", mode= "w", encoding= "utf-8") as data:
        data.write(result)

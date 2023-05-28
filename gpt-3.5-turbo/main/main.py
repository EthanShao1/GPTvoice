import os
import asyncio
import fileOpen as FO
import Translate as tran
import speech_synthesis as speech
from uuid import uuid4
from gpt3contextual import ContextualChatGPT, ContextManager

context_key = str(uuid4())
setUp = FO.fileRead("text/set.txt")

async def main():
    cm = ContextManager(
        timeout = 9999999999,
        username = "　你　",
        agentname = "ひなた",
        chat_description = setUp,
    )
    
    cc = ContextualChatGPT(
        os.environ.get("OPENAI_API"),
        context_manager=cm
    )
    
    while True:
        text = input(f"{cm.username}> ")
        resp, prompt, completion = await cc.chat(context_key, text)
        print(f"{cm.agentname}> {resp}")
        
        data = completion["choices"][0]["message"]["content"]
        FO.fileWrite("text/text.txt", data)

        await tran.translate_text()
        await speech.speaker()

asyncio.run(main())

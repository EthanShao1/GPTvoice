import os
import asyncio
import Translate as tran
import speech_synthesis as speech
from uuid import uuid4
from gpt3contextual import ContextualChatGPT, ContextManager

context_key = str(uuid4())

with open("set.txt", mode= "r", encoding= "utf-8") as set:
    setUp = set.read()

async def response():
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
        with open("text.txt", mode= "w", encoding= "utf-8") as file:
            file.write(data)

        await tran.translate_text()
        # await asyncio.sleep(1)
        await speech.speaker()

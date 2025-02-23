import os
import fileOpen as FO
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription= os.environ.get('SPEECH_KEY'),
                                       region= os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# speech_config.speech_synthesis_voice_name='zh-CN-XiaoyiNeural'
speech_config.speech_synthesis_voice_name='ja-JP-AoiNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

async def speaker():
    text = FO.fileRead("text/read.txt")
        
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
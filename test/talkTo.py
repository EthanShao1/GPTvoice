import speech_recognition

def VoiceToText():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source: 
        print("請開始說話:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    Text = r.recognize_google(audio, language="zh-TW") 

    return Text

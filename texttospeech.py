import pyttsx3

class TTS:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice','com.apple.speech.synthesis.voice.daniel')

    def say_word(self):
        self.engine.say("hello")
        self.engine.runAndWait()



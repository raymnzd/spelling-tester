import pyttsx3

class TTS:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice','com.apple.speech.synthesis.voice.daniel')
        self.word_list = [word for word in open('words.txt','r')]  
        print(self.word_list)
    def get_word(self):
        pass

    def say_word(self):
        self.engine.say("hello")
        self.engine.runAndWait()

    def inc_rate(self):
        rate = engine.getProperty('rate')
        self.engine.setProperty('rate', rate+50)

    def dec_rate(self):
        rate = engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)


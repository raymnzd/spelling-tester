import pyttsx3
import texttospeech
import time
from PyQt5.QtWidgets import QApplication, QLabel

def main():
    app = QApplication([])
    label = QLabel("Spell the word")
    label.show()
    tts = texttospeech.TTS()
    app.exec_()

if __name__ == "__main__":
    main()

import pyttsx3
from random import shuffle

engine = pyttsx3.init()
words = open('words.txt', 'r')
word_list = []

#add each line to list
for line in words:
   word_list.append(words.readline())


def spelling_bee():
    correct = True
    shuffle(word_list)
    engine.setProperty('rate',150)
    while correct:
        engine.say(word_list[0])
        engine.runAndWait()
        
        answer = input()
        if answer.lower() != word_list[0].lower().strip():
            correct = False
        else:
            word_list.pop(0)


    print('Wrong, the answer was ' + word_list[0])
    print(len(word_list[0]), "was the length of the word")
    print(list(word_list[0]))
    print(len(answer), "was the length of your input")
    if input("Would you like to play again? y/n ") == "y":
        spelling_bee()


spelling_bee()

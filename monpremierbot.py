#!/usr/bin/python3
#salutation = ['Hello', 'Ciao', 'Goodbye', 'Salam', 'Hy', 'GoodNight', 'Holla', 'BonesNuches', 'SeeYou', 'GoodAfternoon']

question = input("Bonjour, je suis votre premier bot, veillez inseré un mot\n")

proposition = ["salut", "bonjour", "bonsoir"]
if (question.lower() in proposition):
    print("Salut mon ami")
else:
    print("je ne comprend rien")

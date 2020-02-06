#!/usr/bin/python3
import random
import re
salutation = ['Hello', 'Ciao', 'Goodbye', 'Salam', 'Hy', 'GoodNight', 'Holla', 'BonesNuches', 'SeeYou', 'GoodAfternoon']

reponse = input("Bonjour, je suis votre premier bot, veillez inseré un mot!\n")
proposition = ["salut", "bonjour", "bonsoir"]
if (reponse.lower() in proposition):

    print(random.choice(salutation) + " mon ami")
else:
    print("je ne comprend rien")

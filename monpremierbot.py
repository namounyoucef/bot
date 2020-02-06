#!/usr/bin/python3
import random
import re
import datetime
#salutation = ['Hello', 'Ciao', 'Goodbye', 'Salam', 'Hy', 'GoodNight', 'Holla', 'BonesNuches', 'SeeYou', 'GoodAfternoon']
categories = ["voiture", "telephone", "ordinateur"]
exclure = ["je", "tu", "bien", "nous", "svp", "bonjour"]
#question = input("Bonjour, je suis votre premier bot, veillez inseré un mot!\n")
requete = input ("bonjour, je suis votre assistant MyBot, Que desirez vous achetez ? \n")
decoupe = (re.findall(r"[a-zA-Z]+", requete))
#print (decoupe)
final = list(set(decoupe) - set(exclure))
finale = [mot.lower() for mot in final if len(mot) > 2 ]
#print(finale)

#proposition = ["salut", "bonjour", "bonsoir"]
if "voiture" in finale : 
    print("voici le catalogue de voitures")
elif "telephone" in finale :
    print("voici le catalogue de telephone")
elif "ordinateur" in finale :
    print("voici notre game d'ordinateur ")
else:
    print("vu a {0}".format(datetime.datetime.now())) 
#if (reponse.lower() in proposition):

   # print(random.choice(salutation) + " mon ami")
#else:
   # print("je ne comprend rien")

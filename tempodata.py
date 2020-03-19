#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
Mon super programme de relevé de
température pour matplotlib.
L'emploi consiste à relever les 
températures à la fin de chaque mois.
"""


import os
import json
#import pylint.lint
#import aspidata


print("###########")
print("Bienvenue !")
print("###########\n")
print("--------------------------------------------------")
print("Notes à l'attention de l'utilisateur: \n")
print("Veuillez créer au moins 2 dates à chaque lancement")
print("et veuillez les entrer dans l'ordre, autrement")
print("le programme ne fonctionnera pas !!!")
print("--------------------------------------------------\n")
print("Lancement du programme...\n")

class Tempa:
    """
    Meteo class
    PLusieurs questions se succèdent
    Il en faut minimum 2 pour que matplotlib
    se lance...
    """
    JOUR_ENPLUS = 0 # Usefull for writting several days !
    # Preformated data to tested entries and writting into a txt file.
    data_format = []
    print("Nombre de caractères str pour le jour : ", len(data_format))
    DAYIN = data_format
    print(DAYIN.count("/"))
    print(DAYIN.count(""))

    heure_format = ["","h",""]
    print("Nombre de caractères str pour l'heure : ", len(heure_format))
    HER = heure_format
    print(HER.count("h"))
    print(HER.count(""))

    nbr_format = ["",".",""]
    print("Nombre de caractères str pour le nbre de degrés : ", len(nbr_format))
    NBR = nbr_format
    print(NBR.count("."))
    print(NBR.count(""))

    print("Nbre d'éléments dans la liste :")
    CIELO = {0:"couvert", 1:"nuageux", 2:"dégagé", 3:"pluie", 4:"neige", 5:"tempetueux"}
    print("Le ciel : ", len(CIELO))
    print(CIELO)
    ASK = ''

    def __init__(self):
        """
        On réinitialise une fois le questionaire terminé.
        Revient au tout début.
        """
        print("Création d'un jour...\n")
        while True:
            try:
                self.DAYIN = input("Veuillez entrer la date du jour au format ../../.. svp : ")
                print(self.DAYIN)
                if self.DAYIN.count("/") == 2:
                    print("+ Les 2 slash y sont.")
                    print(self.DAYIN.count("/"))
                    if len(self.DAYIN) == 10:
                        print("+ Les 10 éléments sont bien respectés.")
                        print(len(self.DAYIN))
                        if self.DAYIN[0:2] >= str(0) + str(1) and self.DAYIN[0:2] <= str(31):
                            print("+ La date du jour est ok.")
                            print(self.DAYIN[0:2])
                            if self.DAYIN[3:5] >= str(0) + str(1) and self.DAYIN[3:5] <= str(12):
                                print("+ Le mois semble respecté.")
                                print(self.DAYIN[3:5])
                                if self.DAYIN[6:11] == str(2020):
                                    print("+ L'année semble respectée.")
                                    print(self.DAYIN[6:11])
                                    print("\nOk, poursuivons avec l'heure !\n")
                                    break
                                else:
                                    print("- Ce n'est pas la bonne année.")
                                    print("Veuillez reformuler votre date.")
                            else:
                                print("- Le mois ne semble pas rationnel!")
                                print("Veuillez reformuler votre date.")
                        else:
                            print("- Il y a 1 à 31 jours max dans le mois.")
                            print("Veuillez reformuler votre date.")
                    else:
                        print("- Soit il manque la notation des dates en dizaine,")
                        print("soit il manque un 0 devant!")
                        print("Veuillez reformuler votre date.")
                else:
                    print("- Il manque 1 ou 2 '/' (slash)")
                    print("Veuillez reformuler votre date.")
            except ValueError:
                print("- Vous n'avez pas entré le bon format de date!")
                print("Veuillez reformuler votre date.")
        while True:
            try:
                self.HER = input("Veuillez entrer l'heure du relevé, au format ..h.. svp ? : ")
                print(self.HER)
                if self.HER.count("h") == 1:
                    print("+ Le 'h' y est")
                    print(self.HER.count("h"))

                    if len(self.HER) == 5:
                        print("+ Les 5 éléments y sont.")
                        print(len(self.HER))

                        if self.HER[0:2] >= str(0) + str(0) and self.HER[0:2] < str(24):
                            print("+ Ok pour l'heure.")
                            print(self.HER[0:2])

                            if self.HER[3:5] >= str(0) + str(0) and self.HER[3:5] < str(60):
                                print("+ Ok pour les minutes")
                                print(self.HER[3:5])
                                print("\nOk, passons au degrés !\n")
                                break
                            else:
                                print("- Les minutes ne jouent pas (00-60) !")
                        else:
                            print("- L'heure ne joue pas (00-23)!")
                    else:
                        print("- L'heure n'est pas au bon format, la longueur est différente de 5.")
                else:
                    print("- Le 'h' entre 2 n'y est pas !")
            except ValueError:
                print("- Y'a un truc qui joue pas avec l'heure...")
        while True:
            try:
                self.NBR = input("Veuillez entrer le nbre avec + ou - devant (ex: +33.0): ")
                print(self.NBR)
                if self.NBR.count(".") == 1:
                    print("+ Le '.' y est")
                    print(self.NBR.count("."))
                    if self.NBR.count("+") == 1 or self.NBR.count("-") == 1:
                        print("+ Le '+' ou le '-' y est !")
                        print(self.NBR.count("+ , -"))
                        if len(self.NBR) == 5:
                            print("+ Les 5 éléments y sont (ex: -33.0 excepté pour 0.0).")
                            print(len(self.NBR))
                            print("\nOk, passons au temps qu'il fait !\n")
                            break
                        elif len(self.NBR) == 4:
                            print("+ Les 4 éléments y sont (ex: 22.5 ou -2.5).")
                            print(len(self.NBR))
                            print("\nOk, passons au temps qu'il fait !\n")
                            break
                        elif len(self.NBR) == 3:
                            print("+ Les 3 éléments y sont (ex: 0.0).")
                            print(len(self.NBR))
                            print("\nOk, passons au temps qu'il fait !\n")
                            break
                        else:
                            print("- Les degrés ne sont pas au bon format !")
                    else:
                        print("- Il n'y a pas de '+' ou de '-', veuillez en entrer un !")
                else:
                    print("- Le '.' entre 2 n'y est pas !")
            except ValueError:
                print("- Y'a un truc qui joue pas avec les degrés...")
        while True:
            try:
                print("Quel temps fait-il ? \n0-couvert\n1-nuageux\n2-dégagé")
                print("3-pluie\n4-neige\n5-tempetueux\n : ")
                # self.ask is usefull to call self.cielo & 'w' value into .txt file
                self.ASK = input("Choisir entre 0, 1, 2, 3, 4, 5 : ")
                if self.ASK == '0':
                    self.ASK = self.CIELO[0]
                    #self.CIELO[0]
                    print(self.CIELO[0])
                    break
                elif self.ASK == '1':
                    self.ASK = self.CIELO[1]
                    #self.CIELO[1]
                    print(self.CIELO[1])
                    break
                elif self.ASK == '2':
                    self.ASK = self.CIELO[2]
                    #self.CIELO[2]
                    print(self.CIELO[2])
                    break
                elif self.ASK == '3':
                    self.ASK = self.CIELO[3]
                    #self.CIELO[3]
                    print(self.CIELO[3])
                    break
                elif self.ASK == '4':
                    self.ASK = self.CIELO[4]
                    #self.CIELO[4]
                    print(self.CIELO[4])
                    break
                elif self.ASK == '5':
                    self.ASK = self.CIELO[5]
                    #self.CIELO[5]
                    print(self.CIELO[5])
                    break
                else:
                    print("\n- Vous n'avez pas choisi le bon chiffre !\n")
            except ValueError:
                print("Je ne sais pas ce que vous avez entré, essayé à nouveau svp.")
        Tempa.JOUR_ENPLUS += 1 # Attribut de classe (variable de classe)

reponse = input("Voulez-vous continuer ? (o/n) : \n")
champs = "Programme Python : Relevé des températures (Esteban et Cie)"
traity = "-----------------------------------------------------------"
sharp = "####################################################"
data = {}
data["data"] = []
continuer = 0
while reponse != 'n':
    if reponse != 'o':
        print("Vous n'avez pas presser la touche 'n' ou 'o' !")
        reponse = input("Voulez-vous coutinuer oui ou non (o/n) ? : ")
        if reponse == 'n':
            print("Merci et aurevoir!")
            break
    if reponse == 'o':
        print("Ok, on continue\n")
        tempo = Tempa()
        if not os.path.isfile("myfile.txt"):
            file = open("MyFichier.txt", 'at') # (at = append + text)
            print("\nVoici le résultat final de vos entrées :")
            print("---------------------------------------\n")
            print("Jour > {}".format(tempo.DAYIN))
            print("Heure de la prise > {}".format(tempo.HER))
            print("Température > {}°".format(tempo.NBR))
            # input(x) --> self.ask = self.cielo[x] --> print(self.cielo[key])
            print("Ciel > {}".format(tempo.ASK))
            print("Jours répertoriés à la suite : {}".format(tempo.JOUR_ENPLUS))
            # For writting data into "MyFichier.txt"
            file.write(str(champs.center(50)))
            file.write(str("\n"))
            file.write(str(traity.center(50)))
            file.write(str("\n\n"))
            file.write("Date: ")
            file.write(str(tempo.DAYIN))
            file.write(str("\n\n"))
            file.write("Heure: ")
            file.write(str(tempo.HER))
            file.write(str("\n\n"))
            file.write("Température: ")
            file.write(str(tempo.NBR +"C°"))
            file.write(str("\n\n"))
            file.write("Temps: ")
            # input(x) --> self.ask = self.cielo[x] --> print(self.cielo[key])
            file.write(str(tempo.ASK))
            file.write(str("\n\n"))
            file.write("N jour répertorié à la suite : ")
            file.write(str(tempo.JOUR_ENPLUS))
            file.write(str("\n\n"))
            file.write(str(sharp))
            file.write(str("\n\n"))
            file.close()
            # Write a list in json file
            data["data"].append({
                "Jour" : tempo.DAYIN,
                "Temperature" : tempo.NBR
                })

        with open("data.json", "w") as datafile:
            json.dump(data, datafile, indent=4)
        if not os.path.isfile("myfile.txt"):
            fil2 = open("MyValues.txt", 'at') # (at = append + text)
            print("\n")
            print("Température > {}C°".format(tempo.NBR))
            print("\n")
            dicolist2 = {}
            dicolist2 = {tempo.DAYIN : tempo.NBR}
            print(dicolist2)
            print("Les dernières valeurs enregistrées dans MyValues.txt")
            listal2 = []
            listal2.append(dicolist2.items())
            print("\nPrint(lista2) :")
            print("-----------------")
            print(listal2)
            fil2.write(str("\n"))
            for key in listal2[0]:
                print(key[0])
            fil2.write(str(key[0]))
            fil2.write(str(" : "))
            for value in listal2[0]:
                print(value[1])
            fil2.write(str(value[1]))
            fil2.close()
            print("\nDerniers relevés :")
            print("--------------------")

        with open("MyValues.txt", 'r') as y_file:
            content2 = y_file.read()
            print(content2)
            reponse = input("\nVoulez-vous continuer? o/n : \n")
            if reponse == 'n':
                print("\nChargement des données vers aspidata.py...")
                print("lancement du programme 'aspidata.py', puis de 'plot_prog.py'\n")
                print("pour le rendu graphique avec matplotlib...\n")
                # Launch next prog...
                os.system('python3 aspidata.py')
            else:
                continuer += 1

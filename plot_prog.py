#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
Third file launching since aspidata.py
This file open a graphical representation
of temperatures with matplotlib
"""


import json
import matplotlib.pyplot as plt


print("\nListe1=dates :")
print("--------------")
file = open("data_jour.json")
list1 = json.load(file)
file.close

for letter in list1:
    print("list1: " + letter)

print("\nList2=températures :")
print("--------------------")

file2 = open("data_temp.json")
list2 = json.load(file2)
file2.close

for letter in list2:
    print("List2: " + letter)

print("\nSuper LOOP!\n")

dicolist = {}

for list1, list2 in zip(list1, list2):
    dicolist[list1] = list2

print("Affichage du dictionnaire :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)

print("\nListe des dates dans le désordre :")
print("----------------------------------")
print(list1)
print("\nListe des températures :")
print("------------------------")
print(list2)

list2 = list(map(float, list2))

show_grid = True
with plt.style.context(('seaborn-darkgrid')):
    plt.plot(list1, list2)
    plt.ylabel('Temperatures °C')
    plt.xlabel('Dates')
    plt.title('Relevé des températures du mois de FEVRIER 2020')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.show()

#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
That's second file launching since tempodata.py
It load data.json for writing data into data_jour.json
and into data_temp.py
"""


import os
import json
import time


file = open("data.json")
data = json.load(file)
file.close

for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))
    print("\nTo represent the data_get:\n")
    print(data.get("data"))
    print("\n")
    print("Valeur: " + str(value[0]))
    print("Valeur: " + str(value[1]))
    print("\n")
    print("Jour: " + str(value[0]["Jour"]))
    print("Température: " + str(value[0]["Temperature"]))
    print("\n")
    print("Jour: " + str(value[1]["Jour"]))
    print("Température: " + str(value[1]["Temperature"]))

print("\nDay LOOP\n")

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Jour'])
    print(value[0]['Jour'])

print("\nThat seems ok!\n")

with open("data_jour.json", "w") as data_file:
    json.dump(data_list1, data_file, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nTemperature LOOP\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Temperature'])
    print(value[0]['Temperature'])

print("\nThat seems correct!\n")

with open("data_temp.json", "w") as data_file:
    json.dump(data_list2, data_file, indent=4)

print("\nLancement du programme 'plot_prog.py'...")
# Time stamp 2 sec:
print("Chargement dans 2 secondes...")
time.sleep(2)
# Launching plot_prog.py
os.system('python3 plot_prog.py')

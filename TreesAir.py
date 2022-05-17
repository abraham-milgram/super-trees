"""
->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
<> File: TreesAir.py
<> Author: Abraham Milgram
<> Description: Takes trees.csv and air.csv and concentrates them into a single csv  
<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<
"""

import csv
from decimal import Decimal
import re


trees = open("trees.csv", 'r', encoding="utf8") # Contains the quantities of trees and land mass of all 42 uhf areas in new york city
air = open("air.csv", 'r', encoding="utf8") # Contains the air quality data of all 42 uhf areas in new york city

gas = ['NOx', 'SO2', 'PM2.5'] # Three gasses measured in the air quality data

airdata = {}

# Processes air quality data into dictionary by gas type and uhf
for g in gas:
    airdata[g] = {}
first = True
for line in air:
    if first:
        first = False
        continue
    data = re.findall(r'(?:^|,)((?:[^\",]|\"[^\"]*\")*)', line.strip('\n'))
    airdata[data[0]][data[1]] = data[2]

treedata = {}

# Processes tree data and computes the trees per km2
first = True
for line in trees:
    if first:
        first = False
        continue
    data = re.findall(r'(?:^|,)((?:[^\",]|\"[^\"]*\")*)', line)
    treedata[data[0]] = round(float(Decimal(data[2])/Decimal(data[1])))

# Combines the two data sets and writes them to lines
fusiondance = []
for g in gas:
    for uhf in treedata.keys():
        fusiondance.append([g, uhf, treedata[uhf], airdata[g][uhf]])

# Writes lines to new csv
with open('treesair2015.csv', 'w', encoding="utf8") as tr:
    writer = csv.writer(tr)
    writer.writerow(['Gas', 'District', '# of Trees per km2', 'Total Emisions per km2'])
    for i in fusiondance:
        writer.writerow(i)
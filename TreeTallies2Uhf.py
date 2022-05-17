import re
import csv
from decimal import *
t2015 = open(r"trees.csv", 'r', encoding="utf8")

def makedata(f, length):
    processed = {}
    f.seek(0)
    categories = f.readline().strip('\n').split(',')
    
    first = True
    for id, line in enumerate(f):
        if first:
            first = False
            continue
        linee = line.strip('\n')
        data1 = re.findall(r'(?:^|,)((?:[^\",]|\"[^\"]*\")*)', linee)

        processed[str(id)] = {}
        for index, i in enumerate(data1):
            processed[str(id)][categories[index]] = i

    return processed
outputsum = {}
trees = []
def tree_collect(processed):
    outputdata = {}
    for passenger in processed:
        tree = processed[passenger]['spc_common']
        if tree not in trees:
            trees.append(tree)
        location = processed[passenger]['postcode']
        
        if location not in outputdata.keys():
            outputdata[location] = {}

        if tree in outputdata[location].keys():
            outputdata[location][tree] += 1
        else:
            outputdata[location][tree] = 1
        outputsum[location] = sum(list(outputdata[location].values()))
    return outputdata

tt2015 = 683788
t2015p = tree_collect(makedata(t2015, tt2015))

for i in t2015p.keys():
    t2015p[i]['sum'] = outputsum[i]

lines = []

for zip in t2015p.keys():
    line = [zip, t2015p[zip]['sum']]
    del t2015p[zip]['sum']
    for t in trees:
        if t in t2015p[zip]:
            line.append(t2015p[zip][t])
        else:
            line.append(0)
    lines.append(line[1:])

neighborhoods = {}
sizes = {}
uhfs = open(r"uhfProcessed.csv", 'r', encoding="utf8")
first = True
for i in uhfs:
    if first:
        first = False
        continue
    data = re.findall(r'(?:^|,)((?:[^\",]|\"[^\"]*\")*)', i)
    for index, a in enumerate(data[2].strip('"').split(',')):
        neighborhoods[a] = data[0]
        sizes[data[0]] = float(sum([Decimal(i.strip(' ').strip('"')) for i in data[3].strip('\n').split(',')]))

final = {}
for i in neighborhoods.keys():
    if neighborhoods[i] not in final.keys():
        try:
            final[neighborhoods[i]] = lines[list(t2015p.keys()).index(i)]
        except:
            continue
    else:
        for index, a in enumerate(final[neighborhoods[i]]):
            try:
                final[neighborhoods[i]][index] += lines[list(t2015p.keys()).index(i)][index]
            except:
                continue
for uhf in final.keys():
    final[uhf] = [sizes[uhf]] + final[uhf]

print(final)

with open('uhfTREES.csv', 'w', encoding="utf8") as tr:
    writer = csv.writer(tr)
    writer.writerow(['uhf', 'area km2', '# of trees'] + trees)
    for uhf in final.keys():
        writer.writerow([uhf, final[uhf]])
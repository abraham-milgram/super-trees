import re
import requests
import csv


areas = {}
uhf = open(r"Data Processing\General Csv Parser\UHF.csv", 'r')
first = True
for line in uhf:
    if first:
        first = False
        continue
    data = re.findall(r'(?:^|,)((?:[^\",]|\"[^\"]*\")*)', line.strip('\n'))
    areas[data[0]] = {'Name': data[1], 'Zips': data[2].strip('"').split(','), 'borough': ''}

boroughs = {}
borough = ['bronx', 'brooklyn', 'new york', 'queens', 'staten island']

for i in range(5):
    boroughs[str(i + 1)] = borough[i] 

first = True
for i in areas.keys():
    if first:
        first = False
        continue
    areas[i]['borough'] = boroughs[i[0]]

sites = []
for meme in list(areas.keys()):
    zipss = {}
    for zips in areas[meme]['Zips']:
        try:
            zipss[zips] = re.findall('\d*\.*\d*', re.findall('Land Area:</span></td><td class="info">\d*\.*\d* sq mi', requests.get(rf"https://www.zip-codes.com/zip-code/{zips}/zip-code-{zips}.asp").text)[0])[-8]
        except:
            print(zips)
            exit()

    areas[meme]['Zips'] = zipss

with open('uhf.csv', 'w', newline='') as csv_data:
    writer = csv.writer(csv_data)
    writer.writerow(['UHF', 'borough', 'name', 'zip_codes', 'zip_sizes'])
    for uhf in areas.keys():
        writer.writerow([uhf, areas[uhf]['borough'], areas[uhf]['Name'], ', '.join(list(areas[uhf]['Zips'].keys())), ', '.join(list(areas[uhf]['Zips'].values()))])

# print(areas)
import csv
import json
from pprint import pprint

data = open('data.csv')

reader = csv.DictReader(data)

def output_json():
    contents = json.dumps(list(reader), indent=4)
    with open('data.json', 'w') as file:
        file.write(contents)

def output_xml():
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<banks>']

    for row in reader:
        xml.append('<bank>')
        xml.extend(f'    <{k}>{v}</{k}>' for k, v in row.items())
        xml.append('</bank>')
    xml.append('<banks>')

    with open('data.xml', 'w') as file:
        file.write('\n'.join(xml))

def total_deposits():
    total = sum(int(row['DEPSUM'].replace(',', '')) for row in reader)
    print(f'total: ${total}')

def bank_deposits():
    deposits = {}

    for row in reader:
        if row['NAMEFULL'] not in deposits:
            deposits[row['NAMEFULL']] = 0
        deposits[row['NAMEFULL']] += int(row['DEPSUM'].replace(',', ''))

    deplist = [{'name': k, 'deposits': v} for k, v in deposits.items()]
    deplist.sort(key=lambda k: k['deposits'])

    pprint(deplist)

print('[1] output as json')
print('[2] output as xml')
print('[3] total deposits')
print('[4] bank deposits')
print('')

try:
    choice = int(input('what would you like to do? '))
except:
    print('bad choice')

if choice == 1:
    output_json()
elif choice == 2:
    output_xml()
elif choice == 3:
    total_deposits()
elif choice == 4:
    bank_deposits()

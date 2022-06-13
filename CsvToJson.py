#https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json
import csv
import json

'''
def csvCount(filename):
    countcsv = open(filename, 'r')
    rdr = csv.reader(countcsv)
    count=0
    for line in rdr:
        count = count + 1
    countcsv.close()
    rdr.close()
    return count
'''

csvfile = open('top20.csv', 'r',encoding='utf-8')
jsonfile = open('top20.json', 'w',encoding='utf-8')

reader = csv.DictReader(csvfile)

rowCount = 8
i = 0

jsonfile.write('[\n')

for row in reader:
    json.dump(row, jsonfile, indent=4, ensure_ascii = False)
    if i < rowCount-1:
        jsonfile.write(',\n')
    else:
        jsonfile.write('\n')
    i= i + 1
    
jsonfile.pop(',')
jsonfile.write(']')


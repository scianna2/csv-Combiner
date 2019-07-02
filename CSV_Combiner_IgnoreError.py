import csv
from os import walk

importedFiles=[]

with open('Master.csv', 'r', errors='ignore', newline='') as masterCsv:
    masterCsvReader = csv.reader(masterCsv, delimiter=',', quotechar='"')

    for row in masterCsvReader:
        if len(row)>0:           
            fileCheck=(row[len(row)-1])
            if fileCheck in importedFiles:
                continue
            importedFiles.extend([fileCheck])

with open('Master.csv', 'a', newline='') as masterCsv:
    masterCsvWriter = csv.writer(masterCsv, delimiter=',', quotechar='"')

    (_, _, filenames) = next(walk('InputData'))


    for filename in filenames:
        if filename in importedFiles:
            continue
        with open('InputData/'+filename, errors='ignore', newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            rowNumber=0
            for row in csvreader:
                rowNumber+=1
                if rowNumber==1:
                    continue
                row.extend([filename])
                masterCsvWriter.writerow(row)


        

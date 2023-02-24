import csv

def writecsv (datalist):
    with open ('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

# data = ['ขนมครก', 20, '07.00 น.']
# write (data)

def readcsv():
    with open ('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

data = readcsv()
print(data)


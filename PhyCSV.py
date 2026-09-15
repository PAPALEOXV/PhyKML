#Please backup CSV or Phyphox
#Please remove NaN and blank rows
import csv
name=input()
data=[]
with open(name+'.csv',mode='r',encoding='utf-8-sig')as file:
    file=csv.reader(file)
    for row in file:
        row=[row[0],row[1],row[2],row[5],row[6],row[7],row[9]]
        data.append(row)
print(len(data))
with open(name+'.csv',mode='w',encoding='utf-8-sig')as file:
    file=csv.writer(file)
    file.writerows(data)
print(name+'.csv')
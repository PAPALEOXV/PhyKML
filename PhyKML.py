#Please remove NaN and blank rows
import csv
name=input()
data=[]
with open(name+'.csv',mode='r',encoding='utf-8')as file:
    file=csv.reader(file)
    next(file)
    for row in file:
        row=row[2]+','+row[1]
        data.append(row)
print(len(data))
data=' '.join(data)
data='''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>'''+name+'''</name>
        <Placemark>
            <name>'''+name+'''</name>
            <Style>
                <LineStyle>
                    <color>ff2dc0fb</color>
                    <width>1.33</width>
                </LineStyle>
            </Style>
            <LineString>
                <coordinates>'''+data+'''</coordinates>
            </LineString>
        </Placemark>
    </Document>
</kml>'''
with open(name+'.kml',mode='w',encoding='utf-8')as file:
    file.write(data)
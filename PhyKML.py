import openpyxl
xlsx=input()
sheet=input()
name=input()
start=int(input())
xlsx=openpyxl.load_workbook(xlsx)
sheet=xlsx[sheet]
coord=[]
for row in sheet.iter_rows(min_row=start,values_only=True):
    lon=row[2]
    lat=row[1]
    if lat is not None and lon is not None:
        coord.append((float(lon),float(lat)))
print(len(coord))
data=' '.join([f'{lon},{lat}'for lon,lat in coord])
data=f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>{name}</name>
        <Placemark>
        <name>{name}</name>
        <Style>
            <LineStyle>
                <color>ff2dc0fb</color>
                <width>1.33</width>
            </LineStyle>
        </Style>
        <LineString>
            <coordinates>{data}</coordinates>
        </LineString>
        </Placemark>
    </Document>
</kml>'''
with open(f'{name}.kml','w',encoding='utf-8')as kml:
    kml.write(data)
print(f'{name}.kml')
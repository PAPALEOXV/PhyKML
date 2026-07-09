import openpyxl
workbook=openpyxl.load_workbook('exemple.xls')
sheet=workbook['Raw Data']
kml_name="exemple"
start_row=5
coord=[]
for row in sheet.iter_rows(min_row=start_row,values_only=True):
    lat=row[1]
    lon=row[2]
    if lat is not None and lon is not None:        coord.append((float(lon),float(lat)))
print(len(coord),"coords")
coords=' '.join([f'{lon},{lat}'for lon,lat in coord])
kml=f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>{kml_name}</name>
    <Placemark>
      <name>{kml_name}</name>
      <LineString>
        <coordinates>{coords}</coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>
"""
with open(f'{kml_name}.kml','w',encoding='utf-8')as out_file:
    out_file.write(kml)
print("OK")
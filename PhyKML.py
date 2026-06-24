import openpyxl
wb=openpyxl.load_workbook('example.xlsx') #file
sht=wb['Raw Data'] #sheet
kmln="example" #name
mnr=5 #start row
crd=[]
for row in sht.iter_rows(min_row=mnr,values_only=True):
    lat=row[1] #latitude
    lon=row[2] #longitude
    if lat is not None and lon is not None:
        crd.append((float(lon),float(lat)))
print(len(crd),"coords")
crds=' '.join([f'{lon},{lat}'for lon,lat in crd])
kmls=f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>{kmln}</name>
    <Placemark>
      <name>{kmln}</name>
      <LineString>
        <coordinates>{crds}</coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>
"""
with open(f'{kmln}.kml','w',encoding='utf-8')as fst:
    fst.write(kmls)
print("OK")

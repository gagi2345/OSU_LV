#Skripta zadatak_1.py ucitava podatkovni skup iz  data_C02_emission.csv.
#Dodajte programski kod u skriptu pomocu kojeg možete odgovoriti na sljedeca pitanja: 
#a) Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicina? Postoje li izostale ili 
#duplicirane vrijednosti? Obrišite ih ako postoje. Kategoricke velicine konvertirajte u tip 
#category.
#b) Koja tri automobila ima najvecu odnosno najmanju gradsku potrošnju? Ispišite u terminal: 
#ime proizvodaca, model vozila i kolika je gradska potrošnja. 
#c) Koliko vozila ima velicinu motora izmedu 2.5 i 3.5 L? Kolika je prosjecna C02 emisija 
#plinova za ova vozila?
#d) Koliko mjerenja se odnosi na vozila proizvodaca Audi? Kolika je prosjecna emisija C02 
#plinova automobila proizvodaca Audi koji imaju 4 cilindara? 
#e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecna emisija C02 plinova s obzirom na 
#broj cilindara?
#f) Kolika je prosjecna gradska potrošnja u slucaju vozila koja koriste dizel, a kolika za vozila 
#koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?
#g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvecu gradsku potrošnju goriva? 
#h) Koliko ima vozila ima rucni tip mjenjaca (bez obzira na broj brzina)? 
#i) Izracunajte korelaciju izmedu numerickih velicina. Komentirajte dobiveni rezultat.

import pandas as pd
import numpy as np
import matplotlib . pyplot as plt

data = pd.read_csv("data_C02_emission.csv")
#a)
print("Broje mjerenja:", len(data))

print(data.dtypes)

print ( data . isnull () . sum () )
print(data.duplicated().sum())
data . dropna ( axis =0 )
data . drop_duplicates ()
data = data . reset_index ( drop = True )
print(data.astype("category"))

#b)
columns=data[['Make','Model','Fuel Consumption City (L/100km)']]
print('najveca:', columns.nlargest(3,'Fuel Consumption City (L/100km)'))
print('najveca:', columns.nsmallest(3,'Fuel Consumption City (L/100km)'))

#c)
filtrirano= data[(data['Engine Size (L)']>=2.5) & (data['Engine Size (L)']<=3.5)]
print('broj vozila:', len(filtrirano))
print('prosjecna emisija:',filtrirano['CO2 Emissions (g/km)'].mean)

#d)
audi=data[data['Make']=='Audi']
print("Broj mjerenja za Audi:", len(audi))
audi4 = data[(data["Make"] == "Audi") & (data["Cylinders"] == 4)]
print("Prosjecna CO2 emisija audija:", audi4["CO2 Emissions (g/km)"].mean())

#e)
print(data["Cylinders"].value_counts())
print(data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean())

#f)
diesel = data[data["Fuel Type"] == "D"]
benz = data[data["Fuel Type"] == "X"]

print("Dizel gradska potrosnja:", diesel['Fuel Consumption City (L/100km)'].mean())
print("Dizel gradska potrosnja MEDIJAN:", diesel['Fuel Consumption City (L/100km)'].median())
print("Dizel gradska potrosnja:", benz['Fuel Consumption City (L/100km)'].mean())
print("Dizel gradska potrosnja MEDIJAN:", benz['Fuel Consumption City (L/100km)'].median())

#g)
filtriranoDizel = data[(data["Cylinders"] == 4) & (data["Fuel Type"] == "D")]
print('najvecu gradsku potrošnju goriva za dizel sa 4 cilindra:\n',filtriranoDizel.max())

#h)
manual = data[data['Transmission'].str.startswith('M') ]
print("Broj vozila s pravim ručnim mjenjačem:", len(manual))

#i)
numeric=data.select_dtypes(include='number')
correlation_matrix = numeric.corr()
print(correlation_matrix)
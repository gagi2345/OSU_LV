#Napišite programski kod koji ce prikazati sljedece vizualizacije: 
#a) Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz. 
#b) Pomocu dijagrama raspršenja prikažite odnos izmedu gradske potrošnje goriva i emisije 
#C02 plinova. Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu
#velicina, obojite tockice na dijagramu raspršenja s obzirom na tip goriva. 
#c) Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip 
#goriva. Primjecujete li grubu mjernu pogrešku u podacima? 
#d) Pomocu stupcastog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu 
#groupby.
#e) Pomocu stupcastog grafa prikažite na istoj slici prosjecnu C02 emisiju vozila s obzirom na 
#broj cilindara.
import pandas as pd
import numpy as np
import matplotlib . pyplot as plt

data=pd.read_csv('data_C02_emission.csv')

#a)

plt.hist(data['CO2 Emissions (g/km)'], bins=20, color='b', edgecolor='black')
plt.title("Raspodjela emisije CO2 (g/km)")
plt.xlabel("CO2 Emissions (g/km)")
plt.ylabel("Broj vozila")
plt.show()

#b)

data.plot.scatter(
    x='Fuel Consumption City (L/100km)',
    y='CO2 Emissions (g/km)',
    c='Fuel Type', cmap='cool', s=50,               
)
plt.show()

#c)
                              
data.boxplot(
    column=['Fuel Consumption Hwy (L/100km)'],
    by='Fuel Type')
plt.show()


#d) 
fuel_group = data.groupby('Fuel Type')

vehicle_counts = fuel_group.size()

vehicle_counts.plot(kind="bar",color="orange")
plt.xlabel('Tip goriva')
plt.ylabel("Broj vozila")
plt.xticks(rotation=0)
plt.show()


#e)
cilindersAndC02=data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cilindersAndC02.plot(kind="bar")
plt.xlabel('broj cilindara')
plt.ylabel("CO2 Emissions (g/km)")
plt.xticks(rotation=0)
plt.show()
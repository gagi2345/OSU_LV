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
#grouped = data . groupby ('Fuel Type')
#grouped . boxplot ( column = ['Fuel Consumption Hwy (L/100km)'])
                              
data.boxplot(
    column=['Fuel Consumption Hwy (L/100km)'],
    by='Fuel Type')
plt.show()

#d) e)

fuel_group = data.groupby('Fuel Type')

vehicle_counts = fuel_group.size()

avg_CO2 = fuel_group['CO2 Emissions (g/km)'].mean()

# Pozicije za stupce
x = np.arange(len(vehicle_counts))
width = 0.35  # širina stupca

# Kreiranje figure i prve osi
fig, ax1 = plt.subplots(figsize=(10,6))

# Stupci za broj vozila na lijevoj osi
ax1.bar(x - width/2, vehicle_counts, width, label='Broj vozila', color='b', edgecolor='black')
ax1.set_xlabel('Tip goriva')
ax1.set_ylabel('Broj vozila', color='b')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_xticks(x)
ax1.set_xticklabels(vehicle_counts.index)

# Druga osa y za CO2 emisiju
ax2 = ax1.twinx()
ax2.bar(x + width/2, avg_CO2, width, label='Prosječna CO2 emisija', color='orange', edgecolor='black')
ax2.set_ylabel('Prosječna CO2 emisija (g/km)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

plt.title('Broj vozila i prosječna CO2 emisija po tipu goriva')
plt.show()

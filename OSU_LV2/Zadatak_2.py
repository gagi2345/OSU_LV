#Datoteka data.csv sadrži mjerenja visine i mase provedena na muškarcima i
#ženama. Skripta zadatak_2.py ucitava dane podatke u obliku numpy polja  data pri cemu je u 
#prvom stupcu polja oznaka spola (1 muško, 0 žensko), drugi stupac polja je visina u cm, a treci
#stupac polja je masa u kg
#a) Na temelju velicine numpy polja data, na koliko osoba su izvršena mjerenja? ˇ
#b) Prikažite odnos visine i mase osobe pomocu naredbe ´ matplotlib.pyplot.scatter.
#c) Ponovite prethodni zadatak, ali prikažite mjerenja za svaku pedesetu osobu na slici.
#d) Izracunajte i ispišite u terminal minimalnu, maksimalnu i srednju vrijednost visine u ovom ˇ
#podatkovnom skupu.
#e) Ponovite zadatak pod d), ali samo za muškarce, odnosno žene. Npr. kako biste izdvojili
#muškarce, stvorite polje koje zadrži bool vrijednosti i njega koristite kao indeks retka.
#ind = (data[:,0] == 1)
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data.csv",delimiter=",",skiprows=1)

spol=data[:,0]
visina=data[:,1]
masa= data[:,2]

print("podaci:")
print(data)

print("Broj osoba je:", data.shape[0])


#visina vs masa
plt.scatter(data[:,1],data[:,2])
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Visina vs Masa")
plt.show()


plt.scatter(data[::50,1], data[::50,2])
plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Svaka 50. osoba")
plt.show()

print("Min visina:", np.min(visina))
print("Max visina:", np.max(visina))
print("Srednja visina:", np.mean(visina))#prosjecna viina


muskarci = data[data[:,0] == 1]
zene = data[data[:,0] == 0]

print("Muskarci - min:", np.min(muskarci[:,1]))
print("Muskarci - max:", np.max(muskarci[:,1]))
print("Muskarci - srednja:", np.mean(muskarci[:,1]))

print("Zene - min:", np.min(zene[:,1]))
print("Zene - max:", np.max(zene[:,1]))
print("Zene - srednja:", np.mean(zene[:,1]))
#Kvantizacija boje je proces smanjivanja broja razlicitih boja u digitalnoj slici, ali ˇ
#uzimajuci u obzir da rezultantna slika vizualno bude što sli ´ cnija originalnoj slici. Jednostavan ˇ
#nacin kvantizacije boje može se posti ˇ ci primjenom algoritma ´ K srednjih vrijednosti na RGB
#vrijednosti elemenata originalne slike. Kvantizacija se tada postiže zamjenom vrijednosti svakog
#elementa originalne slike s njemu najbližim centrom. Na slici 7.3a dan je primjer originalne
#slike koja sadrži ukupno 106,276 boja, dok je na slici 7.3b prikazana rezultantna slika nakon
#kvantizacije i koja sadrži samo 5 boja koje su odredene algoritmom ¯ K srednjih vrijednosti.
#1. Otvorite skriptu zadatak_2.py. Ova skripta ucitava originalnu RGB sliku ˇ test_1.jpg
#te ju transformira u podatkovni skup koji dimenzijama odgovara izrazu (7.2) pri cemu je ˇ n
#broj elemenata slike, a m je jednak 3. Koliko je razlicitih boja prisutno u ovoj slici? ˇ
#2. Primijenite algoritam K srednjih vrijednosti koji ce prona ´ ci grupe u RGB vrijednostima ´
#elemenata originalne slike.
#3. Vrijednost svakog elementa slike originalne slike zamijeni s njemu pripadajucim centrom. ´
#4. Usporedite dobivenu sliku s originalnom. Mijenjate broj grupa K. Komentirajte dobivene
#rezultate.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

##########################


# 1) broj različitih boja u slici
unique_colors = np.unique((img_array * 255).astype(np.uint8), axis=0)
print("Broj različitih boja u slici:", len(unique_colors))

# 2) kvantizacija boje pomoću KMeans
K = 5   # mijenjaj broj grupa / boja

km = KMeans(n_clusters=K, init='k-means++', n_init=10, random_state=0)
labels = km.fit_predict(img_array)
centers = km.cluster_centers_

# 3) svaki piksel zamijeni pripadnim centrom
img_array_aprox = centers[labels]

# vrati natrag u oblik slike
img_aprox = np.reshape(img_array_aprox, (w, h, d))

# osiguraj raspon [0,1]
img_aprox = np.clip(img_aprox, 0, 1)

# 4) prikaži kvantiziranu sliku
plt.figure()
plt.title(f"Kvantizirana slika, K={K}")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()

# 5) lakat metoda - ovisnost J o K
K_values = range(1, 11)
inertias = []

for k in K_values:
    model = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=0)
    model.fit(img_array)
    inertias.append(model.inertia_)

plt.figure()
plt.plot(K_values, inertias, 'o-')
plt.xlabel("K")
plt.ylabel("J / inertia")
plt.title("Lakat metoda za kvantizaciju slike")
plt.grid(True)
plt.show()

# 6) prikaži svaku grupu kao zasebnu binarnu sliku
for k in range(K):
    mask = (labels == k).astype(np.uint8)
    mask_img = np.reshape(mask, (w, h))

    plt.figure()
    plt.title(f"Binarna slika za grupu {k}")
    plt.imshow(mask_img, cmap='gray')
    plt.tight_layout()
    plt.show()


# 7) ispis informacija

print("Korišten broj grupa K =", K)
print("Centri (RGB):")
print(centers)
print("Vrijednost kriterijske funkcije J (inertia):", km.inertia_)
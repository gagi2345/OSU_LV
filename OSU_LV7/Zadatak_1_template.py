#Skripta zadatak_1.py sadrži funkciju generate_data koja služi za generiranje
#umjetnih podatkovnih primjera kako bi se demonstriralo grupiranje. Funkcija prima cijeli broj
#koji definira željeni broju uzoraka u skupu i cijeli broj od 1 do 5 koji definira na koji nacince
#se generirati podaci, a vraca generirani skup podataka u obliku numpy polja pricemu su prvi i 
#drugi stupac vrijednosti prve odnosno druge ulazne velicine za svaki podatak. Skripta generira 
#500 podatkovnih primjera i prikazuje ih u obliku dijagrama raspršenja.
#1. Pokrenite skriptu. Prepoznajete li koliko ima grupa u generiranim podacima? Mijenjajte
#nacin generiranja podataka. 
#2. Primijenite metodu K srednjih vrijednosti te ponovo prikažite primjere, ali svaki primjer
#obojite ovisno o njegovoj pripadnosti pojedinoj grupi. Nekoliko puta pokrenite programski
#kod. Mijenjate broj K. Što primjecujete? 
#3. Mijenjajte nacin de ˇ finiranja umjetnih primjera te promatrajte rezultate grupiranja podataka
#(koristite optimalni broj grupa). Kako komentirate dobivene rezultate?

import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering


def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
    
    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe 
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples,
                        centers = 4,
                        cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
                        random_state=random_state)
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    # 2 grupe  
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

# generiranje podatkovnih primjera
X = generate_data(500, 1)

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()

################################


# odaberi način generiranja podataka i broj grupa
flagc = 1      # mijenjaj od 1 do 5
K = 3          # mijenjaj broj grupa

# ponovno generiraj podatke za odabrani slučaj
X = generate_data(500, flagc)

# pokreni KMeans
km = KMeans(n_clusters=K, init='k-means++', n_init=10, random_state=0)
labels = km.fit_predict(X)
centers = km.cluster_centers_

# prikaži grupirane primjere
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=labels, s=20, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='x', linewidths=3)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title(f'KMeans grupiranje, flagc={flagc}, K={K}')
plt.show()


# odaberi način generiranja podataka i broj grupa
flagc = 1      # mijenjaj od 1 do 5
K = 4         # mijenjaj broj grupa

# ponovno generiraj podatke za odabrani slučaj
X = generate_data(500, flagc)

# pokreni KMeans
km = KMeans(n_clusters=K, init='k-means++', n_init=10, random_state=0)
labels = km.fit_predict(X)
centers = km.cluster_centers_

# prikaži grupirane primjere
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=labels, s=20, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='x', linewidths=3)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title(f'KMeans grupiranje, flagc={flagc}, K={K}')
plt.show()


# odaberi način generiranja podataka i broj grupa
flagc = 1      # mijenjaj od 1 do 5
K = 2          # mijenjaj broj grupa

# ponovno generiraj podatke za odabrani slučaj
X = generate_data(500, flagc)

# pokreni KMeans
km = KMeans(n_clusters=K, init='k-means++', n_init=10, random_state=0)
labels = km.fit_predict(X)
centers = km.cluster_centers_

# prikaži grupirane primjere
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=labels, s=20, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='x', linewidths=3)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title(f'KMeans grupiranje, flagc={flagc}, K={K}')
plt.show()


# odaberi način generiranja podataka i broj grupa
flagc = 1      # mijenjaj od 1 do 5
K = 5          # mijenjaj broj grupa

# ponovno generiraj podatke za odabrani slučaj
X = generate_data(500, flagc)

# pokreni KMeans
km = KMeans(n_clusters=K, init='k-means++', n_init=10, random_state=0)
labels = km.fit_predict(X)
centers = km.cluster_centers_

# prikaži grupirane primjere
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=labels, s=20, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='x', linewidths=3)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title(f'KMeans grupiranje, flagc={flagc}, K={K}')
plt.show()

# Lakat metoda - prikaz kriterijske funkcije J = inertia
K_values = range(1, 11)
inertias = []

for k in K_values:
    model = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=0)
    model.fit(X)
    inertias.append(model.inertia_)

plt.figure()
plt.plot(K_values, inertias, 'o-')
plt.xlabel('K')
plt.ylabel('J / inertia')
plt.title(f'Lakat metoda, flagc={flagc}')
plt.grid(True)
plt.show()

# Komentari za različite tipove podataka
if flagc == 1:
    print("flagc=1: očekuju se 3 dobro odvojene grupe -> KMeans radi vrlo dobro za K=3.")
elif flagc == 2:
    print("flagc=2: grupe su izdužene/rotirane -> KMeans može raditi slabije jer pretpostavlja približno 'okrugle' klastere.")
elif flagc == 3:
    print("flagc=3: očekuju se 4 grupe različitih varijanci -> dobar izbor je K=4, ali neke grupe mogu biti slabije odvojene.")
elif flagc == 4:
    print("flagc=4: koncentrični krugovi -> KMeans nije prikladan jer dijeli prostor linearno oko centara.")
elif flagc == 5:
    print("flagc=5: moons skup -> KMeans nije idealan jer grupe nisu konveksne.")
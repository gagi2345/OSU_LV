# Skripta zadatak_2.py ucitava podatkovni skup Palmer Penguins [1]. Ovaj 
#podatkovni skup sadrži mjerenja provedena na tri razlicite vrste pingvina (’Adelie’, ’Chinstrap’, ’Gentoo’) na tri razlicita otoka u podrucju Palmer Station, Antarktika. Vrsta pingvina 
#odabrana je kao izlazna velicina i pri tome su klase oznacene s cjelobrojnim vrijednostima 
#0, 1 i 2. Ulazne velicine su duljina kljuna (’bill_length_mm’) i duljina peraje u mm (’flipper_length_mm’). Za vizualizaciju podatkovnih primjera i granice odluke u skripti je dostupna
#funkcija plot_decision_region.
#a) Pomocu stupcastog dijagrama prikažite koliko primjera postoji za svaku klasu (vrstu 
#pingvina) u skupu podataka za ucenje i skupu podataka za testiranje. Koristite numpy 
#funkciju unique.
#b) Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka za ucenje.
#c) Pronadite u atributima izgradenog modela parametre modela. Koja je razlika u odnosu na 
#binarni klasifikacijski problem iz prvog zadatka?
#d) Pozovite funkciju plot_decision_region pri cemu joj predajte podatke za ucenje i 
#izgradeni model logisticke regresije. Kako komentirate dobivene rezultate? 
#e) Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke 
#regresije. Izracunajte i prikažite matricu zabune na testnim podacima. Izracunajte tocnost. 
#Pomocu classification_report funkcije izracunajte vrijednostcetiri glavne metrikena skupu podataka za testiranje.
#f) Dodajte u model još ulaznih velicina. Što se dogada s rezultatima klasifikacije na skupu
#podataka za testiranje?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, ConfusionMatrixDisplay
 
def plot_decision_region(X, y, classifier, resolution=0.02):
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
 
    # Granice grafa
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
 
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
 
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
 
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=colors[idx], marker='o',
                    edgecolor='black', label=cl)
 
 
# Učitavanje podataka, izbacivanje NA vrijednosti i pretvaranje klasa u brojeve
df = pd.read_csv('penguins.csv')
df = df.dropna()
df['species'] = df['species'].map({'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2})
 
# Ulazne veličine za početak: duljina kljuna i duljina peraje
X = df[['bill_length_mm', 'flipper_length_mm']].values
y = df['species'].values
 
# Podjela na train (80%) i test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# a) Stupčasti dijagram klasa u train i test skupu
klase_train, brojac_train = np.unique(y_train, return_counts=True)
klase_test, brojac_test = np.unique(y_test, return_counts=True)
 
plt.figure(figsize=(8, 5))
bar_width = 0.35
x_pos = np.arange(len(klase_train))
 
plt.bar(x_pos - bar_width/2, brojac_train, bar_width, label='Train skup', color='skyblue', edgecolor='k')
plt.bar(x_pos + bar_width/2, brojac_test, bar_width, label='Test skup', color='lightcoral', edgecolor='k')
 
plt.xticks(x_pos, ['Adelie (0)', 'Chinstrap (1)', 'Gentoo (2)'])
plt.ylabel('Broj primjera')
plt.title('a) Broj primjera po klasama u train i test skupu')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
 
# b) Izgradnja modela logističke regresije
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
 
# c) Parametri modela
print("c) Parametri modela")
print("Intercept (theta_0):\n", model.intercept_)
print("Koeficijenti (theta_1, theta_2):\n", model.coef_)
print("\nOdgovor na pitanje (c):")
print("Razlika u odnosu na 1. zadatak je u tome što je ovo problem s 3 klase (višeklasna klasifikacija).")
print("Zbog toga model nema samo jedan pravac (jedan set parametara), već gradi više hiperravnina.")
print("Dimenzije parametara su sada matrica (3x2 za koeficijente, i 3 za intercept), po jedan set za svaku klasu.\n")
 
# d) Crtanje granice odluke na train skupu
plt.figure(figsize=(8, 6))
plot_decision_region(X_train, y_train, model)
plt.title('d) Granica odluke na skupu za učenje')
plt.xlabel('Duljina kljuna (mm)')
plt.ylabel('Duljina peraje (mm)')
plt.legend(['Adelie (0)', 'Chinstrap (1)', 'Gentoo (2)'])
plt.show()
 
print("d) Komentar granice odluke")
print("Model uspijeva dosta dobro odvojiti klasu 2 (Gentoo) od ostalih jer imaju osjetno veće peraje.")
print("Međutim, između klase 0 i klase 1 postoji preklapanje koje linearni model (logistička regresija)")
print("samo s ove 2 značajke ne može savršeno razdvojiti.\n")
 
# e) Klasifikacija testnog skupa i metrike
y_pred = model.predict(X_test)
 
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
 
print("e) Metrike na testnom skupu")
print(f"Točnost (Accuracy): {acc:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))
 
# Prikaz matrice zabune
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Adelie', 'Chinstrap', 'Gentoo'])
disp.plot(cmap='Blues')
plt.title('e) Matrica zabune na testnom skupu')
plt.show()
 
# f) Dodavanje još ulaznih veličina
print("f) Dodavanje novih značajki")
# i bill_depth_mm te body_mass_g
X_sve = df[['bill_length_mm', 'flipper_length_mm', 'bill_depth_mm', 'body_mass_g']].values
 
# podjela, koristim iste postavke
X_train_f, X_test_f, y_train_f, y_test_f = train_test_split(X_sve, y, test_size=0.2, random_state=42)
 
# Novi model
model_sve = LogisticRegression(max_iter=2000) # Još veći iter zbog većih brojeva (masa u gramima)
model_sve.fit(X_train_f, y_train_f)
 
y_pred_f = model_sve.predict(X_test_f)
acc_f = accuracy_score(y_test_f, y_pred_f)
 
print(f"Točnost sa svim značajkama: {acc_f:.4f}\n")
print("Classification Report (Sve značajke):")
print(classification_report(y_test_f, y_pred_f))
 
print("\nOdgovor na pitanje (f):")
print("Kada dodamo još ulaznih veličina (poput dubine kljuna i mase tijela), modelu dajemo više informacija.")
print("Kao što vidimo iz rezultata, točnost modela se obično poveća jer sada ima dodatne dimenzije")
print("u kojima lakše može linearno odvojiti klase koje su se ranije preklapale (npr. Adelie i Chinstrap).")
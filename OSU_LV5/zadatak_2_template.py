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
#Pomocu classification_report funkcije izracunajte vrijednostcetiri glavne metrike

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split

labels= {0:'Adelie', 1:'Chinstrap', 2:'Gentoo'}

def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    edgecolor = 'w',
                    label=labels[cl])

# ucitaj podatke
df = pd.read_csv("penguins.csv")

# izostale vrijednosti po stupcima
print(df.isnull().sum())

# spol ima 11 izostalih vrijednosti; izbacit cemo ovaj stupac
df = df.drop(columns=['sex'])

# obrisi redove s izostalim vrijednostima
df.dropna(axis=0, inplace=True)

# kategoricka varijabla vrsta - kodiranje
df['species'].replace({'Adelie' : 0,
                        'Chinstrap' : 1,
                        'Gentoo': 2}, inplace = True)

print(df.info())

# izlazna velicina: species
output_variable = ['species']

# ulazne velicine: bill length, flipper_length
input_variables = ['bill_length_mm',
                    'flipper_length_mm']

X = df[input_variables].to_numpy()
y = df[output_variable].to_numpy()

# podjela train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

#a)
classes_train, counts_train = np.unique(y_train, return_counts=True)
classes_test, counts_test = np.unique(y_test, return_counts=True)

plt.figure()
x=np.arange(len(classes_train))

plt.bar(x-0.2, counts_train, width=0.4, label="Train")
plt.bar(x+0.2, counts_test, width=0.4, label="Test")  # pomaknuto da se ne preklapaju

plt.xticks(x, [labels.get(c, c) for c in classes_train])
plt.xlabel("vrsta pingvina")
plt.ylabel("Broj primjeraka")
plt.title("broj primjera po klasama train i test")
plt.legend()
plt.show()


#b)
from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression(solver="lbfgs", max_iter=1000)
lr_model.fit(X_train, y_train.ravel())

y_train_p = lr_model.predict(X_train)
y_test_p = lr_model.predict(X_test)


#c)
print("Klase modela:", lr_model.classes_)
print("Koeficijenti modela (weights):\n", lr_model.coef_)
print("Intercepti (bias):\n", lr_model.intercept_)


#d)
#plot_decision_regions(X_train, y_train, lr_model) #sama radi odluke
#plt.xlabel('bill_length_mm')
##plt.ylabel('flipper_length_mm')
#plt.title('Granica odluke - podaci za ucenje')
#plt.legend()
#lt.show()

#e)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, classification_report
print(f'Tocnost: {accuracy_score(y_test, y_test_p):.4f}')
print(classification_report(y_test, y_test_p))

disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.title('Matrica zabune')
plt.show()

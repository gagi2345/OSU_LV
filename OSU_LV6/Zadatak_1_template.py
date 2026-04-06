
#Skripta zadatak_1.py ucitava Social_Network_Ads.csv skup podataka [2].
#Ovaj skup sadrži podatke o korisnicima koji jesu ili nisu napravili kupovinu za prikazani oglas.
#Podaci o korisnicima su spol, dob i procijenjena placa. Razmatra se binarni klasifikacijski
#roblem gdje su dob i procijenjena placa ulazne velicine, dok je kupovina (0 ili 1) izlazna 
#velicina. Za vizualizaciju podatkovnih primjera i granice odluke u skripti je dostupna funkcija 
#plot_decision_region [1]. Podaci su podijeljeni na skup za ucenje i skup za testiranje modela 
#u omjeru 80%-20% te su standardizirani. Izgraden je model logisticke regresije te je izracunata 
#njegova tocnost na skupu podataka za ucenje i skupu podataka za testiranje. Potrebno je: 
#1. Izradite algoritam KNN na skupu podataka za ucenje (uz K=5). Izracunajte tocnost 
#klasifikacije na skupu podataka za ucenje i skupu podataka za testiranje. Usporedite 
#dobivene rezultate s rezultatima logisticke regresije. Što primjecujete vezano uz dobivenu 
#granicu odluke KNN modela?
#2. Kako izgleda granica odluke kada je K =1 i kada je K = 100?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

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
                    label=cl)


# ucitaj podatke
data = pd.read_csv("Social_Network_Ads.csv")
print(data.info())

data.hist()
plt.show()

# dataframe u numpy
X = data[["Age","EstimatedSalary"]].to_numpy()
y = data["Purchased"].to_numpy()

# podijeli podatke u omjeru 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify=y, random_state = 10)

# skaliraj ulazne velicine
sc = StandardScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform((X_test))

# Model logisticke regresije
LogReg_model = LogisticRegression(penalty=None) 
LogReg_model.fit(X_train_n, y_train)

# Evaluacija modela logisticke regresije
y_train_p = LogReg_model.predict(X_train_n)
y_test_p = LogReg_model.predict(X_test_n)

print("Logisticka regresija: ")
print("Tocnost train: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
print("Tocnost test: " + "{:0.3f}".format((accuracy_score(y_test, y_test_p))))

# granica odluke pomocu logisticke regresije
plot_decision_regions(X_train_n, y_train, classifier=LogReg_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("Tocnost: " + "{:0.3f}".format((accuracy_score(y_train, y_train_p))))
plt.tight_layout()
plt.show()
##############################
# KNN model K=5
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_n, y_train)

# evaluacija
y_train_knn = knn_model.predict(X_train_n)
y_test_knn = knn_model.predict(X_test_n)

print("\n\n####################\nKNN (K=5): ")
print("Tocnost train: " + "{:0.3f}".format(accuracy_score(y_train, y_train_knn)))
print("Tocnost test: " + "{:0.3f}".format(accuracy_score(y_test, y_test_knn)))

# granica odluke
plot_decision_regions(X_train_n, y_train, classifier=knn_model)
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.legend(loc='upper left')
plt.title("KNN K=5")
plt.tight_layout()
plt.show()

# K = 1
knn_model_1 = KNeighborsClassifier(n_neighbors=1)
knn_model_1.fit(X_train_n, y_train)

plot_decision_regions(X_train_n, y_train, classifier=knn_model_1)
plt.title("KNN K=1")
plt.show()


# K = 100
knn_model_100 = KNeighborsClassifier(n_neighbors=100)
knn_model_100.fit(X_train_n, y_train)

plot_decision_regions(X_train_n, y_train, classifier=knn_model_100)
plt.title("KNN K=100")
plt.show()

#Logistička regresija → daje linearnu granicu odluke (ravna linija).
#KNN → daje nelinearnu, zakrivljenu granicu koja prati raspored podataka.
#KNN se bolje prilagođava lokalnoj strukturi podataka.
#Logistička regresija je jednostavniji model i manje sklona overfittingu.
#K	Granica odluke	Objašnjenje
#K = 1	vrlo nazubljena	overfitting
#K = 5	glatka	dobra generalizacija
#K = 100	skoro ravna	underfitting
###########################################
#Pomocu unakrsne validacije odredite optimalnu vrijednost hiperparametra K
#algoritma KNN za podatke iz Zadatka 1.

# definiraj pipeline (skaliranje + KNN)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

# raspon K vrijednosti koje testiramo
param_grid = {
    'knn__n_neighbors': np.arange(1, 51)  # K od 1 do 50
}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("\n\n################\nNajbolji K:", grid.best_params_['knn__n_neighbors'])
print("Najbolja točnost (CV): {:.3f}".format(grid.best_score_))

best_model = grid.best_estimator_

y_train_best = best_model.predict(X_train)
y_test_best = best_model.predict(X_test)

print("\nKNN (optimalni K):")
print("Tocnost train: {:.3f}".format(accuracy_score(y_train, y_train_best)))
print("Tocnost test: {:.3f}".format(accuracy_score(y_test, y_test_best)))

####################################
#Na podatke iz Zadatka 1 primijenite SVM model koji koristi RBF kernel funkciju
#te prikažite dobivenu granicu odluke. Mijenjajte vrijednost hiperparametra C i γ. Kako promjena
#ovih hiperparametara utjece na granicu odluke te pogrešku na skupu podataka za testiranje? 
#Mijenjajte tip kernela koji se koristi. Što primjecujete?


# SVM RBF
svm_model = svm.SVC(kernel='rbf', C=1, gamma=0.1)
svm_model.fit(X_train_n, y_train)

# evaluacija
y_train_svm = svm_model.predict(X_train_n)
y_test_svm = svm_model.predict(X_test_n)

print("\n\n#####################\nSVM RBF:")
print("Tocnost train: {:.3f}".format(accuracy_score(y_train, y_train_svm)))
print("Tocnost test: {:.3f}".format(accuracy_score(y_test, y_test_svm)))

# granica odluke
plot_decision_regions(X_train_n, y_train, classifier=svm_model)
plt.title("SVM RBF")
plt.show()


#C
for C in [0.1, 1, 10, 100]:
    svm_model = svm.SVC(kernel='rbf', C=C, gamma=0.1)
    svm_model.fit(X_train_n, y_train)
    
    y_test_svm = svm_model.predict(X_test_n)
    print("C =", C, "Test accuracy =", accuracy_score(y_test, y_test_svm))
    
    plot_decision_regions(X_train_n, y_train, classifier=svm_model)
    plt.title("SVM RBF, C=" + str(C))
    plt.show()

#γ
for g in [0.01, 0.1, 1, 10]:
    svm_model = svm.SVC(kernel='rbf', C=1, gamma=g)
    svm_model.fit(X_train_n, y_train)
    
    y_test_svm = svm_model.predict(X_test_n)
    print("gamma =", g, "Test accuracy =", accuracy_score(y_test, y_test_svm))
    
    plot_decision_regions(X_train_n, y_train, classifier=svm_model)
    plt.title("SVM RBF, gamma=" + str(g))
    plt.show()

#Mijenjanje kernela
for k in ['linear', 'poly', 'rbf']:
    svm_model = svm.SVC(kernel=k)
    svm_model.fit(X_train_n, y_train)
    
    y_test_svm = svm_model.predict(X_test_n)
    print("Kernel =", k, "Test accuracy =", accuracy_score(y_test, y_test_svm))
    
    plot_decision_regions(X_train_n, y_train, classifier=svm_model)
    plt.title("SVM kernel = " + k)
    plt.show()
#Parametar C kontrolira kompromis između širine margine i pogreške klasifikacije. Veći C dovodi do složenije granice odluke i mogućeg overfittinga.
#Parametar γ određuje utjecaj pojedinih točaka – veće vrijednosti γ daju kompleksniju granicu odluke.
#Promjenom kernela mijenja se oblik granice odluke: linear kernel daje linearnu granicu, dok RBF i polynomial kernel daju nelinearne granice. RBF kernel se pokazao najfleksibilnijim i često daje najbolje rezultate.
#################################

#Pomocu unakrsne validacije odredite optimalnu vrijednost hiperparametra  C i γ
#algoritma SVM za problem iz Zadatka 1.


# parametri koje testiramo
param_grid = {
    'C': [0.1, 1, 10, 100, 1000],
    'gamma': [0.001, 0.01, 0.1, 1, 10],
    'kernel': ['rbf']
}

svm_model = svm.SVC()

# GridSearchCV
grid = GridSearchCV(svm_model, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train_n, y_train)

print("\n\n##########\nNajbolji parametri:", grid.best_params_)
print("Najbolja CV točnost:", grid.best_score_)

best_svm = grid.best_estimator_

y_train_best = best_svm.predict(X_train_n)
y_test_best = best_svm.predict(X_test_n)

print("\n\nTocnost train:", accuracy_score(y_train, y_train_best))
print("Tocnost test:", accuracy_score(y_test, y_test_best))

plot_decision_regions(X_train_n, y_train, classifier=best_svm)
plt.title("SVM optimalni C i gamma")
plt.show()
#Skripta zadatak_1.py generira umjetni binarni klasifikacijski problem s dvije
#ulazne velicine. Podaci su podijeljeni na skup za ucenje i skup za testiranje modela. 
#a) Prikažite podatke za ucenje u x1 −x2 ravnini matplotlib biblioteke pri cemu podatke obojite 
#s obzirom na klasu. Prikažite i podatke iz skupa za testiranje, ali za njih koristite drugi
#marker (npr. ’x’). Koristite funkciju scatter koja osim podataka prima i parametre c i
#cmap kojima je moguce definirati boju svake klase.
#b) Izgradite model logisticke regresije pomocu scikit-learn biblioteke na temelju skupa podataka za ucenje. 
#c) Pronadite u atributima izgradenog modela parametre modela. Prikažite granicu odluke 
#naucenog modela u ravnini x1 − x2 zajedno s podacima za ucenje. Napomena: granica 
#odluke u ravnini x1 −x2 definirana je kao krivulja: θ0 +θ1x1 +θ2x2 = 0.
#d) Provedite klasifikaciju skupa podataka za testiranje pomocu izgradenog modela logisticke 
#regresije. Izracunajte i prikažite matricu zabune na testnim podacima. Izracunate tocnost, 
#preciznost i odziv na skupu podataka za testiranje.
#e) Prikažite skup za testiranje u ravnini x1 −x2. Zelenom bojom oznacite dobro klasificirane
#primjere dok pogrešno klasificirane primjere oznacite crnom bojom.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
#a)
plt.figure()

plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap="viridis",  label="Train")

plt.scatter(X_test[:,0], X_test[:,1], c=y_test, cmap="viridis",marker="x", label="Test")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("prikaz podataka train i test")
plt.legend()
plt.show()

#b)
lr_model=LogisticRegression()
lr_model.fit(X_train, y_train)



#c)

w1, w2 = lr_model.coef_[0]
b = lr_model.intercept_[0]

print("Koeficijenti: ", w1,w2)
print("intercept: ", b)


# granica odluke
x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_values = -(w1 * x_values + b) / w2

# crtanje podataka
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', marker='x')

# crtanje granice
plt.plot(x_values, y_values)

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Granica odluke - logisticka regresija")
plt.show()

#d)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score


y_test_p=lr_model.predict(X_test)
cm=confusion_matrix(y_test,y_test_p)
print("matrica zabune:", cm)

disp=ConfusionMatrixDisplay(confusion_matrix(y_test,y_test_p))
disp.plot()
plt.show()


accuracy=accuracy_score(y_test,y_test_p)
precision=precision_score(y_test,y_test_p)
recall=recall_score(y_test,y_test_p)
print("tocnost:",accuracy)
print("preciznost: ",precision)
print("odziv: ", recall)

#e)

good=y_test_p==y_test
bad=y_test_p!=y_test

plt.figure()
plt.scatter(X_test[good,0], X_test[good,1],c="green",label="dobro klasificirani")
plt.scatter(X_test[bad,0], X_test[bad,1],c="black",label="lose klasificirani")

plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.show()
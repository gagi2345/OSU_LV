#Napišite skriptu koja ce ucitati izgradenu mrežu iz zadatka 1 i MNIST skup 
#podataka. Pomocu matplotlib biblioteke potrebno je prikazati nekoliko loše klasi ficiranih slika iz
#skupa podataka za testiranje. Pri tome u naslov slike napišite stvarnu oznaku i oznaku predvidenu 
#mrežom.

import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt

# učitaj spremljeni model iz zadatka 1
model = keras.models.load_model("mnist_model.keras")

# učitaj MNIST podatke
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# skaliranje na [0,1]
x_test_s = x_test.astype("float32") / 255

# dodaj dimenziju kanala -> (28, 28, 1)
x_test_s = np.expand_dims(x_test_s, -1)

# predikcija nad testnim skupom
y_pred_prob = model.predict(x_test_s)
y_pred = np.argmax(y_pred_prob, axis=1)

# pronađi pogrešno klasificirane primjere
pogresni = np.where(y_pred != y_test)[0]

print("Broj pogrešno klasificiranih slika:", len(pogresni))

# prikaži nekoliko pogrešno klasificiranih slika
broj_slika = 9

plt.figure(figsize=(10, 10))
for i in range(broj_slika):
    idx = pogresni[i]
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_test[idx], cmap="gray")
    plt.title(f"Stvarna: {y_test[idx]}, Predviđena: {y_pred[idx]}")
    plt.axis("off")

plt.tight_layout()
plt.show()
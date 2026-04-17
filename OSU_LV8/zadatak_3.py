#Napišite skriptu koja ce ucitati izgradenu mrežu iz zadatka 1. Nadalje, skripta 
#treba ucitati sliku test.png sa diska. Dodajte u skriptu kod koji ce prilagoditi sliku za mrežu, 
#klasificirati sliku pomocu izgradene mreže te ispisati rezultat u terminal. Promijenite sliku 
#pomocu nekog grafickog alata (npr. pomocu Windows Paint-a nacrtajte broj 2) i ponovo pokrenite 
#skriptu. Komentirajte dobivene rezultate za razlicite napisane znamenke.

import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt

# učitaj spremljeni model
model = keras.models.load_model("mnist_model.keras")

# učitaj sliku kao grayscale i promijeni veličinu na 28x28
img = keras.utils.load_img("test.png", color_mode="grayscale", target_size=(28, 28))

# pretvori u numpy polje
img_array = keras.utils.img_to_array(img)

# ukloni zadnju dimenziju za lakšu obradu
img_array = img_array[:, :, 0]

# inverzija boja zbog MNIST formata
img_array = 255 - img_array

# skaliranje na [0,1]
img_array = img_array.astype("float32") / 255.0

# dodavanje dimenzija: (1, 28, 28, 1)
img_array = np.expand_dims(img_array, axis=0)
img_array = np.expand_dims(img_array, axis=-1)

# klasifikacija
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction, axis=1)[0]

print("Predviđena znamenka:", predicted_class)
print("Vjerojatnosti po razredima:", prediction[0])

plt.imshow(img_array[0, :, :, 0], cmap="gray")
plt.title(f"Predikcija: {predicted_class}")
plt.axis("off")
plt.show()
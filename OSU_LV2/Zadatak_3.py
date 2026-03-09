#Skripta zadatak_3.py ucitava sliku ’road.jpg’. Manipulacijom odgovarajuce
#numpy matrice pokušajte:

import numpy as np
import matplotlib . pyplot as plt

img = plt.imread ("road.jpg")

#a) posvijetliti sliku,
bright = img + 50
bright = np.clip(bright, 0, 255)
plt.imshow(bright, cmap="gray")
plt.title("Posvijetljena slika")
plt.axis("off")
plt.show()

#b) prikazati samo drugu cetvrtinu slike po širini,
h, w = img.shape[:2]
quarter = img[:, w//4:w//2]

plt.imshow(quarter)
plt.title("Druga cetvrtina")
plt.axis("off")
plt.show()

#c) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
rotated = np.rot90(img, 1)

plt.imshow(rotated)
plt.title("Rotirana slika")
plt.axis("off")
plt.show()

#d) zrcaliti sliku.
mirror = np.fliplr(img)

plt.imshow(mirror)
plt.title("Zrcaljena slika")
plt.axis("off")
plt.show()
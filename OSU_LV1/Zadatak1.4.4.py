rijecnik = {}

with open("song.txt", "r", encoding="utf-8") as dat:
    for red in dat:
        red = red.lower()
        rijeci = red.split()

        for rijec in rijeci:
            rijec = rijec.strip(".,!?;:\"()[]")

            if rijec in rijecnik:
                rijecnik[rijec] += 1
            else:
                rijecnik[rijec] = 1

# pronalazak riječi koje se pojavljuju samo jednom
jednom = []

for kljuc, vrijednost in rijecnik.items():
    if vrijednost == 1:
        jednom.append(kljuc)

print("Broj riječi koje se pojavljuju samo jednom:", len(jednom))
print("Te riječi su:")
for rijec in jednom:
    print(rijec)

brojevi= []

while True:
    unos=input("unesite broj ili 'Done' za kraj unosa: ")
    if unos == "Done":
        break

    try:
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        print("pogrešan unos")

if len(brojevi) == 0:
    print("nije unesen niti jedan broj")
else:
    print("unjeli ste ", len(brojevi)," brojeva")
    print("Srednja vrijednost brojeva je", sum(brojevi)/len(brojevi))
    print("Najmanji broj je: ", min(brojevi))
    print("Najveci broj je: ", max(brojevi))

#Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji 
#sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
#potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
#vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
#(npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovarajucu poruku.
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

print("unjeli ste ", len(brojevi)," brojeva")
print("Srednja vrijednost brojeva je", sum(brojevi)/len(brojevi))
print("Najmanji broj je: ", min(brojevi))
print("Najveci broj je: ", max(brojevi))
print("sortirano", sorted(brojevi))
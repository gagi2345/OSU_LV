#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je placen 
#po radnom satu. Koristite ugradenu Python metodu input(). Nakon toga izracunajte koliko 
#je korisnik zaradio i ispišite na ekran. Na kraju prepravite rješenje na nacin da ukupni iznos 
#izracunavate u zasebnoj funkciji naziva ˇ total_euro.

radni_sati= int(input("Unesi radne sate: "))
placeno = int(input("Unesi placu po satu: "))

#ukupno_zaradeno = radni_sati*placeno

#print("Ukupna placa: ", ukupno_zaradeno)
def ukupna_placa(a,b):
     return a*b

print("Ukupna placa: ", ukupna_placa(radni_sati, placeno))

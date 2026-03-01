radni_sati= int(input("Unesi radne sate: "))
placeno = int(input("Unesi placu po satu: "))

#ukupno_zaradeno = radni_sati*placeno

#print("Ukupna placa: ", ukupno_zaradeno)
def ukupna_placa(a,b):
     return a*b

print("Ukupna placa: ", ukupna_placa(radni_sati, placeno))

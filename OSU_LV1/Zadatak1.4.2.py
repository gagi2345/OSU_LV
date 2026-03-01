try:
    ocjena= float(input("unesi ocjenu od 0.0 do 1.0: "))

    if ocjena <0.0 or ocjena > 1.0:
        print(" Nevaljan unos ocjene!")
    elif ocjena >=0.9:
        print("A")
    elif ocjena >= 0.8:
        print("B")
    elif ocjena >=0.7:
        print("C")
    elif ocjena >=0.6:
        print("D")
    else:
        print("F")
except ValueError:
    print("nije unesen broj")

ham_broj_rijeci = 0
ham_broj_poruka = 0

spam_broj_rijeci = 0
spam_broj_poruka = 0
spam_usklicnik = 0

with open("SMSSpamCollection.txt", "r", encoding="utf-8") as dat:
    for red in dat:
        red = red.strip() #uklanja prazan prostor
        
        # Razdvajanje oznake i poruke (samo prvo razdvajanje!)
        tip, poruka = red.split(maxsplit=1)

        rijeci = poruka.split()
        broj_rijeci = len(rijeci)

        if tip == "ham":
            ham_broj_poruka += 1
            ham_broj_rijeci += broj_rijeci

        elif tip == "spam":
            spam_broj_poruka += 1
            spam_broj_rijeci += broj_rijeci
            
            if poruka.endswith("!"):
                spam_usklicnik += 1


prosjek_ham = ham_broj_rijeci / ham_broj_poruka
prosjek_spam = spam_broj_rijeci / spam_broj_poruka

print("Prosječan broj riječi (ham):", prosjek_ham)
print("Prosječan broj riječi (spam):", prosjek_spam)
print("Broj spam poruka koje završavaju uskličnikom:", spam_usklicnik)

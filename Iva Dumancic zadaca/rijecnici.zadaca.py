import random 
imena=['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra', 'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']
rijecnik=dict()
for i in imena:
    rijecnik[i]=random.randint(1,5)
print(rijecnik)

broj_ocjena=dict()
for ocjena in rijecnik.values():
    if ocjena in broj_ocjena:
        broj_ocjena[ocjena]+=1
    else:
        broj_ocjena[ocjena]= 1
print(broj_ocjena)
broj_ucenika=len(rijecnik)
print(broj_ucenika)
zbroj=0
for ocjena in rijecnik.values():
    if ocjena > 1:
        zbroj += 1
print(zbroj)
postotak=(zbroj/broj_ucenika)*100
print("Postotak prolaznosti je",round(postotak,2),"%")


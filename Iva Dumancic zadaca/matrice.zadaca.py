"""Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice."""

import random
redci=7
stupci=7
matrica=[]

for i in range(redci):
  red=[]
  for j in range(stupci):
    unos=random.randint(1,9)
    red.append(unos)
  matrica.append(red)

for i in range(redci):
  for j in range(stupci):
    print(matrica[i][j],end=" ")
  print()

zbroj=0 
for i in range (redci):
    for j in range (stupci):
        if i==0 or i ==6 or j ==0 or j==6:
            zbroj +=matrica[i][j]
print("Zbroj elemenaata na rubovima matrice je:",zbroj)

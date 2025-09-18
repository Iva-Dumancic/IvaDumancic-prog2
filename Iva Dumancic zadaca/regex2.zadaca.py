"""Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime.
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
"""
import re
unos1=input("Unesi mail adresu:")
reg1="[a-zA-Z]+[a-zA-Z]+@fpmoz.sum.ba$"
result1=re.findall(reg1,unos1)
print(result1)

unos2= input("Unesi eduId: ")
reg2="^[a-zA-Z][a-zA-Z]+[0-9]*@sum.ba$"
result2=re.findall(reg2,unos2)
print(result2)
if result1 and result2:
    print("Mail i eduId su ispravni!")

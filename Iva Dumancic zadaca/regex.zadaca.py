"""Potrebno napisati regex koji vraca podudaranje
ukoliko se unese string koji počinje
kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
String mora sadržavati bar jedan broj između 0 i 5 i razmak."""
import re
unos=input("Unesite string:")
reg='^r+.*r+$'
uvjet1=re.match(reg,unos)

reg2='[0-5]'
uvjet2=re.search(reg2,unos)

reg3 ='\s'
uvjet3=re.search(reg3,unos)

if uvjet1 and uvjet2 and uvjet3:
    print("ispravno")

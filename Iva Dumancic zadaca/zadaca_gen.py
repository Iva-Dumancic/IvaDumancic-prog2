def parni_brojevi(n):
    for i in range(n):
        if i % 2==0:
            yield i
def neparni_brojevi(n):
    for i  in range(n):
        if i % 2 != 0:
            yield i
            
my_gen1=parni_brojevi(5)
my_gen2=neparni_brojevi(5)

for broj in my_gen1:
    print(broj)
for el in my_gen2:
    print(el)

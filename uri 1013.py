valores = input()
lista = valores.split()
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
maior = (a + b + abs(a - b))  / 2
maior2 = (maior + c + abs(maior - c))/2
print("%d eh o maior" %maior2)

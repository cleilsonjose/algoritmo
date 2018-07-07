a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
positivo = 0
exu = 5
soma = 0
lista = [a,b,c,d,e,f]
while exu > -1:
    if lista[exu] > 0:
        positivo = positivo +1
        soma = lista[exu] + soma
    exu = exu - 1
media = soma/positivo
print("{} valores positivos".format(positivo))
print("{0:.1f}".format(media))

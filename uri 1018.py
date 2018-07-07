valor = int(input())
if 0 < valor < 1000000:
    print("{}".format(valor))
    cem = valor//100 
    aux1 = valor%100
    cinquenta = aux1 // 50
    aux2 = aux1 % 50
    vinte = aux2 // 20
    aux3 = aux2 % 20
    dez = aux3 //10
    aux4 = aux3 % 10
    cinco = aux4 //5
    aux5 = aux4 % 5
    dois = aux5 // 2
    um = aux5 % 2
    
print("{} nota(s) de R$ 100,00".format(cem))
print("{} nota(s) de R$ 50,00".format(cinquenta))
print("{} nota(s) de R$ 20,00".format(vinte))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinco))
print("{} nota(s) de R$ 2,00".format(dois))
print("{} nota(s) de R$ 1,00".format(um))

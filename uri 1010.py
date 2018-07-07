a1 = input()
a2 = input()

lista1 = a1.split()

numpeca1 = int(lista1[0])
quantpeca1 = int(lista1[1])
valorpeca1 = float(lista1[2])

lista2 = a2.split()

numpeca2 = int(lista2[0])
quantpeca2 = int(lista2[1])
valorpeca2 = float(lista2[2])

valor = valorpeca1 * quantpeca1 + valorpeca2 * quantpeca2
print("VALOR A PAGAR: R$ %1.2f"%valor)

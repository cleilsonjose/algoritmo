N = float(input())
N +=  0.001
if 0 < N < 1000000.00:
    #notas
    cem = N//100
    cinquenta = (N%100)//50
    vinte = ((N%100)%50)//20
    dez =  (((N%100)%50)%20)//10
    cinco = ((((N%100)%50)%20)%10)//5
    dois = (((((N%100)%50)%20)%10)%5)//2
    #moedas
    um = ((((((N%100)%50)%20)%10)%5)%2)//1
    cinquentaC = (((((((N%100)%50)%20)%10)%5)%2)%1)//0.5
    vintecincoC = ((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)//0.25
    dezC = (((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)//0.10
    cincoC = ((((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.10)//0.05
    umC = (((((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.10)%0.05)//0.01
print("NOTAS:")
print("{0:.0f} nota(s) de R$ 100.00".format(cem))
print("{0:.0f} nota(s) de R$ 50.00".format(cinquenta))
print("{0:.0f} nota(s) de R$ 20.00".format(vinte))
print("{0:.0f} nota(s) de R$ 10.00".format(dez))
print("{0:.0f} nota(s) de R$ 5.00".format(cinco))
print("{0:.0f} nota(s) de R$ 2.00".format(dois))
print("MOEDAS:")
print("{0:.0f} moeda(s) de R$ 1.00".format(um))
print("{0:.0f} moeda(s) de R$ 0.50".format(cinquentaC))
print("{0:.0f} moeda(s) de R$ 0.25".format(vintecincoC))
print("{0:.0f} moeda(s) de R$ 0.10".format(dezC))
print("{0:.0f} moeda(s) de R$ 0.05".format(cincoC))
print("{0:.0f} moeda(s) de R$ 0.01".format(umC))

lista=[None]*61
lista[0] = 0
lista[1] = 1
for i in range(2,61,1):
    lista[i] = lista[i-1] + lista[i-2]
T = int(input())
for i in range(T):
     N = int(input())
     print("Fib(%d) = %d" %(N,lista[N]))
     


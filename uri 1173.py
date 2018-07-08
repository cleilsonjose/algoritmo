N=[None ]*10
aux=int(input())
N[0]=aux
if N[0]<=50:
    for i in range(10):
        if i > 0:
            aux=aux*2
            N[i]=aux
        print("N[%d] = %d" %(i,N[i]))

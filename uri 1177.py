N=[None]*1000
T= int(input())
cont = 0
if T>=2 and T<=50:
    for i in range(1000):
        if cont==T:
            cont=0
        N[i] = cont
        cont+=1
    for i in range(1000):
        print("N[%d] = %d"%(i,N[i]))
     


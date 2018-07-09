X = float(input())
N=[None]*100
N[0] = X
for i in range(1,100,1):
    X= X/2
    N[i] = X
for i in range(100):
    print("N[%d] = %.4f"%(i,N[i]))
     


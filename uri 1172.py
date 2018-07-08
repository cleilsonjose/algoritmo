X=[None ]*10
for i in range(10):
    X[i]=int(input())
    if X[i]<=0:
        X[i]=1
    print("X[%d] = %d" %(i,X[i]))

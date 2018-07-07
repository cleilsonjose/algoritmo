while True:
    soma = 0
    X = int(input())
    if X==0:
        break
    else:
        if X%2!=0:
            X=X+1
        for i in range(X,X+10,2):
            soma+=i
        print(soma)

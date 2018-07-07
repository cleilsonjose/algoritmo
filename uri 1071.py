soma = 0
X = int(input())
Y = int(input())
if X>Y:
    a=Y
    Y=X
    X=a
for i in range(X+1,Y):
    if i%2!=0:
        soma+=i
print(soma)

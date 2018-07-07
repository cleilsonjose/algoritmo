cont=idade = soma=0
while idade >= 0:
    idade = int(input())
    if idade>=0:
        soma+=idade
        cont+=1
    else:
        break
print("%.2f" %(soma/cont))

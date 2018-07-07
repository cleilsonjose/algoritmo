valor = input().split()

codigo = int(valor[0])
quant = int(valor[1])

if codigo == 1:
    total = quant * 4.00
elif codigo == 2:
    total = quant * 4.50
elif codigo == 3:
    total = quant * 5.00
elif codigo == 4:
    total = quant * 2.00
else:
    total = quant * 1.50
    
print("Total: R$ {0:.2f}".format(total))

idade = int(input())

anos = idade//365
mes = (idade%365)//30
dias = (idade%365)%30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dias))

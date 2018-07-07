lista = input().split()
a = int(lista[0])
b = int(lista[1])
tempo=24-a
if a>=0 or a <= 24 and a>=0 or a <= 24:
    if a == b:
        print("O JOGO DUROU 24 HORA(S)")
    elif a>b:
        tempo = tempo +b
        print("O JOGO DUROU %d HORA(S)" %tempo)
    else:
        tempo = (b-a)
        print("O JOGO DUROU %d HORA(S)" %tempo)

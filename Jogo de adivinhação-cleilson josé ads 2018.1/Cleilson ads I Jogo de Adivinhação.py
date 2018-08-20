from random import randint
print("************************************\n"
"** ADS 2018.1 - IFPI Campus Picos **\n"
"****** Aluno: Cleilson Josè ********\n"
"* Bem vindo ao Jogo de Adivinhação *\n"
"************************************\n")
def jogo(nome,numt,erro):
    valendo=True
    tentativa=1
    N=randint(1,100)
    op=3
    #print(N)
    pontus=100
    while valendo:
        if tentativa<=numt:
            print("Tentativa {}".format(tentativa))
            nj = int(input("Qual seu chute {}?\n".format(nome)))
            print("{} seu chute foi {}".format(nome,nj))
            if nj < 0:
                print("{} você não pode chutar números negativos.".format(nome))
            else:
                if nj == N:
                    arq = open("rank.txt","r")
                    x = arq.readlines()
                    arq.close()
                    pontmaior=(int(x[0]))
                    if pontmaior >= pontus:
                        print("Sua pontuação foi {} ficando abaixo do recorde atual que é de {} pontos".format(pontus,pontmaior))
                    else:
                        print("Parabéns {} Você acertou em {} tentativas\n"
                              "Você é o novo recordista de pontos com {} pontos".format(nome,tentativa,pontus))
                        arq = open("rank.txt","w")
                        arq.write(str(pontus))
                    arq.close()
                    valendo = False
                    op=2
                elif nj < N:
                    pontus-=erro
                    tentativa+=1
                    print("{} você errou!, seu chute foi Menor que o número secreto".format(nome))
                elif nj > N:
                    pontus-=erro
                    tentativa+=1
                    print("{} você errou!, seu chute foi Maior que o número secreto".format(nome))
        else:
            print("Você perdeu! Tente novamente!")
            valendo = False
        
                
def nivel():
    erro=numt=op=0
    go=True
    while go:
        print("Qual o nível de dificuldade?\n"
                "(1) Fácil (2) Médio (3) Difícil\n")
        op=int(input("Informe o nível\n"))
        if op < 1 or op > 3:
            print("numero invalido, informe novamente:")
        else:
            go=False
    nome=input("Qual seu nome?\n")
    if op == 1:
        numt=10
        erro = 10
        jogo(nome,numt, erro)
    elif op == 2:
        numt=5
        erro = 20
        jogo(nome,numt, erro)
    elif op == 3:
        numt=4
        erro = 25
        jogo(nome,numt, erro)
        
nivel()
go=True
while go:
        print("***********************************************************\n"
                "***********************************************************\n"
                "0 - Sair\n"
                "1 - Jogar novamente")
        op=int(input())
        if op == 1:
            nivel()
        else:
            go=False


    

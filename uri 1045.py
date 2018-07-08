valor = input().split()
A = float(valor[0])
B = float(valor[1])
C = float(valor[2])
a=b=c = 0

if(A>B>C)or(A==B>C)or(A==B>C) or(A==B==C):
    a = A
    b = B
    c = C
elif(A>C>B)or(A==C>B)or(A>C==B):
    a = A
    b = C
    c = B
elif(B>A>C)or(B==A>C)or(B>A==C):
    a = B
    b = A
    c = C
elif(B>C>A)or(B==C>A)or(B>C==A):
    a = B
    b = C 
    c = A
elif(C>A>B)or(C==A>B)or(C>A==B):
    a = C
    b = A
    c = B
elif(C>B>A)or(C==B>A)or(C>B==A):
    a = C
    b = B
    c = A
    
if a>=b+c:
    print("NAO FORMA TRIANGULO")
if (a**2) == ((b**2)+(c**2)):
    print("TRIANGULO RETANGULO")
if (a**2) > ((b**2)+(c**2)):
    print("TRIANGULO OBTUSANGULO")
if (a**2) < ((b**2)+(c**2)):
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
if a == b!=c or a == c!=b or b == c!=a:
    print("TRIANGULO ISOSCELES")



    
   

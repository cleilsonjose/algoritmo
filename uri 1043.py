valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
if (B-C)< A and A < (B+C) and (A - C) < B and B < (A + C) and (A - B)< C and C < (A + B):
    Perimetro = A+B+C
    print("Perimetro = %.1f"%Perimetro)
else:
    Area = ((A+ B)*C)/2
    print("Area = %.1f"%Area)

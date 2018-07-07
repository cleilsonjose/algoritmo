valores = input()
lista = valores.split()
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

TRIANGULO = (A * C)/2
CIRCULO = 3.14159 * C**2
TRAPEZIO = ((A+B) * C)/2
QUADRADO = B**2
RETANGULO = A * B
print("TRIANGULO: %1.3f" %TRIANGULO)
print("CIRCULO: %1.3f" %CIRCULO )
print("TRAPEZIO: %1.3f" %TRAPEZIO)
print("QUADRADO: %1.3f" %QUADRADO)
print("RETANGULO: %1.3f" %RETANGULO)

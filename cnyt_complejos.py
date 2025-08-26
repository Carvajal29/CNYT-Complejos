import math  

# ((a,b),(a,b)) 
def suma(a, b):        
    return (a[0]+b[0], a[1]+b[1])  

def resta(a, b):     
    return (a[0]-b[0], a[1]-b[1])  

def producto(a, b):     
    real = a[0]*b[0] - a[1]*b[1]     
    imaginario = a[0]*b[1] + a[1]*b[0]     
    return (real, imaginario)  

def division(a, b):     
    denominador = b[0]**2 + b[1]**2     
    if denominador == 0:         
        raise ZeroDivisionError("División entre cero en números complejos.")     
    real = (a[0]*b[0] + a[1]*b[1]) / denominador     
    imaginario = (a[1]*b[0] - a[0]*b[1]) / denominador     
    return (real,imaginario)  

# ((a,b)) 
def modulo(vector):     
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)  

def conjugado(c):     
    return (c[0], -c[1])  

def fase(c):     
    return math.atan2(c[1], c[0])  

# Conversio de coordenadas
def polares(c):     
    r = modulo(c)     
    angulo = fase(c)     
    return (r, angulo)  

def cartesianas(p):     
    real = p[0]*math.cos(p[1])     
    imag = p[0]*math.sin(p[1])     
    return (real, imag)  

def main():     
    print("Hola")     
    print("Digita 1 si la tupla está en coordenadas cartesianas")     
    print("Digita 2 si la tupla está en coordenadas polares")     
    print("Digita 0 para salir")     

    opcion = int(input("Opción: "))     

    while opcion != 0:         
        if opcion == 1:   # coordenadas cartesianas             
            print("1 : suma")             
            print("2 : resta")             
            print("3 : producto")             
            print("4 : division")             
            print("5 : modulo")             
            print("6 : conjugado")                         
            print("7 : convertir a polares")             

            op = int(input("Elige una operación: "))             

            if op in [1,2,3,4]:                 
                a = tuple(map(float, input("Ingrese el primer número (a b): ").split()))                 
                b = tuple(map(float, input("Ingrese el segundo número (a b): ").split()))                 
                if op == 1: print("Resultado:", suma(a,b))                 
                elif op == 2: print("Resultado:", resta(a,b))                 
                elif op == 3: print("Resultado:", producto(a,b))                 
                elif op == 4: print("Resultado:", division(a,b))             

            else:                 
                a = tuple(map(float, input("Ingrese el número (a b): ").split()))                 
                if op == 5: print("Módulo:", modulo(a))                 
                elif op == 6: print("Conjugado:", conjugado(a))                 
                elif op == 7: print("Fase (radianes):", fase(a))                 
                elif op == 8: print("Forma polar:", polares(a))             

        elif opcion == 2:   # coordenadas polares           
            r, angulo = map(float, input("Ingrese el número (r θ): ").split())             
            print("En forma cartesiana:", cartesianas((r, angulo)))             

        else:             
            print("Opción no válida.")                  
        print("Digita 1 si tu tupla está en coordenadas cartesianas")         
        print("Digita 2 si tu tupla está en coordenadas polares")         
        print("Digita 0 para salir")         
        opcion = int(input("Opción:"))     

    print("chao")  

main()


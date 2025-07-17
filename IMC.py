print("Bienvenido al Sistema de evaluación de IMC")
while True:
    edad = input("Ingrese su edad (2-110 años): ")
        edad = int(edad)
        if 2 <= edad <= 110:
            break
    print("¡Error! Ingrese solo números entre 2 y 110")
while True:
    peso = input("Ingrese su peso: ")
        peso = float(peso)
        if 10 <= peso <= 300:
            break
    print("¡Error! Ingrese un peso válido")
while True:
    altura = input("Ingrese su altura en metros: ")
        altura = float(altura)
        if 0.5 <= altura <= 2.5:
            break
    print("¡Error! Ingrese una altura válida")







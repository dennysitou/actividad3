print("Bienvenido al Sistema de evaluación de IMC")
while True:
    edad = input("Ingrese su edad en años: ")
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

imc = peso / (altura * altura)
print(f"Su IMC es: {imc}")

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Peso saludable")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")









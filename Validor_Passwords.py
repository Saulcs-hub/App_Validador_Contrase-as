# Evaluar passwords seguras
from unittest import result


def evaluar_passwords(password):
    #Contador para el puntaje
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_digitos = False
    tiene_simbolo = False


    if len(password) < 8:
        return "La contrasena debe contener minimo 8 caracteres"

    for i in password:
        if i.isupper():
            tiene_mayusculas = True
        elif i.isdigit():
            tiene_digitos = True
        elif not i.isalpha():
            tiene_simbolo = True
        elif i.islower():
            tiene_minusculas = True

    contador_total = tiene_mayusculas + tiene_minusculas + tiene_simbolo + tiene_digitos

    if contador_total <= 1:
        return "[+] La contraseña es debil"

    elif contador_total >= 2 and contador_total < 4:
        return "[+] La contraseña es normal"

    else:
        return "[+] La contraseña es muy buena"

# Mostrar menu de opciones
def mostrar_menu():
    print("Ingresa una opcion: ")
    print("1. Evaluar que tan segura es mi contraseña actual")
    print("2. Recomendar una contraseña mejor")
    print("0. Salir")

# Funcion main
def main():
    print("**** 💻 Bienvenido a el programa de validacion de contraseñas y de generador de contraseñas seguras  ****")
    print("Este programa esta hecho para validar tus contraseñas actuales y brindarte una recomendacion de el nivel\n"
          "actual de tu contraseña con el fin de que no roben facilmente tus credenciales y tengas una mayor proteccion\n"
          "Al navegar por internet.... Todo con fines de desarrollar nuestros conocimientos en ciberseguridad")

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1:
            password = input("Ingresa tu contraseña actual: ")
            resultado = evaluar_passwords(password)
            print(resultado)
        elif opcion == 2:
            pass
        elif opcion == 0:
            print("Salir")
            break

if __name__ == "__main__":
    main()



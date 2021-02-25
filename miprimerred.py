
print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")


nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()


año = int(input("Para preparar tu perfil, dime en que año naciste . "))
edad = 2021-año
print()


estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
estatura_m = float(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )


num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))


print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
print()


mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Que piensas hoy? ")

print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")
                


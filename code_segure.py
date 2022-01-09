import time

banner = """

   __                            _   _             
  /__\ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __  
 /_\| '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ 
//__| | | | (__| |  | |_| | |_) | |_| | (_) | | | |
\__/|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                     |___/|_|                      

"""

print(banner)

#Datos numericos
def num(arg1):
    print("")
    print("El hash de los numero es: ", hash(arg1))
    

print("Ingresa datos numericos: ")
print("")
num(input(int()))
print("")
time.sleep(1)
print("Ingresa los datos numericos en signo negativo: ")
print("")
num(input(int()))
print("")
time.sleep(1)
print("Magia, ¿Verdad?")
print("")
time.sleep(2)
def text(arg1):
    print("")
    print("El hash de la cadena de extos es: ", hash(arg1))
print("Ingresa una cadena de texto: ")
print("")
text(input(str("")))
print("")
time.sleep(1)
print("Cambia un caracter de tu texto: ")
print("")
text(input(str()))
print("")
time.sleep(1)
print('¿Obervaste el cambio de numeros?\nMagia, no?')


import os
import time
from equipo import Equipo
from menu import Menu

if __name__ == "__main__":
  ejecutar = True
  
  os.system("cls")
  print("Bienvenido al Sistema de E-Sports con python!")
  time.sleep(2)
  
  while ejecutar:
    os.system("cls")
    Menu().principal()
    opcion = input()

    match opcion:
        case "1":
            os.system("cls")
            Menu().equipos()
        case "2":
            os.system("cls")
            Menu().jugadores()
        case "0":
            os.system("cls")
            print("¡Hasta pronto!")
            ejecutar = False
        case _:
            "Opcion invalida."
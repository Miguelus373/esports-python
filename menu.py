import os
from equipo import Equipo
from jugador import Jugador

class Menu:
  def principal(self):
    print("-------------------------")
    print("¿Que desea hacer?")
    print("-------------------------")
    print("1. Opciones de Equipos")
    print("-------------------------")
    print("2. Opciones de Jugadores")
    print("-------------------------")
    print("0. Salir")
    print("-------------------------")

  def opciones(self, registro, registros):
    print("-------------------------")
    print(f"Opciones de {registros}")
    print("-------------------------")
    print(f"1. Listar {registros}")
    print("-------------------------")
    print(f"2. Agregar {registro}")
    print("-------------------------")
    print(f"3. Editar {registro}")
    print("-------------------------")
    print(f"4. Eliminar {registro}")
    print("-------------------------")
    print("0. Volver")
    print("-------------------------")

  def equipos(self):
    volver = False
    
    while volver == False:
      self.opciones("equipo", "equipos")
      opcion = input()
        
      match opcion:
        case "1":
          os.system("cls")
          Equipo().listado()
        case "2":
          os.system("cls")
          Equipo().agregar()
        case "3":
          os.system("cls")
          Equipo().editar()
        case "4":
          os.system("cls")
          Equipo().eliminar()
        case "0":
          volver = True
          os.system("cls")
        case _:
          "Opcion invalida."

  def jugadores(self):
    volver = False
    
    while volver == False:
      self.opciones("jugador", "jugadores")
      opcion = input()

      match opcion:
        case "1":
          os.system("cls")
          Jugador().listado()
        case "2":
          os.system("cls")
          Jugador().agregar()
        case "3":
          os.system("cls")
          Jugador().editar()
        case "4":
          os.system("cls")
          Jugador().eliminar()
        case "0":
          volver = True
          os.system("cls")
        case _:
          "Opcion invalida."
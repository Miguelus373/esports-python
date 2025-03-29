import psycopg
from conexion_bd import conectar

class Jugador:
  def listado(self):
    conexion = conectar() # Establece la conexión a la base de datos

    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("SELECT j.id, j.nombre, nickname, rol, e.nombre FROM jugador j JOIN equipo e ON j.equipo_id = e.id ORDER BY e.nombre, j.id ASC") # Ejecuta una consulta para obtener todos los registros
          registros = cursor.fetchall() # Recupera todos los registros de la consulta
        print("ID | Nombre | Nickname | Rol | Equipo")
        for jugador in registros:
          print(f"{jugador[0]}. | {jugador[1]} | {jugador[2]} | {jugador[3]} | {jugador[4]}") # Imprime cada jugador
      except psycopg.Error as e:
        print(f"Error al leer registros: {e}") # Muestra un mensaje de error si la lectura falla
      finally:
        conexion.close() # Cierra la conexión a la base de datos

  def bd_buscar(self, id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute(f"SELECT EXISTS(SELECT 1 FROM jugador WHERE id = {id})") # Busca un jugador si existe con ID
          exists = cursor.fetchone()[0]
          return exists
      except psycopg.Error as e:
        print(f"Error al buscar jugador: {e}") # Muestra un mensaje de error si la busqueda falla
      finally:
        conexion.close()
    
  # Función para crear un nuevo jugador en la base de datos
  def bd_crear(self, nombre, nickname, rol, equipo_id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("INSERT INTO jugador (nombre, nickname, rol, equipo_id) VALUES (%s, %s, %s, %s)",
          (nombre, nickname, rol, equipo_id)) # Inserta los datos proporcionados en la tabla equipos
        conexion.commit() # Confirma la transacción para guardar los cambios
        print("Jugador creado exitosamente") # Imprime un mensaje si el jugador fue creado exitosamente
      except psycopg.Error as e:
        print(f"Error al crear jugador: {e}") # Muestra un mensaje de error si la inserción falla
      finally:
        conexion.close()

  # Función para borrar un jugador de la base de datos
  def bd_eliminar(self, id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("DELETE FROM jugador WHERE id = %s", (id,)) # Borra el jugador especificado por la ID
        conexion.commit() # Confirma la transacción para guardar los cambios
        print("Registro borrado exitosamente") # Imprime un mensaje si el jugador fue borrado exitosamente
      except psycopg.Error as e:
        print(f"Error al borrar jugador: {e}") # Muestra un mensaje de error si el borrado falla
      finally:
        conexion.close() # Cierra la conexión a la base de datos

  # Función para actualizar un jugador en la base de datos
  def bd_actualizar(self, nickname, id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("UPDATE jugador SET nickname = %s WHERE id = %s",
        (nickname, id)) # Actualiza los datos del jugador especificado
        conexion.commit() # Confirma la transacción para guardar los cambios
        print("Jugador actualizado exitosamente") # Imprime un mensaje si el jugador fue actualizado exitosamente
      except psycopg.Error as e:
        print(f"Error al actualizar jugador: {e}") # Muestra un mensaje de error si la actualización falla
      finally:
        conexion.close() # Cierra la conexión a la base de datos
  
  # Función para pedir los datos de jugador al usuario
  def agregar(self):
    print("Nombre del jugador:")
    nombre = input()
    print("Nickname del jugador:")
    nickname = input()
    print("Rol del jugador:")
    rol = input()
    print("ID del equipo del jugador:")
    equipo_id = input()
  
    # Guardar jugador en BD
    self.bd_crear(nombre, nickname, rol, equipo_id)

  def eliminar(self):
    print("Ingrese el ID del jugador que desea eliminar")
    id = input()
    existe = self.bd_buscar(id)

    # Eliminar jugador de BD
    if existe:
      self.bd_eliminar(id)
    else:
      print(f"No existe un jugador con la id: {id}")
  
  def editar(self):
    print("Ingrese el ID del jugador que desea Editar")
    id = input()
    existe = self.bd_buscar(id)
  
    # Actualizar jugador en BD
    if existe:
      print(f"Nuevo nickname del jugador")
      nickname = input()
      self.bd_actualizar(nickname, id)
    else:
      print(f"No existe un jugador con la id: {id}")
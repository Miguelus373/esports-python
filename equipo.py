import psycopg
from conexion_bd import conectar

class Equipo:
  def listado(self):
    conexion = conectar() # Establece la conexión a la base de datos

    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("SELECT id, nombre, entrenador, pais FROM equipo ORDER BY id ASC") # Ejecuta una consulta para obtener todos los registros
          registros = cursor.fetchall() # Recupera todos los registros de la consulta
        print("ID | Nombre | Entrenador | Pais")
        for equipo in registros:
          print(f"{equipo[0]}. | {equipo[1]} | {equipo[2]} | {equipo[3]}") # Imprime cada equipo
      except psycopg.Error as e:
        print(f"Error al leer registros: {e}") # Muestra un mensaje de error si la lectura falla
      finally:
        conexion.close() # Cierra la conexión a la base de datos

  def bd_buscar(self, id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute(f"SELECT EXISTS(SELECT 1 FROM equipo WHERE id = {id})") # Busca un equipo si existe con ID
          exists = cursor.fetchone()[0]
          return exists
      except psycopg.Error as e:
        print(f"Error al buscar equipo: {e}") # Muestra un mensaje de error si la busqueda falla
      finally:
        conexion.close()
    
  # Función para crear un nuevo equipo en la base de datos
  def bd_crear(self, nombre, entrenador, pais):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("INSERT INTO equipo (nombre, entrenador, pais) VALUES (%s, %s, %s)",
          (nombre, entrenador, pais)) # Inserta los datos proporcionados en la tabla equipos
        conexion.commit() # Confirma la transacción para guardar los cambios
        print("Equipo creado exitosamente") # Imprime un mensaje si el equipo fue creado exitosamente
      except psycopg.Error as e:
        print(f"Error al crear equipo: {e}") # Muestra un mensaje de error si la inserción falla
      finally:
        conexion.close()

  # Función para borrar un equipo de la base de datos
  def bd_eliminar(self, id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("DELETE FROM equipo WHERE id = %s", (id,)) # Borra el equipo especificado por la ID
        conexion.commit() # Confirma la transacción para guardar los cambios
        print("Registro borrado exitosamente") # Imprime un mensaje si el equipo fue borrado exitosamente
      except psycopg.Error as e:
        print(f"Error al borrar equipo: {e}") # Muestra un mensaje de error si el borrado falla
      finally:
        conexion.close() # Cierra la conexión a la base de datos

  # Función para actualizar un equipo en la base de datos
  def bd_actualizar(self, nombre, id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
      try:
        with conexion.cursor() as cursor:
          cursor.execute("UPDATE equipo SET nombre = %s WHERE id = %s",
        (nombre, id)) # Actualiza los datos del equipo especificado
        conexion.commit() # Confirma la transacción para guardar los cambios
        print("Equipo actualizado exitosamente") # Imprime un mensaje si el equipo fue actualizado exitosamente
      except psycopg.Error as e:
        print(f"Error al actualizar equipo: {e}") # Muestra un mensaje de error si la actualización falla
      finally:
        conexion.close() # Cierra la conexión a la base de datos
  
  # Función para pedir los datos de equipo al usuario
  def agregar(self):
    print("Nombre del equipo:")
    nombre = input()
    print("Entrenador del equipo:")
    entrenador = input()
    print("Pais del equipo:")
    pais = input()
  
    # Guardar equipo en BD
    self.bd_crear(nombre, entrenador, pais)  

  def eliminar(self):
    print("Ingrese el ID del equipo que desea eliminar")
    id = input()
    existe = self.bd_buscar(id)
  
    # Eliminar equipo de BD
    if existe:
      self.bd_eliminar(id)
    else:
      print(f"No existe un equipo con la id: {id}")
  
  def editar(self):
    print("Ingrese el ID del equipo que desea Editar")
    id = input()
    existe = self.bd_buscar(id)
  
    # Actualizar equipo en BD
    if existe:
      print(f"Nuevo nombre del equipo")
      nombre = input()
      self.bd_actualizar(nombre, id)
    else:
      print(f"No existe un equipo con la id: {id}")
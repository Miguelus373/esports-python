import psycopg # Importa la biblioteca psycopg para interactuar con PostgreSQL

def conectar():
  try:
    conexion = psycopg.connect( host="localhost", dbname="esports", user="postgres", password="12345678")
    return conexion
  except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
  return None

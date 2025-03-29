# E-Sports Python

## Gestión de Jugadores y Equipos en una Liga de eSports

Esta aplicación de Python permite gestionar una base de datos simple que contiene información sobre jugadores y equipos en una liga de eSports. La aplicación se ejecuta en la consola y ofrece un menú interactivo para facilitar la navegación y la gestión de registros.

### Características

- **Gestión de Jugadores**: Crear, listar, actualizar y eliminar registros de jugadores.
- **Gestión de Equipos**: Crear, listar, actualizar y eliminar registros de equipos.
- **Interfaz de Consola**: Navegación a través de opciones numéricas en un menú interactivo.

### Estructura de la Base de Datos

La base de datos consta de dos tablas principales:

1. **Equipos**:
   - ID (clave primaria)
   - Nombre del equipo
   - Entrenador
   - País

2. **Jugadores**:
   - ID (clave primaria)
   - Nombre
   - Nickname
   - Rol
   - Equipo (clave foránea)

### Instalación

Para ejecutar esta aplicación, asegúrate de tener Python instalado en tu sistema. Luego, sigue estos pasos:

1. Clona el repositorio:

```
  git clone https://github.com/Miguelus373/esports-python.git
```

2. Navega al directorio del proyecto:

```
  cd esports-python
```

3. Instala psycopg:

```
  pip install psycopg
```

### Uso

Para iniciar la aplicación, ejecuta el siguiente comando en la consola:

```
py esports.py
```

Una vez que la aplicación esté en funcionamiento, verás un menú principal con las siguientes opciones:

1. Opciones de Equipos
2. Opciones de Jugadores
3. Salir

Selecciona una opción ingresando el número correspondiente y sigue las instrucciones en pantalla para realizar las operaciones deseadas.

---

¡Esperamos que disfrutes utilizando esta aplicación para gestionar tu liga de eSports! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.
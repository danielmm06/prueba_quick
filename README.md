# Expliacion paso a paso para ejecución del proyecto

- Acceder al repositorio y clonar el repositorio
  - **$git clone https://github.com/danielmm06/prueba_quick.git**
  - **$cd prueba_quick**

- Crear el entorno virtual para instalar las diferentes librerias que se usaron en el proyecto
  - **$python3 -m venv venv**

- Ingresar al envoltorio y activarlo 
  - **$source venv/bin/activate**

- Una vez activado instalar las dependencias
  - **(env)$ pip install -r requirements.txt**

- Ejecutar el proyecto
  - **$python3 manage.py runserver**
  
# CONFIGURACION Y ESQUEMA DE BASES DE DATOS

Para el desarrollo de este proyecto se uso la base de datos ***SQLITE3*** por prácticidad:
```
      DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
           }
       }
 ```

Si se desea usar otra base de datos se debe configurar el archivo ***settings***, en el apartado ***DATABASES*** y colocar base de datos de preferencia. 

A continuacion un ejemplo de configuracion de una Base de datos de postgresql:
```
    DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'test',
              'USER':'postgres',
              'PASSWORD':'ROOT',
              'HOST':'localhost',
              'PORT':'5432'
          }
      }
 ```

Despues de tener creada la base de datos, se procederá a realizar las ***migraciones***. 
  - **$python manage.py makemigrations api** (En caso de hacer modificaciones a los modelos, siempre se debe hacer antes del migrate)
  - **$python manage.py migrate** 


# ENDPOINTS 

- Endpoints CRUD 
  - listar o crear clientes
    - http://localhost:8000/client/
  
  - Actualizar o eliminar un cliente a través del ID
    - http://localhost:8000/client/ud/ID

  - listar y crear productos)
    - http://localhost:8000/products/ 
  
  - Actualizar o eliminar un producto a través del ID
    - http://localhost:8000/products/ud/ID 

  - listar y crear de facturas
    - http://localhost:8000/bills/
  
  - Actualizar y eliminar una factura a través del ID
    - http://localhost:8000/bills/ud/ID
  
  - Listar facturas_productos
    - http://localhost:8000/bills/products/


- Endpoint para registar un usuario:
  - http://localhost:8000/api/create_user/1.0/ 

  Recibe un archivo Json mediante un POST de la forma:
  ```
  {
      "username": "prueba_quick",
      "first_name" "Prueba",
      "last_name": "quick",
      "email": "prueba_quick@pruebas.com",
      "password": "pruebas123"
  }
  ```

- Endpoint para iniciar sesión y generar token 
  - http://localhost:8000/login/ 

  - En base de datos se encuentra un usuario de prueba con:
    ```
    username = daniel
    password = daniel_123
    ``` 

- Para tener acceso al token de aseguramiento de los endpoints
  - http://localhost:8000/api_generate_token/ Se puede tener acceso a este mediante las credenciales de prueba anteriormente mencionadas.


- Enpoint para generar CSV con los registros de los clientes
  - http://localhost:8000/excel/
    - Mediante el método GET de esta url automáticamente se creara un reporte en csv de los clientes creados, este archivo se guardará en la carpeta   static/excel.
    - Mediante la misma url pero con el método POST y enviando en el body los datos key-value como se muestra a continuación:
  ```
    key: files
    value: archivo.csv() 
  ```
Al enviar el POST se guardará una copia del documento en la carpeta ***static/excel*** y se cargarán los registros en la tabla de Clientes. 

**NOTA**: en el proyecto hay dos archivos:

  - ***archivoPruebaCargue.csv*** con algunos datos de prueba para ser cargados.
  - ***test quick.postman_collection.json*** donde exporte la coleccion de pruebas realizadas en postman.

***Desarrollado por Luis Daniel Malaver Mendoza***

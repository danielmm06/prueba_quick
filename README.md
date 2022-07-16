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

- En este proyecto se usa ***SQLITE3*** como base de datos para más prácticidad, pero si se desea usar otra base de datos se debe configurar el archivo ***settings***, en el apartado ***DATABASES*** y colocar base de datos de preferencia. Una vez hecho esto y creada la base de datos, se procederá a realizar las ***migraciones***. 
  - **$python manage.py makemigrations api** (En caso de hacer modificaciones a los modelos, siempre se debe hacer antes del migrate)
  - **$python manage.py migrate** 


# ENDPOINTS 

- Endpoints CRUD 
  - http://localhost:8000/client/ (Listado y creación de clientes)
  - http://localhost:8000/clientud/<pk> (Actualizar y eliminar un cliente a través del id)

  - http://localhost:8000/products/ (Listado y creación de productos)
  - http://localhost:8000/products/ud/<pk> (Actualizar y eliminar un producto a través del id)

  - http://localhost:8000/bills/ (Listado y creación de facturas)
  - http://localhost:8000/bills/ud/<pk> (Actualizar y eliminar una factura a través del id)

  - http://localhost:8000/bills/products/ (Lista facturas-productos)


- Endpoint para registar un usuario con los siguientes datos: username, firstname, lastname, correo
  - http://localhost:8000/api/create_user/1.0/ 

  Recibe un archivo Json mediante un POST de la forma:
  ```
  {
      "username": " ",
      "firstname" " ",
      "lastname": " ",
      "correo": " "
  }
  ```

- Endpoint para iniciar sesión y generar token 
  - http://localhost:8000/login/ 

  - Se ingresa el usuario creado anteriormente, en base de datos se encuentra un usuario de prueba con:
    ```
    username = daniel
    password = daniel_123
    ``` 
  Este endpoint cuenta con un template HTML que se puede visualizar desde el navegador. 

- Para tener acceso al token de aseguramiento de los endpoints
  - http://localhost:8000/api_generate_token/
  Podemos tener acceso a este mediante las credenciales de prueba anteriormente mencionadas.


- Enpoint para generar CSV con los registros de los clientes
  - http://localhost:8000/excel/
  Mediante el método GET de esta url automáticamente se creara un reporte en csv de los clientes creados, este archivo se guardará en la carpeta      static/excel.



- Endpoint para realizar un cargue de un archivo CSV para creación de clientes
  - http://localhost:8000/excel/
  Mediante la misma url pero con el método POST y enviando en el body los datos key-value lo siguiente:
  key: files, value: archivo.csv() 

A través de postman se puede realizar una prueba sencilla, se realiza un POST a la url http://localhost:8000/excel/ en el body se establece que se enviará en form-data y en el valor key se define como un archivo (file) lo que permitirá cargar un archivo a través de un input file. Al hacer el POST se guardará una copia del documento en la carpeta static/excel y se cargarán los registros en la tabla Clientes. 

**NOTA**: en el proyecto hay un archivo llamado archivoPruebaCargue.csv con algunos datos de prueba para ser cargados. 


***Desarrollado por Luis Daniel Malaver Mendoza***

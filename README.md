# ProyectoFrander
Sistema de recomendaciones de productos de ropa, implementando un modelo de IA basado en logica difusa, permitiendo sugerir productos a base de las preferencias del usuario

# Instalacion del Proyecto

## Requisitos
* Python en su version 3.11.*
* Git en su ultima version

## Pasos de la Instalacion
1. Clona el repositorio del proyecto en tu maquina local
2. Abre una terminal CMD en la carpeta del proyecto y ejecuta los siguientes comandos:
    1. Descarga el paquete *VIRTUALENV* de python. Saltar si ya se tiene instalado el paquete.
    ```
        pip install virtualenv
    ```
    2. Crea el entorno virtual
    ```
        py -m venv venv
    ```
    3. Activa el entorno virtual
    ```
        venv\Scripts\activate
    ```
3. Luego de habilitar el entorno, instala todas las dependencias del proyecto desde el archivo *REQUIREMENTS.TXT*.
```
    pip install -r requirements.txt
```
4. Ejecuta las migraciones del proyecto.
```
    py manage.py migrate
```
5. Crear un superusuario para administrar el sistema. Colocas el nombre de usuario y contraseña que mas te convenga.
```
    py manage.py createsuperuser
```
6. Ejecuta el servidor del proyecto
```
    py manage.py runserver
```

Luego de que ejecutemos el servidor, vamos a la ruta de 127.0.0.1:8000/admin para acceder al modulo de administracion de datos 



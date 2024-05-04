# Proyecto_Final
# Entrega Final
### alumno: nlugo90@gmail.com

# Comandos

1. Crear proyecto Django
    ```bash
    django-admin startproject <nombre del proyecto>
    ```
    Si el comando anterior falla, se puede utilizar:

    ```bash
    python -m django startproject nombre_del_proyecto
    # o
    python3 -m django startproject nombre_del_proyecto
    ```
2. Testear servidor
    ```bash
    python manage.py runserver
    ```
3. Crear una `application` dentro de mi proyecto:
    ```bash
    python manage.py startapp <nombre de la aplicacion>
    ```
    en este caso sería `gear`:
    ```bash
    python manage.py startapp gear
    ```
4. Creamos un archivo que se llame `urls.py` en `<nombre_del_proyecto>/<nombre_de_su_aplicacion>/urls.py`.


## Templates

1. Los templates son archivos con extensión `.html` que se deben guardar dentro de una carpeta llamada `templates` dentro de la carpeta de cada aplicación.

2. Para utilizarlo en alguna vista se recomienda utilizar la función `render`.

## Modelos

Después de agregar o modificar un modelo en `models.py` tenemos que correr 2 comandos:

1. `python manage.py makemigrations`
2. `python manage.py migrate`

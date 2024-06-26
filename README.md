# Proyecto_Final
# Entrega Final
### alumno: nlugo90@gmail.com

# Descripcion
1. Es una pagina web en la cual el administrador va a poder crear vuelos, visulaizarlos, buscarlo y modificarlos segun lo necesite.
Tambien hay opciones para los usuarios en donde van a poder crear, visualizar y buscar sus reservas.

2. Les dejamos el siguiente link para ver el tutorial de como se utiliza la pagina: [click_para-ver_el_video](https://youtu.be/bENwK7E1EYg)

3. Login
user: invitados password: visita123

# Acerca de mi
- ¡Hola! Mi nombre es Nicolas Lugo y soy el desarrollador principal detrás de este proyecto de Django para la aplicación de vuelos GoGo. 
Soy un apasionado de la programación y me encanta crear soluciones que faciliten la vida de las personas.
Durante el desarrollo de este proyecto, me esforcé por crear una aplicación fácil de usar que permita a los usuarios gestionar vuelos y reservas de manera eficiente. 
Me inspiré en mi propia experiencia como viajero y en las necesidades que he identificado en el mundo de la gestión de viajes.
Soy un entusiasta de Python y Django, y he utilizado mis habilidades en estas tecnologías para construir esta aplicación desde cero. 
Me dediqué a asegurarme de que cada aspecto del proyecto esté cuidadosamente diseñado y probado para garantizar su funcionamiento óptimo.

# Comandos utilizados

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

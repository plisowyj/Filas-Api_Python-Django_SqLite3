# Gestion turnos
## Descripcion
 Aplicacion web echa para el fin de gestionar los turnos de un consultorio medico, bancario, financiero, etc. Brinda distintas herramientas desde la llegada del cliente para su atencion de forma mas optimizada en tiempo real.

## Pasos a seguir para ejecutar en tu pc la aplicacion
1. Desde github copiamos la url de nuestra aplicacion y abrimos en nuestro Visual Studio Code nuestra terminal Git Bash.
2. Clonaremos el repositorio desde github con el comando: git clone "aqui pegar el repositorio".
3. Luego ejecutaremos el comando: py manage.py makemigrations y despues de este el comando: py manage.py migrate
4. Por ultimo para correr el programa en nuestro servidor utilizaremos py manage.py runserver y ahi nos va a aparecer la url de acceso.
5. Copiamos la url y la pegamos en nuestro navegador web para poder empezar a utilizar la aplicacion.

## Casos de pruebas de Drive:

- Hacer click en este link para ver donde fueron probadas las pruebas de Gestion Turnos : https://docs.google.com/spreadsheets/d/18ER2DcmczqclOWvHrD2DImVaBQAJqqfJ770imvrPwPM/edit?usp=sharing 

## Aqui dejamos un video subido desde YouTube de como utilizar la aplicacion y que nos permite hacer cada accion que hagamos en ella.
- URL: https://www.youtube.com/watch?v=_OFgaKYD5Zc&ab_channel=TomyGhi

## URL's de Acceso a cada modulo:
- touch => http://127.0.0.1:8000/touch/
- gestion fila => http://127.0.0.1:8000/
- tv => http://127.0.0.1:8000/caller/
- Nota: en las URL, '8000' es el puerto donde se levanta el server al correr la aplicacion.


## Circuito de uso entre los 3 módulos del proyecto:
![](/static/img/Prj_Coder_Final.png)

## Como utlilizar nuestra Seleccion de tramite:
![](/static/img/tramites_gestionturnos.png)

- Seleccionamos el tramite que deseamos realizar clickeando el boton "Tomar Turno" con el que vamos a ser atendidos.

## Para que sirve nuestra pantalla de Anucios:
![](/static/img/caller_gestionturnos.png)

- Esta pantalla nos indicara la posicion y el lugar a donde sera atendido el Cliente/Paciente.

## Como crear un usuario en Gestion Turnos:
![](/static/img/creacion_usuario.png)

- Seleccionamos arriba a la derecha ingresar y nos aparecera dos opciones, seleccionamos la de Registro de usuario y completaremos los siguientes campos:

![](/static/img/registro_Usuario.png)

## Como iniciar sesion en Gestion Turnos:
![](/static/img/creacion_usuario.png)

- Seleccionamos arriba a la derecha ingresar y nos aparecera dos opciones, seleccionamos la de Iniciar Sesion, ingresaremos nuestro usuario y su contraseña.

![](/static/img/Iniciar.Sesion.png)

## Seccion Acerca de:
![](/static/img/acerca.png)

- Nos habla sobre como esta compuesto el grupo de programadores que han creado este sitio.

## Para que sirven cada boton que tenemos en Atencion-Recepcion:
![](/static/img/listado_ingresos.png)

- El boton amarillo nos permite Revivir la atencion y enviarla devuelta por pantalla.
- El boton Gris nos vuelve a anunciar por pantalla el turno con sus datos.
- El boton rojo Cancela la Atencion.
- El boton verde nos brinda el Detalle del ingreso del cliente.
- El boton celeste permite modificar si el cliente ingreso mal su documento.

## Para que sirven cada boton que tenemos en Atencion-Lugares:
![](/static/img/listado_lugares.png)

- El boton rojo Cancela la atencion.
- El boton verde nos brinda el Detalle del turno.
- el boton amarillo nos deja Revivir Atencion del turno si es que tocamos el boton rojo de cancelar la atencion.

## Para que sirven cada boton que tenemos en Atencion-Anuncios:
![](/static/img/listado_turnos_anunciados.png)

- Tendremos listado en donde encontraremos el turno, recepcion y fecha de anuncio de los "Anunciados".
- El boton rojo es para borrar el anuncio del listado. 

## Para que sirven cada boton que tenemos en Configuraciones-Usuarios:
![](/static/img/configuraciones_Usuarios.png)

- El boton amarillo nos permite ver los detalles del usuario como por ejemplo: el nombre que eligio, nombre de usuario y el email.
- El boton celeste nos permite modifar los datos ingresados del usuario.
- El boton rojo nos permite borrar el usuario del listado.

## Para que sirven cada boton que tenemos en Configuraciones-Tramites:
![](/static/img/Configuraciones_Tramites.png)

- El boton azul nos permite agregar un nuevo tramite en donde nos pedira la descripcion, si esta activo, el decorador y lugar del puesto donde sera posicionado.
- El boton amarillo nos permitira ver el detalle del usuario.
- El boton celeste nos permite modifar los datos ingresados del Tramite.
- El boton rojo nos permite borrar el Tramite del listado.

## Para que sirven cada boton que tenemos en Configuraciones-Clientes:
![](/static/img/configuraciones_Clientes.png)

- El boton azul nos permite agregar un nuevo Cliente en donde ingresaremos los datos de: Apellido, Nombres, Nº Documento, Fecha de Nacimiento y una imagen del usuario.
- El boton amarillo nos permitira ver el detalle del usuario.
- El boton celeste nos permite modifar los datos ingresados del Tramite.
- El boton rojo nos permite borrar el Tramite del listado.

## Para que sirve nuestro Configuraciones-Contadores:
![](/static/img/configuraciones_Contadores.png)

- Nos permite ver que usuarios entraron en orden y si siguen activos para atenderlos.
- El boton rojo reinicia los contadores en 0

![caperucita hacker 756](caperucitaRoja756.jpg)

----
###### Por Natalia cortés Bernal ➡ alias caperucita hacker 756. 
----

# Conexión con servidor web
En esta practica, se realiza un pequeño script de python cuya finalidad es conectarse a un servidor web y obtener de él el archivo que contiene los logs de dicho servidor


#### Proceso de creación del script
Para empezar estaré usando la libreria de paramiko [^1] y webbrowser [^2]

###### Requerimientos para la ejecución del programa
- En primer lugar tener instaladas las librerias paramiko, webbrowser no es necesaria ya que viene incluida con el propio python.
- A continuación, a modo de información la versión de python es Python 3.10.11 (en caso de que diera algún problema).
- Por último arrancar el programa, que puede hacerse desde la propia terminar no es necesario ejecutar desde ningún ide.

[^1]: Esta libreria se encargará de obtener el fichero access.log
del servidor.
[^2]: Esta libreria se encargará de una vez obtenido el archivo correspondiente abrir la web para visualizar dichos datos.
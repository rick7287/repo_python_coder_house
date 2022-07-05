#Ejemplo de un paquete distribuible

#De un modulo propi de Python, voy a importar la funcion setup
from setuptools import setup

setup(
    name='mipaquete',
    version='1.0',
    description='mi primer paquete redis',
    author='Franco',
    packages=['paquete'],

)


#Al ejecutar python setup.py sdist, me va a crear dos carpetas en el directorio raiz:
#Una llamada "dist" con un archivo comprimido conteniendo mi paquete listo para distribuir .tar.gz
#La otra con "name.egg-info", donde name es el nombre que yo le puse al hacer el setup() con info sobre mi paquete


#Como instalo mi paquete?
#Desde la terminal, parado en el directorio donde guarde mi .tar.gz, ejecuto pip name-version.tar.gz
#Y ya puedo import mis modulos o paquetes o funciones
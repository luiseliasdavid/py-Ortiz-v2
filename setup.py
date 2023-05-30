from setuptools import setup

setup(
    name="Mensajes",
    version="1.0",
    description="un paquete para saludar y despedir",
    author="Luis elias david",
    author_email="vsvsevs@gmail.com",
    url="https://www.vdvdfvfv.dev",
    packages=[ 'modulos', 'modulos.mensajes','modulos.mensajes.hola','modulos.mensajes.adios'],
    scripts=['modulos/test.py'],

)
from setuptools import setup

setup(
    name="Mensajes",
    version="3.0",
    description="un paquete para saludar y despedir",
    author="Luis elias david",
    author_email="vsvsevs@gmail.com",
    url="https://www.vdvdfvfv.dev",
    # packages=find_packages()
    install_requirements =[paquete.strip() for paquete in open("requirements.tx").readline()],
    scripts=['modulos/test.py'],

)
import sys
import datetime

"""
mostrar la version de python 
"""
print('version de python', sys.version)

print()

print('informacionn de version', sys.version_info)

print()

""" 
mostrar fecha y hora actuales
"""
now = datetime.datetime.now()
print('la fecha actual es: ',now)
print(now.strftime('%H:%M:%S %Y-%m-%d'))

""" 
mostrar nombre invertido
"""
nombre= input('digite su nombre ')

print('su nombre invertido es', nombre[::-1])
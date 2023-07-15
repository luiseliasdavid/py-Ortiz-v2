import jwt
import datetime

# Clave secreta para firmar y verificar el token (puede ser cualquier valor secreto)
clave_secreta = 'mi_clave_secreta'

# Función para generar un token JWT
def generar_token(datos):
    # Definir fecha de expiración del token (en este caso, 1 hora desde ahora)
    fecha_expiracion = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    # Crear payload (datos) del token
    payload = {
        'datos': datos,
        'exp': fecha_expiracion
    }

    # Generar el token JWT
    token = jwt.encode(payload, clave_secreta, algorithm='HS256')
    return token

# Función para verificar un token JWT
def verificar_token(token):
    try:
        # Decodificar el token y obtener el payload (datos)
        payload = jwt.decode(token, clave_secreta, algorithms=['HS256'])
        return payload['datos']
    except jwt.ExpiredSignatureError:
        return 'El token ha expirado.'
    except jwt.InvalidTokenError:
        return 'Token inválido.'

# Ejemplo de uso
datos_usuario = {
    'id': 123,
    'nombre': 'Usuario Ejemplo',
    'rol': 'admin'
}

# Generar el token
token_generado = generar_token(datos_usuario)
print('Token generado:', token_generado)

# Verificar el token
datos_verificados = verificar_token(token_generado)
print('Datos verificados:', datos_verificados)

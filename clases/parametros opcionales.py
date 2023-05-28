class ClaseBase:
    def __init__(self, parametro_obligatorio, parametro_opcional="valor_predeterminado"):
        self.parametro_obligatorio = parametro_obligatorio
        self.parametro_opcional = parametro_opcional

class ClaseDerivada(ClaseBase):
    def __init__(self, parametro_obligatorio, parametro_opcional="valor_personalizado", otro_parametro=None):
        super().__init__(parametro_obligatorio, parametro_opcional)
        self.otro_parametro = otro_parametro

# Crear una instancia de la clase derivada omitiendo el parámetro opcional pero especificando otro_parametro
objeto = ClaseDerivada("valor_obligatorio", otro_parametro="otro_valor")

print(objeto.parametro_obligatorio)  # Salida: valor_obligatorio
print(objeto.parametro_opcional)  # Salida: valor_personalizado
print(objeto.otro_parametro)  # Salida: otro_valor

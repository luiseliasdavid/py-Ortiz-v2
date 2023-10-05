from urllib.parse import urlencode

# Definir los valores de las etiquetas UTM
utm_source = "facebook"
utm_medium = "social"
utm_campaign = "spring_sale"
utm_content = "ad1"
utm_term = "shoes"

# Crear un diccionario con los valores de las etiquetas
utm_params = {
    'utm_source': utm_source,
    'utm_medium': utm_medium,
    'utm_campaign': utm_campaign,
    'utm_content': utm_content,
    'utm_term': utm_term,
}

# URL base a la que se agregarán las etiquetas UTM
base_url = "https://www.example.com/product-page"

# Agregar las etiquetas UTM a la URL base
url_with_utm = f"{base_url}?{urlencode(utm_params)}"

print("URL con etiquetas UTM:", url_with_utm)

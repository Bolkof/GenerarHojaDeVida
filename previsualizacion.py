import markdown

# Nombre del archivo de entrada (Markdown) y de salida (HTML)
archivo_entrada = 'muestra.md'
archivo_salida = 'muestra.html'

# Abre el archivo de entrada y lee el contenido
with open(archivo_entrada, 'r', encoding='utf-8') as f:
    contenido_markdown = f.read()

# Convierte el contenido Markdown a HTML
contenido_html = markdown.markdown(contenido_markdown)

# Código HTML al principio
html_inicio = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="estilo.css">
  <title>Mi Hoja de Vida</title>
</head>
<body>
"""

# Código HTML al final
html_final = """
</body>
</html>
"""

# Combinar el contenido HTML generado con el código HTML al principio y al final
contenido_html_completo = html_inicio + contenido_html + html_final

# Escribe el contenido HTML completo en el archivo de salida
with open(archivo_salida, 'w', encoding='utf-8') as f:
    f.write(contenido_html_completo)

print(f'Se ha convertido "{archivo_entrada}" a "{archivo_salida}" con éxito.')
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


from weasyprint import HTML, CSS

# Nombre del archivo de entrada (HTML) y de salida (PDF)
archivo_html = 'muestra.html'
archivo_css = 'estilo.css'
archivo_pdf = 'final.pdf'

# Define un estilo CSS para eliminar márgenes
css = CSS(string='@page { margin: 0; }')

# Crea un objeto HTML a partir del archivo HTML y aplica el CSS
html = HTML(filename=archivo_html)
html.write_pdf(archivo_pdf, stylesheets=[css])

print(f'Se ha convertido "{archivo_entrada}" a "{archivo_pdf}" con éxito.')

import markdown

# Nombre del archivo de entrada (Markdown) y de salida (HTML)
archivo_entrada = 'muestra.md'
archivo_salida = 'muestra.html'

# Abre el archivo de entrada y lee el contenido
with open(archivo_entrada, 'r', encoding='utf-8') as f:
    contenido_markdown = f.read()

# Convierte el contenido Markdown a HTML
contenido_html = markdown.markdown(contenido_markdown)

# Escribe el contenido HTML en el archivo de salida
with open(archivo_salida, 'w', encoding='utf-8') as f:
    f.write(contenido_html)

print(f'Se ha convertido "{archivo_entrada}" a "{archivo_salida}" con éxito.')

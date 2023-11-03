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

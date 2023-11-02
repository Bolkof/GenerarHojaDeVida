# GenerarHojaDeVida
Es un generador de hojas de vida desde markdown a pdf


Puedes convertir archivos Markdown simples a un PDF con diseño, utilizsando Python.
Este repositorio utiliza las siguientes biblioteca de tercelos llamadas `markdown` y `weasyprint` Asegúrate de tener estas biblioteca instaladas junto con el repositorio:

```bash
git clone https://github.com/Bolkof/GenerarHojaDeVida.git
```

```bash
cd GenerarHojaDeVida
```

```bash
pip install markdown
```

```bash
pip install weasyprint
```

Edita los siguientes archivos de acuerdo a tu gusto y preferencia `ejemplo_hoja.md ejemplo_estilo.css` y guardalos como `muestra.md estilo.css` en la misma carpeta, luego, puedes usar el siguiente comando Python para tener un resultado previo en HTML y verlo en un navegador.


```bash
python previsualizacion.py
```
 
Al ejecutar el comando anterior se tiene un preliminar del documento el cual se puede ver desde el navegador. Para convertir en markgdon  en un archivo PDF ejecuta el siguiente comando

```bash
python final.py
```

Con el cual generara un archivo pdf llanmado final.pdf
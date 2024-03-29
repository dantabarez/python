import markdown
import pdfkit
import datetime

# Define la información a agregar al PDF en formato Markdown
contenido = f"""
# INDRA

## Acta de OJT Mando y Control

Fecha: {datetime.datetime.now().strftime("%Y-%m-%d")}

Nombre del instructor: Danny Tabarez

Personas en capacitación:

* 
* 
* 

Tareas:

| CODIGO | NOMBRE TAREA |
|--------|--------------|
| 001    | Tarea 1      |
| 002    | Tarea 2      |
| 003    | Tarea 3      |
| 004    | Tarea 4      |


| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Cell 2   | Cell 3   |
| Row 2    | Cell 5   | Cell 6   |
| Row 3    | Cell 8   | Cell 9   |

"""

# Convierte el Markdown a HTML
html = markdown.markdown(contenido)

# Convierte el HTML a un archivo PDF
pdfkit.from_string(html, 'documento2.pdf')

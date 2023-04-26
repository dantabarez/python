from reportlab.pdfgen import canvas
import datetime

# Crea un nuevo documento PDF
pdf = canvas.Canvas("documento.pdf")

# Define la información a agregar al PDF
titulo = "INDRA"
subtitulo = "Acta de OJT Mando y Control"
fecha = datetime.datetime.now().strftime("%Y-%m-%d")
instructor = "Danny Tabarez"
personas_en_capacitacion = [
    ["REYES"],
    ["FREIRE"],
    ["MALDONADO"]

]
tareas = [
    ["CODIGO", "NOMBRE TAREA"],
    ["001", "Tarea 1"],
    ["002", "Tarea 2"],
    ["003", "Tarea 3"],
    ["004", "Tarea 4"]
]

# Agrega el título y subtitulo en el centro de la página
pdf.setFont("Helvetica-Bold", 18)
pdf.drawCentredString(300, 750, titulo)
pdf.setFont("Helvetica", 12)
pdf.drawCentredString(300, 720, subtitulo)

# Agrega la fecha y el nombre del instructor
pdf.drawString(50, 650, "Fecha: " + fecha)
pdf.drawString(50, 630, "Nombre del instructor: " + instructor)

# Agrega la lista de personas en capacitación
pdf.drawString(50, 600, "Personas en capacitación:")
y = 580
for persona in personas_en_capacitacion:
    pdf.drawString(70, y, persona)
    y -= 20

# Agrega la lista de tareas
pdf.drawString(50, 500, "Tareas:")
x = 70
y = 480
for fila in tareas:
    pdf.drawString(x, y, fila[0])
    pdf.drawString(x + 70, y, fila[1])
    y -= 20

# Guarda el documento PDF
pdf.save()

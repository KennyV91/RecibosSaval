from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

w, h = letter
c = canvas.Canvas("Recibo-Saval.pdf", pagesize=letter)
c.drawString(50, h-50, "Saval SRL")



c.save()
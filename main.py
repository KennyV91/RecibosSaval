from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from tkinter import *
canvas = Canvas(width=400, height = 300, bg='white')
canvas.pack(expand=YES, fill=BOTH)


mainloop()

w, h = letter
c = canvas.Canvas("Recibo-Saval.pdf", pagesize=letter)
c.drawString(50, h-50, "Saval SRL")

x = 50
y = h -50
c.line(x, y, x + 200, y)
c.rect(50, h - 300, 300, 200)
c.roundRect(50, h - 300, 300, 200, 10)
c.circle(100, h - 100, 50)
c.ellipse(50, h - 50, x + 150, y - 50)

c.save()
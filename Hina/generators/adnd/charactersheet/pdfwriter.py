from reportlab.pdfgen import canvas

def write(w,fp):
    c=canvas.Canvas(fp)
    c.drawString(100,100,w)
    c.showPage()
    c.save()
    return 0

from reportlab.pdfgen import canvas
from reportlab.pdfgen import inch

    #c.line(x1,y1,x2,y2)


def write(w,fp):
    c=canvas.Canvas(fp)
    c.translate(inch,inch) #moves origin from bottom left to top left
    c.setFont("Helvetica",10)
    
    c.drawString(0,0,"Character")
    c.line(.5*inch,0,4*inch,0)
    c.drawString(1*inch,0)
    
    
    c.showPage() #finishes writing on current page, starts a new page if more is added
    c.save() #finalizes the document
    return 0

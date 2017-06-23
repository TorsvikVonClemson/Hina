from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

    #c.line(x1,y1,x2,y2)


def write(name,fp):


    c=canvas.Canvas(fp)
    c.translate(inch,inch) #moves origin from bottom left to top left
    c.setFont("Helvetica",10)
    
    c.drawString(-.8*inch,10.5*inch,"Character:")
    c.line(-.1*inch,10.4*inch,4*inch,10.4*inch)
    c.drawString(-.1*inch,10.5*inch,name)
    
    
    c.showPage() #finishes writing on current page, starts a new page if more is added
    c.save() #finalizes the document
    return 0

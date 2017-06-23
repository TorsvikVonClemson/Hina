from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

    #c.line(x1,y1,x2,y2)


def write(array,fp):


    c=canvas.Canvas(fp)
    c.translate(inch,inch) #moves origin from bottom left to top left
    c.setFont("Helvetica",10)

#-----Name-----#
    
    c.drawString(-.8*inch,10.5*inch,"Character:")
    c.line(-.1*inch,10.4*inch,3*inch,10.4*inch)
    c.drawString(-.1*inch,10.5*inch,array[0])

#-----Level-----#

    c.drawString(3.5*inch,10.5*inch,"Level:")
    c.line(3.9*inch,10.4*inch,4*inch,10.4*inch)
    array.append("1") #TEMP
    c.drawString(3.9*inch,10.5*inch,array[1])
    
    
    c.showPage() #finishes writing on current page, starts a new page if more is added
    c.save() #finalizes the document
    return 0

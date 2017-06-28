from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

    #c.line(x1,y1,x2,y2)


def write(array,fp):


    c=canvas.Canvas(fp)
    c.translate(inch,inch) #moves origin from bottom left to top left
    c.setFont("Helvetica",10)

#-----------------#
# Begin Section 1 #
#-----------------#

#-------#
# Row 1 #
#-------#

#-----Name-----#
    
    c.drawString(-.8*inch,10.5*inch,"Character:")
    c.line(-.1*inch,10.45*inch,3*inch,10.45*inch)
    c.drawString(-.1*inch,10.5*inch,array[0])

#-----Level-----#

    c.drawString(3.1*inch,10.5*inch,"Level:")
    c.line(3.6*inch,10.45*inch,3.8*inch,10.45*inch)
    c.drawString(3.6*inch,10.5*inch,array[1])

#-----Race-----#

    c.drawString(3.9*inch,10.5*inch,"Race:")
    c.line(4.4*inch,10.45*inch,7*inch,10.45*inch)
    c.drawString(4.4*inch,10.5*inch,array[2])

#-------#
# Row 2 #
#-------#

#-----Class-----#

    c.drawString(-.8*inch,10.25*inch,"Class:")
    c.line(-.3*inch,10.20*inch,.5*inch,10.20*inch)
    c.drawString(-.3*inch,10.25*inch,array[3])

#-----Alignment-----#

    c.drawString(.6*inch,10.25*inch,"Alignment:")
    c.line(1.3*inch,10.20*inch,1.5*inch,10.20*inch)
    c.drawString(1.3*inch,10.25*inch,array[4])

#-----Religion-----#

    c.drawString(1.6*inch,10.25*inch,"Religion:")
    c.line(2.2*inch,10.20*inch,3*inch,10.20*inch)
    c.drawString(2.2*inch,10.25*inch,array[5])

#-----Homeland-----#

    c.drawString(3.1*inch,10.25*inch,"Homeland:")
    c.line(3.8*inch,10.20*inch,5.4*inch,10.20*inch)
    c.drawString(3.8*inch,10.25*inch,array[6])

#-----Gender-----#

    c.drawString(5.5*inch,10.25*inch,"Gender:")
    c.line(6*inch,10.20*inch,7*inch,10.20*inch)
    c.drawString(6*inch,10.25*inch,array[7])

#-------#
# Row 3 #
#-------#


#-----Age-----#

    c.drawString(-.8*inch,10*inch,"Age:")
    c.line(-.3*inch,9.95*inch,0*inch,9.95*inch)
    c.drawString(-.3*inch,10*inch,array[8])

#-----Height-----#

    c.drawString(0*inch,10*inch,"Height:")
    c.line(.5*inch,9.95*inch,.9*inch,9.95*inch)
    c.drawString(.5*inch,10*inch,array[9])

#-----Weight-----#

    c.drawString(1*inch,10*inch,"Weight:")
    c.line(1.5*inch,9.95*inch,1.8*inch,9.95*inch)
    c.drawString(1.5*inch,10*inch,array[10])

#-----Hair-----#

    c.drawString(1.9*inch,10*inch,"Hair:")
    c.line(2.2*inch,9.95*inch,2.8*inch,9.95*inch)
    c.drawString(2.2*inch,10*inch,array[11])

#-----Eyes-----#

    c.drawString(2.9*inch,10*inch,"Eyes:")
    c.line(3.3*inch,9.95*inch,4.1*inch,9.95*inch)
    c.drawString(3.3*inch,10*inch,array[12])

#-----Appearance-----#

    c.drawString(4.2*inch,10*inch,"Appearance:")
    c.line(5*inch,9.95*inch,5.8*inch,9.95*inch)
    c.drawString(5*inch,10*inch,array[13])

#-----Reaction Adj.-----#

    c.drawString(5.9*inch,10*inch,"Reaction Adj.:")
    c.line(6.8*inch,9.95*inch,7*inch,9.95*inch)
    c.drawString(6.8*inch,10*inch,array[14])

#------------------#
# End of Section 1 #
#------------------#

    c.line(-.8*inch,9.75*inch,7.5*inch,9.75*inch)

#-----------------#
# Begin Section 2 #
#-----------------#

    #-STRENGTH-#

    c.rect(-.9*inch,9.4*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,9.5*inch,"STR |")
    c.drawString(-.4*inch,9.5*inch,str(array[15]))
    c.drawString(0*inch,9.5*inch,"Hit Prob:")
    c.drawString(.7*inch,9.5*inch,array[16])
    c.drawString(1.1*inch,9.5*inch,"DMG Adj.:")
    c.drawString(1.8*inch,9.5*inch,array[17])
    c.drawString(2.2*inch,9.5*inch,"Enc.:")
    c.drawString(2.6*inch,9.5*inch,array[18])
    c.drawString(3.3*inch,9.5*inch,"Max Press:")
    c.drawString(4.1*inch,9.5*inch,array[19])
    c.drawString(4.4*inch,9.5*inch,"Open Door:")
    c.drawString(5.2*inch,9.5*inch,array[20])
    c.drawString(5.5*inch,9.5*inch,"B.B./L.G.:")
    c.drawString(6.1*inch,9.5*inch,array[21])

    #-DEXTERITY-#

    c.rect(-.9*inch,9.1*inch,8*inch,.3*inch)
    c.line(-.1*inch,9.1*inch,-.1*inch,9.7*inch)
    c.drawString(-.8*inch,9.2*inch,"DEX |")
    c.drawString(-.4*inch,9.2*inch,str(array[22]))
    c.drawString(0*inch,9.2*inch,"Reaction Adj.")
    c.drawString(1*inch,9.2*inch,array[23])
    c.drawString(3*inch,9.2*inch,"Missile Attack Adj.")
    c.drawString(4.5*inch,9.2*inch,array[24])
    c.drawString(5*inch,9.2*inch,"Defensive Adj.")
    c.drawString(6*inch,9.2*inch,array[25])

    #-CONSTITUTION-#

    c.rect(-.9*inch,8.8*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,8.9*inch,"CON |")
    c.drawString(-.4*inch,8.9*inch,str(array[26]))
    c.drawString(0*inch,8.9*inch,"HP Adj.:")
    c.drawString(.5*inch,8.9*inch,array[27])
    c.drawString(1*inch,8.9*inch,"System Shock:")
    c.drawString(2*inch,8.9*inch,array[28])
    c.drawString(2.5*inch,8.9*inch,"Rez Survival:")
    c.drawString(3.5*inch,8.9*inch,array[29])
    c.drawString(4*inch,8.9*inch,"Poison Save:")
    c.drawString(5*inch,8.9*inch,array[30])
    c.drawString(5.5*inch,8.9*inch,"Regeneration:")
    c.drawString(6.5*inch,8.9*inch,array[31])

    #-Intelligence-#

    c.rect(-.9*inch,8.5*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,8.6*inch,"INT |")
    c.drawString(-.4*inch,8.6*inch,str(array[32]))
    c.drawString(0*inch,8.6*inch,"Languages:")
    c.drawString(.8*inch,8.6*inch,array[33])
    c.drawString(1*inch,8.6*inch,"Spell Level:")
    c.drawString(2*inch,8.6*inch,array[34])
    c.drawString(2.5*inch,8.6*inch,"Chance to Learn:")
    c.drawString(3.7*inch,8.6*inch,array[35])
    c.drawString(4*inch,8.6*inch,"Max Spells:")
    c.drawString(5*inch,8.6*inch,array[36])
    c.drawString(5.5*inch,8.6*inch,"Illusion Immune:")
    c.drawString(6.6*inch,8.6*inch,array[37])

    #-Wisdom-#

    c.rect(-.9*inch,8.2*inch,8*inch,.3*inch)
    c.line(-.1*inch,8.2*inch,-.1*inch,9.7*inch)
    c.drawString(-.8*inch,8.3*inch,"WIS |")
    c.drawString(-.4*inch,8.3*inch,str(array[33]))
    c.drawString(0*inch,8.3*inch,"Magic Def. Adj.:")
    c.drawString(1*inch,8.3*inch,array[34])
    c.drawString(2*inch,8.3*inch,"Bonus Spells:")
    c.drawString(3*inch,8.3*inch,array[35])
    c.drawString(4*inch,8.3*inch,"Spell Fail:")
    c.drawString(5*inch,8.3*inch,array[36])
    c.drawString(6*inch,8.3*inch,"Spell Immune:")
    c.drawString(7*inch,8.3*inch,array[37])

    #-Charisma-#

    c.rect(-.9*inch,7.9*inch,8*inch,.3*inch)
    c.line(-.1*inch,7.9*inch,-.1*inch,9.7*inch)
    c.drawString(-.8*inch,8*inch,"CHA |")
    c.drawString(-.4*inch,8*inch,str(array[22]))
    c.drawString(0*inch,8*inch,"Max Hench:")
    c.drawString(1*inch,8*inch,array[23])
    c.drawString(3*inch,8*inch,"Loyalty Base:")
    c.drawString(4.5*inch,8*inch,array[24])
    c.drawString(5*inch,8*inch,"Reaction Adj.:")
    c.drawString(6*inch,8*inch,array[25])



    
    
    c.showPage() #finishes writing on current page, starts a new page if more is added
    c.save() #finalizes the document
    return 0

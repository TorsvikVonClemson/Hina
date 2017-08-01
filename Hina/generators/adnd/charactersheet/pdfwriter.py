from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

    #c.line(x1,y1,x2,y2)


def write(header,attributes,proficiencies,weapons,dosh,hp,armour,move,save,fp):


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
    c.drawString(-.1*inch,10.5*inch,header[0])

#-----Level-----#

    c.drawString(3.1*inch,10.5*inch,"Level:")
    c.line(3.6*inch,10.45*inch,3.8*inch,10.45*inch)
    c.drawString(3.6*inch,10.5*inch,header[1])

#-----Race-----#

    c.drawString(3.9*inch,10.5*inch,"Race:")
    c.line(4.4*inch,10.45*inch,7*inch,10.45*inch)
    c.drawString(4.4*inch,10.5*inch,header[2])

#-------#
# Row 2 #
#-------#

#-----Class-----#

    c.drawString(-.8*inch,10.25*inch,"Class:")
    c.line(-.3*inch,10.20*inch,.5*inch,10.20*inch)
    c.drawString(-.3*inch,10.25*inch,header[3])

#-----Alignment-----#

    c.drawString(.6*inch,10.25*inch,"Alignment:")
    c.line(1.3*inch,10.20*inch,1.5*inch,10.20*inch)
    c.drawString(1.3*inch,10.25*inch,header[4])

#-----Religion-----#

    c.drawString(1.6*inch,10.25*inch,"Religion:")
    c.line(2.2*inch,10.20*inch,3*inch,10.20*inch)
    c.drawString(2.2*inch,10.25*inch,header[5])

#-----Homeland-----#

    c.drawString(3.1*inch,10.25*inch,"Homeland:")
    c.line(3.8*inch,10.20*inch,5.4*inch,10.20*inch)
    c.drawString(3.8*inch,10.25*inch,header[6])

#-----Gender-----#

    c.drawString(5.5*inch,10.25*inch,"Gender:")
    c.line(6*inch,10.20*inch,7*inch,10.20*inch)
    c.drawString(6*inch,10.25*inch,header[7])

#-------#
# Row 3 #
#-------#


#-----Age-----#

    c.drawString(-.8*inch,10*inch,"Age:")
    c.line(-.3*inch,9.95*inch,0*inch,9.95*inch)
    c.drawString(-.3*inch,10*inch,header[8])

#-----Height-----#

    c.drawString(0*inch,10*inch,"Height:")
    c.line(.5*inch,9.95*inch,.9*inch,9.95*inch)
    c.drawString(.5*inch,10*inch,header[9])

#-----Weight-----#

    c.drawString(1*inch,10*inch,"Weight:")
    c.line(1.5*inch,9.95*inch,1.8*inch,9.95*inch)
    c.drawString(1.5*inch,10*inch,header[10])

#-----Hair-----#

    c.drawString(1.9*inch,10*inch,"Hair:")
    c.line(2.2*inch,9.95*inch,2.8*inch,9.95*inch)
    c.drawString(2.2*inch,10*inch,header[11])

#-----Eyes-----#

    c.drawString(2.9*inch,10*inch,"Eyes:")
    c.line(3.3*inch,9.95*inch,4.1*inch,9.95*inch)
    c.drawString(3.3*inch,10*inch,header[12])

#-----Appearance-----#

    c.drawString(4.2*inch,10*inch,"Appearance:")
    c.line(5*inch,9.95*inch,5.8*inch,9.95*inch)
    c.drawString(5*inch,10*inch,header[13])

#-----Reaction Adj.-----#

    c.drawString(5.9*inch,10*inch,"Reaction Adj.:")
    c.line(6.8*inch,9.95*inch,7*inch,9.95*inch)
    c.drawString(6.8*inch,10*inch,header[14])

#------------------#
# End of Section 1 #
#------------------#

    c.line(-.8*inch,9.75*inch,7.5*inch,9.75*inch)

#-----------------#
# Begin Section 2 #
#-----------------#

    #-STRENGTH-#

    c.rect(-.9*inch,9.4*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,9.5*inch,"STR")
    c.drawString(-.4*inch,9.5*inch,str(attributes[0]))
    c.drawString(0*inch,9.5*inch,"Hit Prob:")
    c.drawString(.7*inch,9.5*inch,attributes[1])
    c.drawString(1.1*inch,9.5*inch,"DMG Adj.:")
    c.drawString(1.8*inch,9.5*inch,attributes[2])
    c.drawString(2.2*inch,9.5*inch,"Enc.:")
    c.drawString(2.6*inch,9.5*inch,attributes[3])
    c.drawString(3.3*inch,9.5*inch,"Max Press:")
    c.drawString(4.1*inch,9.5*inch,attributes[4])
    c.drawString(4.4*inch,9.5*inch,"Open Door:")
    c.drawString(5.2*inch,9.5*inch,attributes[5])
    c.drawString(5.5*inch,9.5*inch,"B.B./L.G.:")
    c.drawString(6.1*inch,9.5*inch,attributes[6])

    #-DEXTERITY-#

    c.rect(-.9*inch,9.1*inch,8*inch,.3*inch)
    c.line(-.1*inch,9.1*inch,-.1*inch,9.7*inch)
    c.drawString(-.8*inch,9.2*inch,"DEX")
    c.drawString(-.4*inch,9.2*inch,str(attributes[7]))
    c.drawString(0*inch,9.2*inch,"Reaction Adj.")
    c.drawString(1*inch,9.2*inch,attributes[8])
    c.drawString(3*inch,9.2*inch,"Missile Attack Adj.")
    c.drawString(4.5*inch,9.2*inch,attributes[9])
    c.drawString(5*inch,9.2*inch,"Defensive Adj.")
    c.drawString(6*inch,9.2*inch,attributes[10])

    #-CONSTITUTION-#

    c.rect(-.9*inch,8.8*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,8.9*inch,"CON")
    c.drawString(-.4*inch,8.9*inch,str(attributes[11]))
    c.drawString(0*inch,8.9*inch,"HP Adj.:")
    c.drawString(.5*inch,8.9*inch,attributes[12])
    c.drawString(1*inch,8.9*inch,"System Shock:")
    c.drawString(2*inch,8.9*inch,attributes[13])
    c.drawString(2.5*inch,8.9*inch,"Rez Survival:")
    c.drawString(3.5*inch,8.9*inch,attributes[14])
    c.drawString(4*inch,8.9*inch,"Poison Save:")
    c.drawString(5*inch,8.9*inch,attributes[15])
    c.drawString(5.5*inch,8.9*inch,"Regeneration:")
    c.drawString(6.5*inch,8.9*inch,attributes[16])

    #-Intelligence-#

    c.rect(-.9*inch,8.5*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,8.6*inch,"INT")
    c.drawString(-.4*inch,8.6*inch,str(attributes[17]))
    c.drawString(0*inch,8.6*inch,"Languages:")
    c.drawString(.8*inch,8.6*inch,attributes[18])
    c.drawString(1*inch,8.6*inch,"Spell Level:")
    c.drawString(2*inch,8.6*inch,attributes[19])
    c.drawString(2.5*inch,8.6*inch,"Chance to Learn:")
    c.drawString(3.7*inch,8.6*inch,attributes[20])
    c.drawString(4*inch,8.6*inch,"Max Spells:")
    c.drawString(5*inch,8.6*inch,attributes[21])
    c.drawString(5.5*inch,8.6*inch,"Illusion Immune:")
    c.drawString(6.6*inch,8.6*inch,attributes[22])

    #-Wisdom-#

    c.rect(-.9*inch,8.2*inch,8*inch,.3*inch)
    c.line(-.1*inch,8.2*inch,-.1*inch,9.7*inch)
    c.drawString(-.8*inch,8.3*inch,"WIS")
    c.drawString(-.4*inch,8.3*inch,str(attributes[23]))
    c.drawString(0*inch,8.3*inch,"Magic Def. Adj.:")
    c.drawString(1*inch,8.3*inch,attributes[24])
    c.drawString(2*inch,8.3*inch,"Bonus Spells:")
    c.drawString(3*inch,8.3*inch,attributes[25])
    c.drawString(4*inch,8.3*inch,"Spell Fail:")
    c.drawString(5*inch,8.3*inch,attributes[26])
    c.drawString(6*inch,8.3*inch,"Spell Immune:")
    c.drawString(7*inch,8.3*inch,attributes[27])

    #-Charisma-#

    c.rect(-.9*inch,7.9*inch,8*inch,.3*inch)
    c.line(-.1*inch,7.9*inch,-.1*inch,9.7*inch)
    c.drawString(-.8*inch,8*inch,"CHA")
    c.drawString(-.4*inch,8*inch,str(attributes[28]))
    c.drawString(0*inch,8*inch,"Max Hench:")
    c.drawString(1*inch,8*inch,attributes[29])
    c.drawString(3*inch,8*inch,"Loyalty Base:")
    c.drawString(4.5*inch,8*inch,attributes[30])
    c.drawString(5*inch,8*inch,"Reaction Adj.:")
    c.drawString(6*inch,8*inch,attributes[31])

#---------------#
# End Section 2 #
#---------------#

#-----------------#
# Begin Section 3 #
#-----------------#

#---Health/Armour---#

    c.rect(-.9*inch,6.8*inch,2.8*inch,1*inch)
    c.drawString(-.8*inch,7.55*inch,"HP")
    c.drawString(-.1*inch,7.55*inch,str(hp))

    c.drawString(.5*inch,7.55*inch,"Armour")
    c.line(.5*inch,7.45*inch,1*inch,7.45*inch)
    c.drawString(.5*inch,7.25*inch,str(armour[1]))

    c.drawString(1.2*inch,7.55*inch,"Weight:")
    c.drawString(1.7*inch,7.55*inch,(str(armour[4])))


    c.drawString(-.8*inch,7.25*inch,"AC")
    if attributes[10].find('-') != 0:
        attributes[10]=attributes[10].lstrip('-')
        c.drawString(-.1*inch,7.25*inch,str(int(armour[2])-int(attributes[10])))
    elif attributes[10].find('+') != 0:
        attributes[10]=attributes[10].lstrip('+')
        c.drawString(-.1*inch,7.25*inch,str(int(armour[2])+int(attributes[10])))
    else:
        c.drawString(-.1*inch,7.25*inch,str(int(armour[2])))


    c.drawString(-.1*inch,7.25*inch,str(int(armour[2])+int(attributes[10])))

    c.drawString(-.8*inch,6.95*inch,"Flatfoot")
    c.drawString(-.1*inch,6.95*inch,str(armour[2]))

    c.drawString(.5*inch,6.95*inch,str(armour[3]))


#---Movement---#

    c.rect(2.1*inch,6.8*inch,5*inch,1*inch)

    c.drawString(2.2*inch,7.6*inch,"Unencumbered:")
    c.drawString(2.2*inch,7.35*inch,"Light:")
    c.drawString(2.2*inch,7.2*inch,"Moderate:")
    c.drawString(2.2*inch,7.05*inch,"Heavy:")
    c.drawString(2.2*inch,6.9*inch,"Severe:")

    c.drawString(3.2*inch,7.35*inch,move[5])
    c.drawString(3.2*inch,7.2*inch,move[6])
    c.drawString(3.2*inch,7.05*inch,move[7])
    c.drawString(3.2*inch,6.9*inch,move[8])

    c.drawString(3.7*inch,7.6*inch,str(move[0]))
    c.drawString(3.7*inch,7.35*inch,str(move[1]))
    c.drawString(3.7*inch,7.2*inch,str(move[2]))
    c.drawString(3.7*inch,7.05*inch,str(move[3]))
    c.drawString(3.7*inch,6.9*inch,str(move[4]))

    c.drawString(4.2*inch,7.6*inch,"")
    c.drawString(4.2*inch,7.35*inch,"Jog")
    c.drawString(4.2*inch,7.2*inch,"Charge")
    c.drawString(4.2*inch,7.05*inch,"Run")
    c.drawString(4.2*inch,6.9*inch,"Sprint")

    c.line(4.3*inch,7.55*inch,7*inch,7.55*inch)

    c.drawString(4.7*inch,7.6*inch,"Speed")
    c.drawString(4.7*inch,7.35*inch,"X2")
    c.drawString(4.7*inch,7.2*inch,"X3")
    c.drawString(4.7*inch,7.05*inch,"X4")
    c.drawString(4.7*inch,6.9*inch,"X5")

    c.drawString(5.2*inch,7.6*inch,"Atk Adj.")
    c.drawString(5.2*inch,7.35*inch,"0")
    c.drawString(5.2*inch,7.2*inch,"+2")
    c.drawString(5.2*inch,7.05*inch,"+4")
    c.drawString(5.2*inch,6.9*inch,"+8")

    c.drawString(5.8*inch,7.6*inch,"Dmg Adj.")
    c.drawString(5.8*inch,7.35*inch,"0")
    c.drawString(5.8*inch,7.2*inch,"0")
    c.drawString(5.8*inch,7.05*inch,"+1")
    c.drawString(5.8*inch,6.9*inch,"+2")

    c.drawString(6.4*inch,7.6*inch,"AC Adj")
    c.drawString(6.4*inch,7.35*inch,"Flatfoot")
    c.drawString(6.4*inch,7.2*inch,"+1")
    c.drawString(6.4*inch,7.05*inch,"+3")
    c.drawString(6.4*inch,6.9*inch,"+5")


#------------------#
# Begin Weapon Box #
#------------------#

    c.drawString(3*inch,6.6*inch,"Weapons")
    c.rect(-.9*inch,6.2*inch,8*inch,.3*inch)

    c.drawString(-.8*inch,6.3*inch,"Name")
    c.line(1.5*inch,4.7*inch,1.5*inch,6.5*inch)		#Name
    c.drawString(1.6*inch,6.3*inch,"RoF")
    c.line(2*inch,4.7*inch,2*inch,6.5*inch)		#RoF
    c.drawString(2.1*inch,6.3*inch,"Atk Adj.")
    c.line(2.7*inch,4.7*inch,2.7*inch,6.5*inch)		#atkadj
    c.drawString(2.8*inch,6.3*inch,"Dmg Adj.")
    c.line(3.4*inch,4.7*inch,3.4*inch,6.5*inch)		#dmgadj
    c.drawString(3.5*inch,6.3*inch,"Damage")
    c.line(4.4*inch,4.7*inch,4.4*inch,6.5*inch)		#dmg
    c.drawString(4.5*inch,6.3*inch,"Range")
    c.line(5.4*inch,4.7*inch,5.4*inch,6.5*inch)		#range
    c.drawString(5.5*inch,6.3*inch,"Type")
    c.line(5.9*inch,4.7*inch,5.9*inch,6.5*inch)		#type
    c.drawString(6*inch,6.3*inch,"Speed")
    c.line(6.5*inch,4.7*inch,6.5*inch,6.5*inch)		#speed
    c.drawString(6.6*inch,6.3*inch,"Weight")

#---Weapon 1---#
    c.rect(-.9*inch,5.9*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,6*inch,weapons[1])
    c.drawString(1.6*inch,6*inch,weapons[2])
    c.drawString(2.1*inch,6*inch,weapons[3])
    c.drawString(2.8*inch,6*inch,weapons[4])
    c.drawString(3.5*inch,6*inch,weapons[5])
    c.drawString(4.5*inch,6*inch,weapons[6])
    c.drawString(5.5*inch,6*inch,weapons[7])
    c.drawString(6*inch,6*inch,weapons[8])
    c.drawString(6.6*inch,6*inch,weapons[9])
#---Weapon 2---#
    c.rect(-.9*inch,5.6*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,5.7*inch,weapons[10])
    c.drawString(1.6*inch,5.7*inch,weapons[11])
    c.drawString(2.1*inch,5.7*inch,weapons[12])
    c.drawString(2.8*inch,5.7*inch,weapons[13])
    c.drawString(3.5*inch,5.7*inch,weapons[14])
    c.drawString(4.5*inch,5.7*inch,weapons[15])
    c.drawString(5.5*inch,5.7*inch,weapons[16])
    c.drawString(6*inch,5.7*inch,weapons[17])
    c.drawString(6.6*inch,5.7*inch,weapons[18])
#---Weapon 3---#
    c.rect(-.9*inch,5.3*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,5.4*inch,weapons[19])
    c.drawString(1.6*inch,5.4*inch,weapons[20])
    c.drawString(2.1*inch,5.4*inch,weapons[21])
    c.drawString(2.8*inch,5.4*inch,weapons[22])
    c.drawString(3.5*inch,5.4*inch,weapons[23])
    c.drawString(4.5*inch,5.4*inch,weapons[24])
    c.drawString(5.5*inch,5.4*inch,weapons[25])
    c.drawString(6*inch,5.4*inch,weapons[26])
    c.drawString(6.6*inch,5.4*inch,weapons[27])
#---Weapon 4---#
    c.rect(-.9*inch,5*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,5.1*inch,weapons[28])
    c.drawString(1.6*inch,5.1*inch,weapons[29])
    c.drawString(2.1*inch,5.1*inch,weapons[30])
    c.drawString(2.8*inch,5.1*inch,weapons[31])
    c.drawString(3.5*inch,5.1*inch,weapons[32])
    c.drawString(4.5*inch,5.1*inch,weapons[33])
    c.drawString(5.5*inch,5.1*inch,weapons[34])
    c.drawString(6*inch,5.1*inch,weapons[35])
    c.drawString(6.6*inch,5.1*inch,weapons[36])
#---Weapon 5---#
    c.rect(-.9*inch,4.7*inch,8*inch,.3*inch)
    c.drawString(-.8*inch,4.8*inch,weapons[37])
    c.drawString(1.6*inch,4.8*inch,weapons[38])
    c.drawString(2.1*inch,4.8*inch,weapons[39])
    c.drawString(2.8*inch,4.8*inch,weapons[40])
    c.drawString(3.5*inch,4.8*inch,weapons[41])
    c.drawString(4.5*inch,4.8*inch,weapons[42])
    c.drawString(5.5*inch,4.8*inch,weapons[43])
    c.drawString(6*inch,4.8*inch,weapons[44])
    c.drawString(6.6*inch,4.8*inch,weapons[45])

#-------#
# Saves #
#-------#

    c.rect(-.9*inch,2.95*inch,2*inch,1.65*inch)

    c.drawCentredString(.35*inch,4.45*inch,"Saving Throws")

    c.drawString(-.8*inch,4.25*inch,"Paralyze/Poison")
    c.drawString(-.8*inch,4*inch,"Rod, Staff or Wand")
    c.drawString(-.8*inch,3.75*inch,"Petrify/Polymorph")
    c.drawString(-.8*inch,3.5*inch,"Breath")
    c.drawString(-.8*inch,3.25*inch,"Spell")
    c.drawString(-.8*inch,3*inch,"Macabre")

#---Modify Saves Based on Attributes---#

#Poison#

    if attributes[15].find('-') != 0:
        attributes[15]=attributes[15].lstrip('-')
        save[0]=save[0]+int(attributes[15])
    elif attributes[15].find('+') != 0:
        save[0]=save[0]-int(attributes[15])

#Magic Save#

    if attributes[24].find('-') != 0:
        attributes[24]=attributes[24].lstrip('-')
        save[4]=save[4]+int(attributes[24])
    elif attributes[24].find('+') != 0:
        save[4]=save[4]-int(attributes[24])

#Mind that Dwarves get an additional Magic and Poison save.

    c.drawString(.6*inch,4.25*inch,str(save[0]))
    c.drawString(.6*inch,4*inch,str(save[1]))
    c.drawString(.6*inch,3.75*inch,str(save[2]))
    c.drawString(.6*inch,3.5*inch,str(save[3]))
    c.drawString(.6*inch,3.25*inch,str(save[4]))
    c.drawString(.6*inch,3*inch,'0')





#----------------#
# Begin Prof Box #
#----------------#

    c.drawString(1*inch,2.7*inch,"Proficiencies")
    c.rect(-.9*inch,0*inch,4.6*inch,2.85*inch)

#---Column 1---#

    c.drawString(-.8*inch,2.5*inch,proficiencies[0])
    c.drawString(-.8*inch,2.25*inch,proficiencies[1])
    c.drawString(-.8*inch,2*inch,proficiencies[2])
    c.drawString(-.8*inch,1.75*inch,proficiencies[3])
    c.drawString(-.8*inch,1.5*inch,proficiencies[4])
    c.drawString(-.8*inch,1.25*inch,proficiencies[5])
    c.drawString(-.8*inch,1*inch,proficiencies[6])
    c.drawString(-.8*inch,.75*inch,proficiencies[7])
    c.drawString(-.8*inch,.5*inch,proficiencies[8])
    c.drawString(-.8*inch,.25*inch,proficiencies[9])

    c.line(-.8*inch,2.45*inch,1.2*inch,2.45*inch)
    c.line(-.8*inch,2.2*inch,1.2*inch,2.2*inch)
    c.line(-.8*inch,1.95*inch,1.2*inch,1.95*inch)
    c.line(-.8*inch,1.7*inch,1.2*inch,1.7*inch)
    c.line(-.8*inch,1.45*inch,1.2*inch,1.45*inch)
    c.line(-.8*inch,1.2*inch,1.2*inch,1.2*inch)
    c.line(-.8*inch,.95*inch,1.2*inch,.95*inch)
    c.line(-.8*inch,.7*inch,1.2*inch,.7*inch)
    c.line(-.8*inch,.45*inch,1.2*inch,.45*inch)
    c.line(-.8*inch,.2*inch,1.2*inch,.2*inch)

#---Column 2---#

    c.drawString(1.4*inch,2.5*inch,proficiencies[10])
    c.drawString(1.4*inch,2.25*inch,proficiencies[11])
    c.drawString(1.4*inch,2*inch,proficiencies[12])
    c.drawString(1.4*inch,1.75*inch,proficiencies[13])
    c.drawString(1.4*inch,1.5*inch,proficiencies[14])
    c.drawString(1.4*inch,1.25*inch,proficiencies[15])
    c.drawString(1.4*inch,1*inch,proficiencies[16])
    c.drawString(1.4*inch,.75*inch,proficiencies[17])
    c.drawString(1.4*inch,.5*inch,proficiencies[18])
    c.drawString(1.4*inch,.25*inch,proficiencies[19])

    c.line(1.4*inch,2.45*inch,3.4*inch,2.45*inch)
    c.line(1.4*inch,2.2*inch,3.4*inch,2.2*inch)
    c.line(1.4*inch,1.95*inch,3.4*inch,1.95*inch)
    c.line(1.4*inch,1.7*inch,3.4*inch,1.7*inch)
    c.line(1.4*inch,1.45*inch,3.4*inch,1.45*inch)
    c.line(1.4*inch,1.2*inch,3.4*inch,1.2*inch)
    c.line(1.4*inch,.95*inch,3.4*inch,.95*inch)
    c.line(1.4*inch,.7*inch,3.4*inch,.7*inch)
    c.line(1.4*inch,.45*inch,3.4*inch,.45*inch)
    c.line(1.4*inch,.2*inch,3.4*inch,.2*inch)

#--------------#
# Temp Section #
#--------------#

    c.drawString(6*inch,2.65*inch,str(dosh))



    
    
    c.showPage() #finishes writing on current page, starts a new page if more is added
    c.save() #finalizes the document
    return 0

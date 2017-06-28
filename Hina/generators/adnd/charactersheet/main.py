import os
from reportlab.pdfgen import canvas
from generators.adnd.charactersheet import pdfwriter

from generators.adnd.charactersheet.race import races
from generators.adnd.charactersheet.race import genders
from generators.adnd.charactersheet.race import names
from generators.adnd.charactersheet.race import religion
from generators.adnd.charactersheet.classes import classes
from generators.adnd.charactersheet.classes import attribute
from generators.adnd.charactersheet.classes import strength
from generators.adnd.charactersheet.classes import dexterity
from generators.adnd.charactersheet.classes import constitution
from generators.adnd.charactersheet.classes import intelligence
from generators.adnd.charactersheet.classes import wisdom
from generators.adnd.charactersheet.classes import charisma
from generators.adnd.charactersheet.classes import proficiencies
#from generators.adnd.charactersheet.fluff import religion

def main(x):

    x=[]

    race=""			#
    while race!="Human":	#Temporary Code to force Race
        race=races.roll()	#
    gender=genders.roll(race)
    name=names.roll(race,gender)
    playerclass=classes.roll(race)
    attributes=attribute.roll(race,playerclass)
    stronk=strength.roll(attributes[0])
    dex=dexterity.roll(attributes[1])
    con=constitution.roll(attributes[2])
    smarts=intelligence.roll(attributes[3])
    wis=wisdom.roll(attributes[4])
    cha=charisma.roll(attributes[5])
    profs=proficiencies.roll(race,playerclass,attributes[3])
    god=religion.roll(race)
#    religion=religion.roll(race)
    title=name+' '+race+' '+playerclass


    file = "/generators/adnd/charactersheet/saved/trash/{}.txt"
    pdffile =  "/generators/adnd/charactersheet/saved/trash/{}.pdf"
    path=os.getcwd()+file
    pdfpath=os.getcwd()+pdffile
    with open(path.format(title),"w") as text_file:

#-------------------------------#
#    Character Sheet Headers    #
#-------------------------------#

        text_file.write("Name: {}\n".format(name))
        text_file.write("Race: {}\n".format(race))
        text_file.write("Gender: {}\n".format(gender))
        text_file.write("Class: {}\n".format(playerclass))
        text_file.write("Homeland: {}\n")
        text_file.write("Religion: {}\n")
        text_file.write("Motivation: {}\n")
        text_file.write("Alignment: {}\n")
        text_file.write("Personality: {}\n")
        text_file.write("Social Class/Previous Occupation: {}\n")
        text_file.write("Hair: {}\n")
        text_file.write("Eyes: {}\n")
        text_file.write("Appearance: {}\n")
        text_file.write("Height: {}\n")
        text_file.write("Weight: {}\n")

#-------------------------------------#
#    Attributes and Related Values    #
#-------------------------------------#

#Strength

        text_file.write("Str: {}\n".format(attributes[0]))
        text_file.write("Hit Adj: {}\n".format(stronk[0]))
        text_file.write("Dmg Adj: {}\n".format(stronk[1]))
        text_file.write("Weight Allowed:{}\n".format(stronk[2]))
        text_file.write("Max Press: {}\n".format(stronk[3]))
        text_file.write("Open Door:{}\n".format(stronk[4]))
        text_file.write("Bend Bar Lift Gate: {}\n".format(stronk[5]))

#Dexterity
        text_file.write("Dex: {}\n".format(attributes[1]))

#Constitution
        text_file.write("Con: {}\n".format(attributes[2]))

#Intelligence
        text_file.write("Int: {}\n".format(attributes[3]))

#Wisdom
        text_file.write("Wis: {}\n".format(attributes[4]))

#Constitution
        text_file.write("Cha: {}\n".format(attributes[5]))

#---------#
# HP & AC #
#---------#


#---------------------#
#    Proficiencies    #
#---------------------#

        length=len(profs)

        while length>0:
              text_file.write(profs[length-1])
              text_file.write("\n")
              length -= 1

    text_file.close()

#-------------#
# PDF Writing #
#-------------#

    pdfarray=[]

#-----Header-----#

    pdfarray.append(name)
    pdfarray.append("1") #TEMP SPACE FOR LEVEL
    pdfarray.append(race)
    pdfarray.append(playerclass)
    pdfarray.append("TN")#TEMP SPACE FOR ALIGNMENT
    pdfarray.append(god)
    pdfarray.append("HOME")#TEMP SPACE FOR HOME
    pdfarray.append(gender)
    pdfarray.append("69")#TEMP SPACE FOR AGE
    pdfarray.append("4'20")#TEMP SPACE FOR HEIGHT
    pdfarray.append("420")#TEMP SPACE FO WEIGHT
    pdfarray.append("BALD")#TEMP SPACE FOR HAIR
    pdfarray.append("NONE")#TEMP SPACE FOR EYES
    pdfarray.append("UGLY")#TEMP SPACE FOR APPEARANCE
    pdfarray.append("0")#TEMP SPACE FOR REACTION ADJ


#-----Attributes-----#

    pdfarray.append(attributes[0])
    pdfarray=pdfarray+stronk
    pdfarray.append(attributes[1])
    pdfarray=pdfarray+dex
    pdfarray.append(attributes[2])
    pdfarray=pdfarray+con
    pdfarray.append(attributes[3])
    pdfarray=pdfarray+smarts
    pdfarray.append(attributes[4])
    pdfarray=pdfarray+wis
    pdfarray.append(attributes[5])
    pdfarray=pdfarray+cha

    pdfwriter.write(pdfarray,pdfpath.format(title))

#--------#
# Return #
#--------#

    x.append(pdfpath.format(title))

    x.append("\n\n**Character Sheets are automatically saved to a trash folder that will be occasionally cleared, notify me if there is one you want to keep.**\n\n**The only race that can be rolled right now is 'Human' while tests are being conducted**\n\n**Right now 18/00 Strength doesn't work proper so untill it gets fixed so if a Human Fighter has 18 Strength refer to the stats for 18/00 in the book.**\n\n**I encourage contributions, it means alot more can get done.**\n\n**Tell me if an error occurs!**\n\n**        -Love, Hina**")

    return x

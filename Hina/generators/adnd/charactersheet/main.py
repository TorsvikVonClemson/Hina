import os
from reportlab.pdfgen import canvas
from generators.adnd.charactersheet import pdfwriter

from generators.adnd.charactersheet.race import races
from generators.adnd.charactersheet.race import genders
from generators.adnd.charactersheet.race import names
from generators.adnd.charactersheet.classes import classes
from generators.adnd.charactersheet.classes import attribute
from generators.adnd.charactersheet.classes import proficiencies
#from generators.adnd.charactersheet.fluff import religion

def main(x):

    x=[]
    
    race=races.roll()
    gender=genders.roll(race)
    name=names.roll(race,gender)
    playerclass=classes.roll(race)
    attributes=attribute.roll(race,playerclass)
    profs=proficiencies.roll(race,playerclass,attributes[3])
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

        text_file.write("======================================================================================================\n".format(attributes[5]))

        text_file.write("Name: {}\t".format(name))
        text_file.write("Race: {}\t".format(race))
        text_file.write("Gender: {}\t".format(gender))
        text_file.write("Class: {}\n".format(playerclass))
        text_file.write("Homeland: {}\t")
        text_file.write("Religion: {}\t")
        text_file.write("Motivation: {}\t")
        text_file.write("Alignment: {}\n")
        text_file.write("Personality: {}\t")
        text_file.write("Social Class/Previous Occupation: {}\n")
        text_file.write("Hair: {}\t")
        text_file.write("Eyes: {}\t")
        text_file.write("Appearance: {}\t")
        text_file.write("Height: {}\t")
        text_file.write("Weight: {}\n\n")

#-------------------------------------#
#    Attributes and Related Values    #
#-------------------------------------#

        text_file.write("======================================================================================================\n".format(attributes[5]))


#Strength
    #Row 1
        text_file.write("Str: {}\t\t".format(attributes[0]))
        text_file.write("Hit: {}\t\t")
        text_file.write("Dmg: {}\t\t")
        text_file.write("Weight:\t\t")
        text_file.write("Max: {}\t\t")
        text_file.write("Open:\t\t")
        text_file.write("B B: {}\n")

    #Row 2
        text_file.write("\t\tProb\t\t")
        text_file.write("Adj.\t\t")
        text_file.write("Allowed\t\t")
        text_file.write("Press\t\t")
        text_file.write("Doors\t\t")
        text_file.write("LiftGate\n")

#Dexterity
        text_file.write("Dex: {}\n".format(attributes[1]))

#Constitution
        text_file.write("Con: {}\n".format(attributes[2]))

#Intelligence
        text_file.write("Int: {}\n".format(attributes[3]))

#Wisdom
        text_file.write("Wis: {}\n".format(attributes[4]))

#Constitution
        text_file.write("Cha: {}\n\n\n".format(attributes[5]))

#---------#
# HP & AC #
#---------#

        text_file.write("======================================================================================================\n".format(attributes[5]))


    #Row 1
        text_file.write("-------------------------------------------------\n")

    #Row 2
        text_file.write("| Hit Points: {}\t| Current:\t\t|\n")

    #Row 3
        text_file.write("-------------------------------------------------\n\n")

#---------------------#
#    Proficiencies    #
#---------------------#

        text_file.write("======================================================================================================\n".format(attributes[5]))

        length=len(profs)

        while length>0:
              text_file.write(profs[length-1])
              text_file.write("\n")
              length -= 1

    


    text_file.close()

    with open(path.format(title),"r") as text_file:

        w=text_file.read()

    pdfwriter.write(w,pdfpath.format(title))

    x.append(path.format(title))

    x.append("\n\n**Character Sheets are automatically saved to a trash folder that will be occasionally cleared, notify me if there is one you want to keep.**\n\n**I have switched to a PDF format but until I figure out how to draw with it it will be illegible. I'll keep posting the .txt till its finalized. (still needs to be opened using rich text)**\n\n**I encourage contributions, it means alot more can get done.**\n\n**Tell me if an error occurs!**\n\n**        -Love, Hina**")

    return x

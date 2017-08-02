import os
from reportlab.pdfgen import canvas
from generators.adnd.charactersheet import pdfwriter

from generators.adnd.charactersheet.race import races
from generators.adnd.charactersheet.race import genders
from generators.adnd.charactersheet.race import names
from generators.adnd.charactersheet.race import religion
from generators.adnd.charactersheet.classes import classes
from generators.adnd.charactersheet.classes import saves
from generators.adnd.charactersheet.classes import attribute
from generators.adnd.charactersheet.classes import strength
from generators.adnd.charactersheet.classes import dexterity
from generators.adnd.charactersheet.classes import constitution
from generators.adnd.charactersheet.classes import intelligence
from generators.adnd.charactersheet.classes import wisdom
from generators.adnd.charactersheet.classes import charisma
from generators.adnd.charactersheet.classes import wp
from generators.adnd.charactersheet.classes import dosh
from generators.adnd.charactersheet.classes import proficiencies
from generators.adnd.charactersheet.classes import hitdie
from generators.adnd.charactersheet.equipment import weapons
from generators.adnd.charactersheet.equipment import armour
from generators.adnd.charactersheet.equipment import movement
from generators.adnd.charactersheet.equipment import miscequip
from generators.adnd.charactersheet.special import rogue
from generators.adnd.charactersheet.special import spells

#from generators.adnd.charactersheet.fluff import religion

def main(x):

    x=[]
    skills=[]
    spelllist=[]

    race=""			#
    while race!="Human":	#Temporary Code to force Race
        race=races.roll()	#
    gender=genders.roll(race)
    name=names.roll(race,gender)
    playerclass=classes.roll(race)
    save=saves.roll(playerclass)
    attributes=attribute.roll(race,playerclass)
    stronk=strength.roll(attributes[0])
    move=movement.roll(race,stronk[3])
    dex=dexterity.roll(attributes[1])
    con=constitution.roll(attributes[2])
    smarts=intelligence.roll(attributes[3])
    wis=wisdom.roll(attributes[4])
    cha=charisma.roll(attributes[5])
    hp=hitdie.roll(playerclass,con[0])
    rolleddosh=dosh.roll(playerclass)
    god=religion.roll(race)
    wplist=wp.roll(playerclass,god)
    pdfweapons=weapons.roll(rolleddosh,wplist)
    remainingdosh=pdfweapons[0]
    playerarmour=armour.roll(remainingdosh,playerclass,god,pdfweapons)
    remainingdosh=playerarmour[0]
    miscequ=miscequip.roll(remainingdosh,playerclass)
    remainingdosh=miscequ[0]
    if playerclass=='Rogue':
        skills=skills+rogue.roll(attributes[1])
    if playerclass=='Wizard' or playerclass=='Cleric':
        spelllist=spelllist+spells.roll(playerclass,smarts[0],god)
    else:
        while len(spelllist)<31:
            spelllist.append("")
    profs=proficiencies.roll(race,playerclass,attributes[3])
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


        text_file.write(str(hp))


    text_file.close()

#-------------#
# PDF Writing #
#-------------#

    pdfheader=[]
    pdfattributes=[]
    pdfproficiencies=[]

#-----Header-----#

    pdfheader.append(name)
    pdfheader.append("1") #TEMP SPACE FOR LEVEL
    pdfheader.append(race)
    pdfheader.append(playerclass)
    pdfheader.append("TN")#TEMP SPACE FOR ALIGNMENT
    pdfheader.append(god)
    pdfheader.append("HOME")#TEMP SPACE FOR HOME
    pdfheader.append(gender)
    pdfheader.append("69")#TEMP SPACE FOR AGE
    pdfheader.append("4'20")#TEMP SPACE FOR HEIGHT
    pdfheader.append("420")#TEMP SPACE FO WEIGHT
    pdfheader.append("BALD")#TEMP SPACE FOR HAIR
    pdfheader.append("NONE")#TEMP SPACE FOR EYES
    pdfheader.append("UGLY")#TEMP SPACE FOR APPEARANCE
    pdfheader.append("0")#TEMP SPACE FOR REACTION ADJ


#-----Attributes-----#

    pdfattributes.append(attributes[0])
    pdfattributes=pdfattributes+stronk
    pdfattributes.append(attributes[1])
    pdfattributes=pdfattributes+dex
    pdfattributes.append(attributes[2])
    pdfattributes=pdfattributes+con
    pdfattributes.append(attributes[3])
    pdfattributes=pdfattributes+smarts
    pdfattributes.append(attributes[4])
    pdfattributes=pdfattributes+wis
    pdfattributes.append(attributes[5])
    pdfattributes=pdfattributes+cha

#-----Proficiencies-----#

    pdfproficiencies=wplist+profs
    while len(pdfproficiencies)<20:
        pdfproficiencies.append("")

#----Inventory---#

    while len(pdfweapons)<46:
        pdfweapons.append("")

    pdfwriter.write(pdfheader,pdfattributes,pdfproficiencies,pdfweapons,remainingdosh,hp,playerarmour,move,save,miscequ,skills,spelllist,pdfpath.format(title))

#--------#
# Return #
#--------#

    x.append(pdfpath.format(title))

    x.append("\n\n**Character Sheets are automatically saved to a trash folder that will be occasionally cleared, notify me if there is one you want to keep.**\n\n**The only race that can be rolled right now is 'Human' while tests are being conducted**\n\n**Right now proficiencies sometimes get rolled twice. If its non-weapon treat it as specialized, if its a weapon proficincy you're just out of luck for now**\n\n**I encourage contributions, it means alot more can get done.**\n\n**Tell me if an error occurs!**\n\n**        -Love, Hina**")

    return x

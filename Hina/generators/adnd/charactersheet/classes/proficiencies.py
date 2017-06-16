import random


def roll(race,playerclass,intel):

    proffinal=[]

#------------------------#
# Starting proficiencies #
#------------------------#

    proffinal.append('Language (Faustic)')

    if race=='Dwarf':
        proffinal.append('Language (Dwarven)')

    if race=='Wood Elf':
        proffinal.append('Language (Sylvan)')

    if race=='Orc Merchant' or race=='Goblin Merchant':
        proffinal.append('Language (Greenskin)')

    if race=='Kobold Pilgrim':
        proffinal.append('Language (Utterances)')

    if race=='Elven Spy':
        proffinal.append('Language (Langue Digne)')

    if race=='Drow Refugee':
        proffinal.append('Language (Deepspeech)')
        proffinal.append('Language (Kehlig)')
        proffinal.append('Language (Kehlig Silent)')

    if race=='Oni' or race=='Ogre':
        proffinal.append("Language (Yu'yen)")

    if race=='Fairy':
        proffinal.append('Language (Sylvan)')

    if playerclass=='Rogue':
        proffinal.append("Language (Thieves' Cant)")




#-------------------------------#
# Count Number of proficiencies #
#-------------------------------#

    if playerclass=='Cleric':
        profcount=4
    elif playerclass=='Rogue':
        profcount=3
    elif playerclass=='Fighter':
        profcount=3
    elif playerclass=='Wizard':
        profcount=4
    else:
        profcount=0


    if intel<9:
        profcount=profcount+1
    elif intel>8 and intel<12:
        profcount=profcount+2
    elif intel>11 and intel<14:
        profcount=profcount+3
    elif intel>13 and intel<16:
        profcount=profcount+4
    elif intel==16:
        profcount=profcount+5
    elif intel==17:
        profcount=profcount+6
    elif intel==18:
        profcount=profcount+7
    elif intel==19:
        profcount=profcount+8
    elif intel==20:
        profcount=profcount+9
    elif intel==21:
        profcount=profcount+10
    elif intel==22:
        profcount=profcount+11
    elif intel==23:
        profcount=profcount+12
    elif intel==24:
        profcount=profcount+15
    elif intel==25:
        profcount=profcount+20


#----------------------------#
# Fill General proficiencies #
#----------------------------#


    with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/resources/proficiencies/general.txt","r") as text_file:

       proflist=text_file.readlines()

       text_file.close()

#---------------------------#
# Fill Cleric proficiencies #
#---------------------------#

    if playerclass == 'Cleric':
        
        with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/resources/proficiencies/priest.txt","r") as text_file:

            proflist.extend(text_file.readlines())

            text_file.close()

#--------------------------#
# Fill Rogue proficiencies #
#--------------------------#

    if playerclass == 'Rogue':
        
        with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/resources/proficiencies/rogue.txt","r") as text_file:

            proflist.extend(text_file.readlines())

            text_file.close()

#----------------------------#
# Fill Fighter proficiencies #
#----------------------------#

    if playerclass == 'Fighter':
        
        with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/resources/proficiencies/warrior.txt","r") as text_file:

            proflist.extend(text_file.readlines())

            text_file.close()

#---------------------------#
# Fill Wizard proficiencies #
#---------------------------#

    if playerclass == 'Wizard':
        
        with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/resources/proficiencies/wizard.txt","r") as text_file:

            proflist.extend(text_file.readlines())

            text_file.close()

#-----------------#
# Roll From Lists #
#-----------------#

    while profcount>0:
        profchoice=random.choice(proflist)
        profchoice=profchoice.rstrip('\n')
        proffinal.append(profchoice)
        profcount -= 1

    return proffinal

import random

def roll(race,gender):

#--------#
# Humans #
#--------#

    if race == 'Human' or race== 'Half-Elf':
        if gender == 'Male':
            with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/Resources/Names/germanmalenames.txt","r") as text_file:

                firstname=text_file.readlines()

            text_file.close()

            first=random.choice(firstname)

            first=first.rstrip('\n')
        
        else:
            with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/Resources/Names/germanfemalenames.txt","r") as text_file:

                firstname=text_file.readlines()

            text_file.close()

            first=random.choice(firstname)

            first=first.rstrip('\n')

        with open("/home/torsvik/Documents/Python/Hina/generators/adnd/charactersheet/Resources/Names/germansurnames.txt","r") as text_file:

            surname=text_file.readlines()

        text_file.close()

        sur=random.choice(surname)

        sur=sur.rstrip('\n')

        x=('{}'.format(first)+' '+'{}'.format(sur))

#---------#
# Dwarves #
#---------#

    elif race == 'Dwarf':
        x='TempName'

    elif race == 'Halfling':
        x='TempName'

    elif race == 'Wood Elf':
        x='TempName'

    elif race == 'Orc Merchant':
        x='TempName'

    elif race == 'Goblin Merchant':
        x='TempName'
 
    elif race == 'Kobold Pilgrim':
        x='TempName'

    elif race == 'Foreigner':
        x='TempName'

    elif race == 'Elven Spy':
        x='TempName'

    elif race == 'Drow Refugee':
        x='TempName'

    elif race == 'Oni':
        x='TempName'

    elif race == 'Fairy':
        x='TempName'

    elif race == 'Ogre':
        x='TempName'

    else:x='!!!check for errors!!!'


    return str(x)

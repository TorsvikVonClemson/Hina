import random
def roll(dosh,playerclass,god,weapon):

    if playerclass=='Wizard':
        buy='Unarmoured'
        AC=10
        weight=5

    elif playerclass=='Fighter' or playerclass=='Paladin' or playerclass=='Ranger':
        if dosh>=400 and dosh<500:
            dosh=dosh-400
            buy='Padded'
            AC=9
            weight=10
        elif dosh>=500 and dosh<2000:
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10
        elif dosh>=2000 and dosh<12000:
            dosh=dosh-2000
            buy='Studded Leather'
            AC=7
            weight=25
        elif dosh>=4000 and dosh<7500:
            dosh=dosh-4000
            buy='Brigadine'
            AC=6
            weight=35
        elif dosh>=7500 and dosh<20000:
            dosh=dosh-7500
            buy='Chain Mail'
            AC=5
            weight=40
        elif dosh>=20000 and dosh<60000:
            dosh=dosh-20000
            buy='Banded Mail'
            AC=4
            weight=35
        elif dosh>=60000 and dosh<200000:
            dosh=dosh-60000
            buy='Plate Mail'
            AC=3
            weight=50
        elif dosh>=200000 and dosh<400000:
            dosh=dosh-200000
            buy='Field Plate'
            AC=2
            weight=60
        elif dosh>=400000:
            dosh=dosh-400000
            buy='Full Plate'
            AC=1
            weight=70
        else:
            buy='Unarmoured'
            AC=10
            weight=5

    elif playerclass=='Rogue' or playerclass=='Bard':
        if dosh>=400 and dosh<500:
            dosh=dosh-400
            buy='Padded'
            AC=9
            weight=10
        elif dosh>=500 and dosh<2000:
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10
        elif dosh>=2000 and dosh<12000:
            dosh=dosh-2000
            buy='Studded Leather'
            AC=7
            weight=25
        elif dosh>=4000 and dosh<7500:
            dosh=dosh-4000
            buy='Brigadine'
            AC=6
            weight=35
        elif dosh>=7500 and dosh<20000:
            dosh=dosh-7500
            buy='Chain Mail'
            AC=5
            weight=40
        else:
            buy='Unarmoured'
            AC=10
            weight=5

    elif playerclass=='Cleric':
        if god=="Ilmura":
            dosh=dosh-4000
            buy='Brigadine'
            AC=6
            weight=35

        elif god=="Makabel":
            dosh=dosh-60000
            buy='Plate Mail'
            AC=3
            weight=50

        elif god=="Leuchtag":
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10
    
        elif god=="Strafeherr":
            dosh=dosh-2000
            buy='Spiked Leather'
            AC=7
            weight=25

        elif god=="Tyr":
            dosh=dosh-400000
            buy='Full Plate'
            AC=1
            weight=70

        elif god=="Bahamut":
            dosh=dosh-12000
            buy='Scale'
            AC=6
            weight=40

        elif god=="Hina":
            dosh=dosh-400
            buy='Padded'
            AC=9
            weight=10

        elif god=="Reueherr":
            dosh=dosh-7500
            buy='Chain Mail'
            AC=5
            weight=40

        elif god=="Calandra":
            dosh=dosh-1500
            buy='Hide'
            AC=6
            weight=30

        elif god=="Cisa":
            dosh=dosh-12000
            buy='Coin Mail'
            AC=6
            weight=40

        elif god=="Gerdora":
            dosh=dosh-12000
            buy='Cuirass and Lobster Tail Helm'
            AC=6
            weight=40

        elif god=="Kolsten":
            dosh=dosh-500
            buy='Leather'
            AC=8
            weight=10



#---Shields---#

    if playerclass=='Wizard':
            shield=''

#2H#

    elif (weapon[1]=='Harpoon' or weapon[1].find('Lance') != -1 or weapon[1]=='Quarterstaff' or weapon[1]=='Zweihander' or weapon[1]=='Trident') and (weapon[10]=='Harpoon' or weapon[10].find('Lance') != -1 or weapon[10]=='Quarterstaff' or weapon[10]=='Zweihander' or weapon[10]=='Trident'):
         shield=''


#Reach#

    elif weapon[6]=="Reach" or weapon[15]=="Reach": 
        if dosh>=100 and dosh<300:
            dosh=dosh-100
            shield='Buckler'
            AC=AC-1
            weight=weight+3
        elif dosh>=300 and dosh<700:
            dosh=dosh-300
            shield='Small Shield'
            AC=AC-1
            weight=weight+5
        elif dosh>=700 and dosh<1000:
            dosh=dosh-700
            shield='Medium Shield'
            AC=AC-1
            weight=weight+10
        elif dosh>=1000:
            dosh=dosh-1000
            shield='Body Shield'
            AC=AC-1
            weight=weight+15
        else:
            shield=''

#find damage

    elif weapon[6]=='Melee' and weapon[5]!='2H':
        split=weapon[5].split('/')
        diemod=0
        if split[0].find('+'):
            diemod=.5
            reform=split[0].split('+')
            split[0]=reform[0]
        elif split[0].find('-'):
            diemod=-.5
            reform=split[0].split('-')
            split[0]=reform[0]
        dmg=split[0].split('D')
        maxdmg=int(dmg[0])*int(dmg[1])+int(diemod)
        if maxdmg<6:
            if dosh>=100:
                dosh=dosh-100
                shield='Buckler'
                AC=AC-1
                weight=weight+3
            else:
                shield=''
        elif maxdmg>=6 and maxdmg<8:
            if dosh>=100 and dosh<300:
                dosh=dosh-100
                shield='Buckler'
                AC=AC-1
                weight=weight+3
            elif dosh>=300:
                dosh=dosh-300
                shield='Small Shield'
                AC=AC-1
                weight=weight+5
            else:
                shield=''
        elif maxdmg>=8:
            if dosh>=100 and dosh<300:
                dosh=dosh-100
                shield='Buckler'
                AC=AC-1
                weight=weight+3
            elif dosh>=300 and dosh<700:
                dosh=dosh-300
                shield='Small Shield'
                AC=AC-1
                weight=weight+5
            elif dosh>=700:
                dosh=dosh-700
                shield='Medium Shield'
                AC=AC-1
                weight=weight+10
    elif weapon[15]=='Melee' and weapon[14]!='2H':
        split=weapon[14].split('/')
        diemod=0
        if split[0].find('+'):
            reform=split[0].split('+')
            split[0]=reform[0]
        elif split[0].find('-'):
            reform=split[0].split('-')
            split[0]=reform[0]

        dmg=split[0].split('D')
        maxdmg=int(dmg[0])*int(dmg[1])
        if maxdmg<6:
            if dosh>=100:
                dosh=dosh-100
                shield='Buckler'
                AC=AC-1
                weight=weight+3
            else:
                shield=''
        elif maxdmg>=6 and maxdmg<8:
            if dosh>=100 and dosh<300:
                dosh=dosh-100
                shield='Buckler'
                AC=AC-1
                weight=weight+3
            elif dosh>=300:
                dosh=dosh-300
                shield='Small Shield'
                AC=AC-1
                weight=weight+5
            else:
                shield=''
        elif maxdmg>=8:
            if dosh>=100 and dosh<300:
                dosh=dosh-100
                shield='Buckler'
                AC=AC-1
                weight=weight+3
            elif dosh>=300 and dosh<700:
                dosh=dosh-300
                shield='Small Shield'
                AC=AC-1
                weight=weight+5
            elif dosh>=700:
                dosh=dosh-700
                shield='Medium Shield'
                AC=AC-1
                weight=weight+10
            else:
                shield=''

#Ranged#

    elif weapon[6].find('/') !=-1 or weapon[16].find('/') or weapon[6].find=='Ammunition' or weapon[16].find('/') !=-1 or weapon[6].find=='Ammunition':
        if dosh>=100:
            shield='Buckler'
            AC=AC-1        
        else:
            shield=''


        
    
    stats=[dosh,buy,AC,shield,weight]

    return stats






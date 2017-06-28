import random
def roll(playerclass,god)

    wplist=[]

#--------------#
# Warrior List #
#--------------#

    if class=="Warrior" or class=="Ranger" or class=="Paladin":
        wpcount=4
        while wpcount>0:
            roll=random.randint(1,#)
            if roll==1:
                wp="Battleaxe"
            elif roll==2:
                wp="Blowgun"                                
            elif roll==3:
                wp="Composite Longbow"         
            elif roll==4:
                wp="Composite Shortbow"       
            elif roll==5:
                wp="Shortbow"       
            elif roll==6:
                wp="Longbow"         
            elif roll==7:
                wp="Bola"      
            elif roll==8:
                wp="Chain"      
            elif roll==9:
                wp="Club"      
            elif roll==10:
                wp="Hand Crossbow"                                
            elif roll==11:
                wp="Crossbow"                                 
            elif roll==12:
                wp="Heavy Crossbow"                                 
            elif roll==13:
                wp="Dagger"
            elif roll==14:
                wp="Parrying Dagger"
            elif roll==15:
                wp="Dart"                                 
                                
                                
                                
                                
                                
                                
                                
                                
      
    elif class=="Wizard":
        wpcount=1
    elif class=="Cleric":
        wpcount=2
    elif class=="Rogue" or class=="Bard":
        wpcount=2
        

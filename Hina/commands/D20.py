import random
def say(x):

    n=[]
    x=x.lstrip('!')
    Xplode=False
    if x.find('D') != -1 and x.find('X') == -1:
        values=x.split('D')
    elif x.find('D') != -1 and x.find('X') != -1: 
        x=x.rstrip('X')
        values=x.split('D')
        xplode=True
    elif x.find('K') != -1:
        values=x.split('K')
    size=values[1]
    num=values[0]

#--------------#
# Standard D20 #
#--------------#

    if x.find('D') != -1:
        if int(num)==1:
            total = random.randint(1,int(size))
            final= 'You rolled: '+str(total)
            return str(final)

        else:    
            while int(num)>0:
                num=int(num)
                roll = random.randint(1,int(size))
                n.append(roll)
                num -= 1
            total=sum(n)
            list1=','.join(str(e) for e in n)
            final='You rolled ['+list1+'] for a total of: '+str(total)
            return str(final)

#-------------#
# L5R Systems #
#-------------#

    elif x.find('K') != -1:
        while int(num)>0:
            num=int(num)
            roll = random.randint(1,10)
            while roll%10==0:
                roll = roll + random.randint(1,10)
            n.append(roll)
            num -= 1
 
        n.sort(key=None,reverse=True)
        k=int(size)
        final1='You rolled ['+','.join(str(e) for e in n)
        if k<len(n):
            del n[k:]
        total=sum(n)
        final2=']\n keeping ['+','.join(str(e) for e in n)+']\n totaling a roll of '+str(total)
        final= final1+final2
        return str(final)

#----------------#
# Xploding D20's #
#----------------#

    if xplode:
        if int(num)==1:
            total = random.randint(1,int(size))
            while total%int(size)==0:
                total = total + random.randint(1,10)
            final= 'You rolled: '+str(total)
            return str(final)

        else:    
            while int(num)>0:
                num=int(num)
                roll = random.randint(1,int(size))
                while roll%int(size)==0:
                        roll = roll + random.randint(1,10)
                n.append(roll)
                num -= 1
            total=sum(n)
            list1=','.join(str(e) for e in n)
            final='You rolled ['+list1+'] for a total of: '+str(total)
            return str(final)

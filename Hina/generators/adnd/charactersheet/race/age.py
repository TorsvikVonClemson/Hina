import random
def roll(race):
    i=0
    if race=="Human":
        age=15
        while i!=4:
            age=age+random.randint(1,6)
            i +=1
    return age

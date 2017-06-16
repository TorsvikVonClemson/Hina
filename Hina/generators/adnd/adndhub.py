from generators.adnd.charactersheet import main

def sort(x):
    x=x.lstrip('%ad&d ')
    if x.startswith('charactersheet'):
      x=main.main(x)

    else: x='fault'

    return x

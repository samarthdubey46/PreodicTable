import time
import os

class bcolors:
    OK = '\033[32m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    BLUE = '\033[94m' #BLUE
    BOLD = '\033[1m' #BOLD
def Print(txt,color,end = "\n",bold = False):
    if bold:
        print(f"{color}{bcolors.BOLD}{txt}{bcolors.RESET}",end = end)
    else:
        print(f"{color}{txt}{bcolors.RESET}",end = end)

def clear():
  
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def learn(elements,shortForms,start,till):
    for i in range(start-1,till):
        Print(f"{i+1} = ",bcolors.FAIL,'')
        Print(f"{elements[i] + ' - ' + shortForms[i]}",bcolors.WARNING,bold=True)
        time.sleep(1)
    Print("\nNow every element will appear on the screen one by one and disapper after a while, then you will have to type it",bcolors.OK,bold=True)
    __ = input("Press enter continue: ")
    clear()
    i = start - 1
    while i < till:
        Print("remember The Element",bcolors.OK,bold=True)
        Print(f"{i+1} = ",bcolors.FAIL,'')
        Print(f"{elements[i] + ' - ' + shortForms[i]}",bcolors.WARNING,bold=True)
        time.sleep(3)
        clear()
        Print("Type The Element",bcolors.OK,bold=True)
        ele = input(f"{bcolors.FAIL}{i+1} = {bcolors.RESET}")
        if ele.strip().lower() == elements[i].lower():
            i+=1
            Print(f"That was right",bcolors.OK,bold=True)
        else:
            Print(f"That was Wrong Try Again",bcolors.FAIL,bold=True)
        time.sleep(1)
        clear()
        if(i == till):
            __ = input("Type y to continue or r to repeat this exercise: ")
            if __ == 'r':
                i = start-1
    



if __name__ == "__main__":
    start = int(input("Start from element : "))
    till = int(input("till element number: "))
    till = min(till,118)
    elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorous', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
    shortForms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
    learn(elements,shortForms)
class bcolors:
    OK = '\033[32m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    BLUE = '\033[94m' #BLUE
    BOLD = '\033[1m' #BOLD

def Print(txt,color = bcolors.OK,end = "\n",bold = False):
    if bold:
        print(f"{color}{bcolors.BOLD}{txt}{bcolors.RESET}",end = end)
    else:
        print(f"{color}{txt}{bcolors.RESET}",end = end)

def play(elements,shortForms,start,till,out=False):
    i = start - 1
    resets = 0
    Totalcorrect = till
    while i < till:
        correct = elements[i].lower()
        ele = input(f"{bcolors.FAIL}{i+1} = {bcolors.RESET}")
        lowered = ele.strip().lower()
        gotWrong = lowered != correct and lowered != shortForms[i].lower() 
        if gotWrong:
            Print(f"The correct ans was {elements[i] + '-' + shortForms[i]}",bcolors.FAIL)
            Totalcorrect -= 1
            if out:
                i = 0
                resets+=1
                continue
        if not gotWrong:
            if lowered == shortForms[i].lower():
                Print(f"The full form is {elements[i]}",bcolors.WARNING)
            else:
                Print(f"The short form is {shortForms[i]}",bcolors.WARNING)
        i += 1
    Print("Completed",bcolors.OK)
    if out:
        Print(f"Resets: {resets}",bcolors.OK if resets == 0 else bcolors.FAIL)
    else:
        Print(f"Correct: {Totalcorrect}",bcolors.OK if Totalcorrect >= till-1 else bcolors.FAIL)


if __name__ == "__main__":
    start = int(input("Start from element : "))
    till = int(input("till element number: "))
    till = min(till,118)
    out = True if input("Restart on wrong: y or n[default]: ") == "y" else False
    elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorous', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
    shortForms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
    play(elements,shortForms,start,till,out)

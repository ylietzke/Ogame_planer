# Definieren der Methoden
def main():
    # user bekommt hallo
    printWelcome()
    # user wird nach Stufe metall mine gefragt
    # user gibt richtige nummer ein
    # metall mine wird berechnet
    handleMetall()
    # user wird nach Stufe kristall mine gefragt
    # user gibt richtige nummer ein
    # kristall mine wird berechnet
    handleKristall()
    #user wird verabschiedet
    printGoodBye()

def handleMetall():
    userInput = getUserInputMetall()
    if isValidInput(userInput):
        produktion = calc_metallmine(userInput)
        printMetallMine(userInput, produktion)
    else:
        printErrorLimitMetallMine()
        main()

def handleKristall():
    userInput = getUserInputKristall()
    if isValidInput(userInput):
        produktion = calc_kristallmine(userInput)
        printKristallMine(userInput, produktion)
    else:
        printErrorLimitKristallMine()
        main()

def calc_metallmine(Stufe_Metallmine):
    return 30 * int(Stufe_Metallmine) * 1.1 ** int(Stufe_Metallmine)        #Formel Energieverbrauch

def calc_kristallmine(Stufe_Kristallmine):
    return 20 * int(Stufe_Kristallmine) * 1.1 ** int(Stufe_Kristallmine)    #Formel Energieverbrauch

def getUserInputMetall():
    return input("Bitte nenne mir die aktuelle Stufe deiner Metallmine:")

def getUserInputKristall():
    return input("Bitte nenne mir die aktuelle Stufe deiner Kristallmine:")

def isValidInput(Stufe_Metallmine):
    if not Stufe_Metallmine.isnumeric():
        return False
    return (int(Stufe_Metallmine) > 0 and int(Stufe_Metallmine) <= 100)

def isValidInput(Stufe_Kristallmine):
    if not Stufe_Kristallmine.isnumeric():
        return False
    return (int(Stufe_Kristallmine) > 0 and int(Stufe_Kristallmine) <= 100)

def printWelcome():
    print ("Willkommen im Ogame Kalkulator.")

def printMetallMine(StufeMetallMine, ProduktionMetallmine):
    print ("Deine aktuelle Metallmine ist Stufe " + str(StufeMetallMine)) 
    print ("Die Produktion pro Stunde deiner Metallmine beträgt auf der aktuellen Stufe " + str(ProduktionMetallmine))

def printKristallMine(StufeKristallMine, ProduktionKristallmine):
    print ("Deine aktuelle Kristallmine ist Stufe " + str(StufeKristallMine))
    print ("Die Produktion pro Stunde deiner Kristallmine beträgt auf der aktuellen Stufe " + str(ProduktionKristallmine))

def printErrorLimitMetallMine():
    print ("Die Eingabe muss eine Zahl zwischen 1 und 100 sein und darf keine Buchstaben enthalten. ")

def printErrorLimitKristallMine():
    print ("Die Eingabe muss eine Zahl zwischen 1 und 100 sein und darf keine Buchstaben enthalten.")

def printGoodBye():
    print ("Vielen Dank, bis zum nächsten Mal!")

# Hier gehts weiter

# Ausführen der Methoden
main()


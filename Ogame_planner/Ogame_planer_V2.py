# Definieren der Methode

def main():
    # user bekommt hallo
    printWelcome()
    # user wird nach Stufe Metallmine gefragt
    # user gibt korrekte nummer an
    # stufe wird angegeben
    handleMetallmine()
    # user wird nach Stufe Kristallmine gefragt 
    # user gibt korrekte nummer an
    # stufe wird angegeben
    handleKristallmine()
    # user wird nach eingestelltem prozentsatz gefragt
    # user gibt prozentsatz in zehntelschritten zwischen 0.0 und 1.0 an
    # prozentsatz wird angegeben
    handleEingestellterProzentsatz()
    # user wird nach Geologen ja/nein gefragt
    # user gibt ja oder nein an
    # wenn ja: Multiplikator 1.1 , wenn nein Multiplikator: 1.0 -> Multiplikator wird angegeben
    handleGeologe()
    # user wird nach item gefragt
    # user gibt item an: metall/kristall
    # user gibt item an
    handleItem()
    # user wird nach bronze(10%)/silber(20%)/gold(30%) gefragt 
    # wenn Bronze: Multiplikator 1.1; wenn silber: Multipl. 1.2; wenn gold: Multipl. 1.3 -> user gibt Stufe an
    # item + bronze/silber/gold wird angegeben
    statusItem()
    # user wird nach Stufe Plasmatechnik gefragt
    # Die Metallproduktion steigt um 1%, die Kristallproduktion um 0,66% und die Deuteriumproduktion um 0,33% pro Ausbaustufe der Plasmatechnik. 
    # user gibt nummer der Stufe an
    # Stufe wird angegeben 
    #handlePlasmatechnik()
    # user wird nach universum gefragt
    # user gibt universum an 
    # je nach universum wird Geschwindigkeitsfaktor angegeben (Geschwindigkeitsfaktor beträgt normalerweise 1, in den Speedwelten 2,4 oder 5)
    #handleUniversum()
    # Produktion Metallmine wird berechnet => Produktion pro Stunde = ABRUNDEN(30 * STUFE * 1,1 ^ STUFE * "eingestellter Prozentsatz" * Geologe * Item + Grundproduktion) * ((100 + 1 * Stufe Plasmatechnik)/100) * Geschwindigkeitsfaktor
    # Produktion Metallmine wird angegeben
    # Energieverbrauch Metallmine wird berechnet => Energieverbrauch = AUFRUNDEN(10 * STUFE * 1,1 ^ STUFE * "eingestellter Prozentsatz")
    # Energieverbrauch Metallmine wird angegeben
    #outputMetallmine()
    # Produktion Kristallmine wird berechnet => Produktion pro Stunde = ABRUNDEN(20 * STUFE * 1,1 ^ STUFE * "eingestellter Prozentsatz" * Geologe * Item) * ((100 + 0,66 * Stufe Plasmatechnik)/100) * Geschwindigkeitsfaktor)
    # Produktion Kristallmine wird angegeben
    # Energieverbrauch Kristallmine wird berechnet => Energieverbrauch = AUFRUNDEN(10 * STUFE * 1,1 ^ STUFE * "eingestellter Prozentsatz")
    # Energieverbrauch Kristallmine wird angeben
    #outputKristallmine()
    # user wird verabschiedet
    printGoodBye()

def handleMetallmine():
    userInputMM = getUserInputMetall()
    if isValidInputMM(userInputMM):
        printMetallMine(userInputMM)
    else:
        printErrorLimitMetallMine()
        handleMetallmine()
        
def handleKristallmine():
    userInputKM = getUserInputKristall()
    if isValidInputKM(userInputKM):
        printKristallMine(userInputKM)
    else:
        printErrorLimitKristallMine()
        handleKristallmine()

def handleEingestellterProzentsatz():
    userInputEP = getUserInputEingestellterProzentsatz()
    if isValidInputEP(userInputEP):
        printEingestellterProzentsatz(userInputEP)
    else:
        printErrorLimitEingestellterProzentsatz()
        handleEingestellterProzentsatz()

def handleGeologe():
    userInputG = getUserInputGeologe()
    if isValidInputG(userInputG):
        printGeologe(userInputG)
    else:
        printErrorLimitGeologe()
        handleGeologe()
    
def handleItem():
    userInputItem = getUserInputItem()
    if isValidInputItem(userInputItem):
        printItem(userInputItem)
    else:
        printErrorLimitItem()
        handleItem()

def statusItem():
    userInputSI = getUserInputSI()
    if isValidInputSI(userInputSI):
        printSI(userInputSI)
    else:
        printErrorLimitSI()
        statusItem()
#def handlePlasmatechnik():
    
#def handleUniversum():

#def outputMetallmine():

#def outputKristallmine():

#def calc_metallmine(Stufe_Metallmine):
 #   return 30 * int(Stufe_Metallmine) * 1.1 ** int(Stufe_Metallmine)        #Formel Produktion Metallmine

#def calc_kristallmine(Stufe_Kristallmine):
 #   return 20 * int(Stufe_Kristallmine) * 1.1 ** int(Stufe_Kristallmine)    #Formel Produktion Kristallmine

#def ev_metallmine(Stufe_Metallmine):
 #   return 10 * int(Stufe_Metallmine) * 1.1 ** int(Stufe_Metallmine)        #Formel Energieverbrauch Metallmine

#def ev_kristallmine(StufeKristallMine):
 #   return 10 * int(StufeKristallMine) * 1.1 ** int(StufeKristallMine)      #Formel Energieverbrauch Kristallmine

def getUserInputMetall():
    return input("Bitte nenne mir die aktuelle Stufe deiner Metallmine:")

def getUserInputKristall():
    return input("Bitte nenne mir die aktuelle Stufe deiner Kristallmine:")

def getUserInputEingestellterProzentsatz():
    return input("Bitte nenne mir den aktuellen eingestellten Prozentsatz auf der jeweiligen Welt. Gib hier eine Dezimalzahl im Bereich von 0.0 und 1.0 an:")

def getUserInputGeologe():
    return input("Besitzt du einen Geologen, dann beantworte mit ja oder nein:")

def getUserInputItem():
    return input("Gib hier 'Metall' ein, wenn du ein Metall-Item besitzt oder 'Kristall', wenn du ein Kristall-Item besitzt:")

def getUserInputSI():
    return input("Gib hier den Status deines Items an: Bronze, Silber oder Gold:")

def isValidInputMM(Stufe_Metallmine):
    if not Stufe_Metallmine.isnumeric():
        return False
    return (int(Stufe_Metallmine) > 0 and int(Stufe_Metallmine) <= 100)

def isValidInputKM(Stufe_Kristallmine):
    if not Stufe_Kristallmine.isnumeric():
        return False
    return (int(Stufe_Kristallmine) > 0 and int(Stufe_Kristallmine) <= 100)

def isValidInputEP(Eingestellter_Prozentsatz):
    if not Eingestellter_Prozentsatz.isnumeric():
        return False
    return (float(Eingestellter_Prozentsatz) >= 0 and float(Eingestellter_Prozentsatz) <= 1)    #Im Terminal kann noch keine Dezimalzahl angegeben werden

def isValidInputG(Geologe):
    if not Geologe.isalpha():
        return False
    return (str(Geologe) == "ja" or str(Geologe) == "JA" or str(Geologe) == "Ja" or str(Geologe) == "jA")                                                                     # ja = 1.1 setzen

def isValidInputItem(Item):
    if not Item.isalpha():
        return False
    return (str(Item) == "Metall" or str(Item) == "metall" or str(Item) == "Kristall" or str(Item) == "kristall")

def isValidInputSI(StatusItem):
    if not StatusItem.isalpha():
        return False
    return(str(StatusItem) == "Bronze" or str(StatusItem) == "Silber" or str(StatusItem) == "Gold")
        
def printWelcome():
    print ("Willkommen im Ogame Kalkulator.")

def printMetallMine(StufeMetallMine):
    print ("Deine aktuelle Metallmine ist Stufe " + str(StufeMetallMine)) 
    
def printKristallMine(StufeKristallMine):
    print ("Deine aktuelle Kristallmine ist Stufe " + str(StufeKristallMine))

def printEingestellterProzentsatz(EingestellterProzentsatz):
    print ("Dein aktueller eingestellter Prozentsatz beträgt " + str(EingestellterProzentsatz))
    
def printGeologe(GeologeJa):
    print ("Der durch den Geologen zugeführte Multiplikator beträgt " + "1.1")

def printItem(Item):
    if str(Item) == "Metall" or str(Item) == "metall":
        print ("Sie haben ein Metall-Item gewählt.") 
    elif str(Item) == "Kristall" or str(Item) == "kristall":
        print ("Sie haben ein Kristall-Item gewählt.")

def printSI(StatusItem):
    if str(StatusItem) == "Bronze" or str(StatusItem) == "bronze":
        print ("Du hast ein Bronze-Item angegeben. Demnach wird die Produktion um 10 % gesteigert.")
    elif str(StatusItem) == "Silber" or str(StatusItem) == "silber":
        print("Du hast ein Silber-Item angegeben. Demnach wird die Produktion um 20 % gesteigert.")
    elif str(StatusItem) == "Gold" or str(StatusItem) == "gold":
        print("Du hast ein Gold-Item angegeben. Demnach wird die Produktion um 30 % gesteigert.")

def printErrorLimitMetallMine():
    print ("Die Eingabe muss eine Zahl zwischen 1 und 100 sein und darf keine Buchstaben enthalten. ")

def printErrorLimitKristallMine():
    print ("Die Eingabe muss eine Zahl zwischen 1 und 100 sein und darf keine Buchstaben enthalten.")

def printErrorLimitEingestellterProzentsatz():
    print ("Deine Eingabe muss eine Dezimalzahl zwischen 0.0 und 1.0 mit einer Stelle nach dem Komma enthalten. Achte auch darauf, dass du einen Punkt verwendest!")

def printErrorLimitGeologe():
    print ("Die Eingabe darf entweder 'ja' oder 'nein' sein!")

def printErrorLimitItem():
    print ("Die Eingabe darf entweder 'Metall' oder 'Kristall' sein!")

def printErrorLimitSI():
    print ("Die Eingabe darf entweder 'Bronze', 'Silber' oder 'Gold' sein!")

def printGoodBye():
    print ("Vielen Dank, bis zum nächsten Mal!")

# Ausführen der Methode
main()
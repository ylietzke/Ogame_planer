print ("Willkommen im Ogame-Kalkulator!")

def calc_kristallmine():
    stufe = input ("Bitte nenne mir die aktuelle Stufe deiner Kristallmine:")
    
    if stufe.isnumeric():
        print ("Deine aktuelle Metallmine ist " + stufe)
        produktion = 30 * int(stufe) * 1.1 ** int(stufe)
        print ("Hier ist deine aktuelle Kristallproduktion:")
        print (produktion)
    elif len(stufe)>0 and len(stufe)<=99:
        print ("Deine aktuelle Metallmine ist " + stufe)
        produktion = 30 * int(stufe) * 1.1 ** int(stufe)
        print ("Hier ist deine aktuelle Kristallproduktion:")
        print (produktion)
    elif stufe.isalpha() and len(stufe)>=100:
        print ("Bitte gib eine Zahl zwischen 1 und 99 an!")
        calc_kristallmine()
    else:
        print ("Bitte gib eine Zahl zwischen 1 und 99 an!")
        calc_kristallmine()
    
calc_kristallmine()

print ("Mit dem folgenden Kalkulator kan...")


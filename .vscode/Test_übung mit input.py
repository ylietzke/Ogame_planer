def task1():
    print ("Welcome to the Y-Test! If you pass the test, you'll get a massage tonight. If not, Y will get it. You have to write the answers like they're written in the tasks!!! Enjoy!")
    print ("This is the first question. Please write down Y's first name, like it's written in his passport.")
    answer = input("Type yannick or yannick-reinhardt here and hit 'Enter'.").lower()
    if answer == "yannick" or answer == "y":
      print ("You are right. Now you can go on with the next question!")
    else:
      print ("You're absolutely wrong! Sir Yannick Lietzke will be happy to get the massage!")
      task1()


    print ("Here is the second question:")
    print ("What color have Y's eyes?")
    answer = input("Type blue , green , grey or blue-green here and hit 'Enter'.").lower()
    if answer == "blue" or answer == "b":
      print ("You are right. Now you can go on with the next question!")
    elif answer == "blue-green" or answer == "bg":
      print ("This answer is not completely correct but okay. You can go on with the next question!")
    else:
      print ("You're absolutely wrong! Sir Yannick Lietzke will be happy to get the massage!")
      task1()


    print ("Here is your next question:")
    print ("How tall is Y?")
    answer = input("Type 1,92m or 1,93m or 1,94m here and hit 'Enter'.")
    if answer == "1,93m" or answer == "193cm":
        print ("Congratulations! This answer is correct. You can go on now with the next question!")
    elif answer == "1,92m" or answer == "192cm":
        print ("Congratulations! This answer is correct. You can go on now with the next question!")
    else:
        print ("You're absolutely wrong! Sir Yannick Lietzke will be happy to get the massage!")
        task1()
    
    print ("Here is your fourth question:")
    print ("On which day is Y's birthday in June?")
    answer = input("Type 8th , 9th or 10th like it is written here and hit 'Enter'.")
    if answer == "8th":
        print ("Congratulations! This answer is also correct. There is just one question left!")
    else:
        print ("You're absolutely wrong! Sir Yannick Lietzke will be happy to get the massage!")
        task1()

    print ("Here is your last question. Let's hope you will make this too!")
    print ("In which year was Y finished in school and starting in the army?")
    answer = input("Type 2011 , 2012 , 2013 , 2014 here and hit 'Enter'.")
    if answer == "2013":
        print ("Good job! You answered all the questions right. Enjoy your massage!")
    else:
        print ("You're absolutely wrong! Sir Yannick Lietzke will be happy to get the massage!")
        task1()
    print ("You're now finished with the test!")
task1()




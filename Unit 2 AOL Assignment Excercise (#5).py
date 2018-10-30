import math #Need to import math so we can calculate square root

run = "Y"

while run == "Y":

    program = ""
    while program != "QP" and program != "TIP" and program != "TEMP": #Defensive coding which makes sure the user enters one of the 3 options
        program = input("Which program would you like to run? (QP,Tip,Temp): ")
        program = program.upper() #We use upper to account for the user entering in lowercase/mixed case

    if program == "QP":
        int1 = int(input("\nEnter number 1: "))
        int2 = int(input("Enter number 2: "))

        int1 = int1 * int1 #Calculate the square of the integers
        int2 = int2 * int2

        hypotenuse = math.sqrt(int1 + int2) #Use the square root function
        hypotenuse = str(round(hypotenuse, 2)) #Convert answer to string for easy printing

        print("The hypotenuse is %s" % hypotenuse)

    elif program == "TIP":
        bill = float(input("\nEnter bill price: "))
        tip = int(input("Enter tip amount (as an integer): "))
        tip = float(tip/100) #Convert the tip to a decimal so we can multiply it with the bill price

        tip_left = bill * tip
        tip_left = str(round(tip_left, 2))
        bill = str(round(bill, 2))

        print("You should leave a tip of $%s on a bill of $%s" % (tip_left, bill))

    else:
        temp_type = input("\nWhich type of temperature are you entering? (c or f): ")
        temp_type = temp_type.upper()
        temp = float(input("Enter temperature: "))

        if temp_type == "C":
            converted = (temp*(9/5)) + 32 #Use the formula with the temperature the user inputted
            converted = str(round(converted, 2))
            temp = str(round(temp, 2))

            print("%s degrees celsius is %s degrees fahrenheit" % (temp, converted))

        else: #Same thing just with a different formula
            converted = (temp-32)/(9/5)
            converted = str(round(converted, 2))
            temp = str(round(temp, 2))

            print("%s degrees fahrenheit is %s degrees celsius" % (temp, converted))


    run = input("\nWould you like to pick a program again? (type y/n): ").upper() #If the user enters anything other than y then the program ends
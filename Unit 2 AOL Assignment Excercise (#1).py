limit = 50
speed = int(input("Enter car speed in KM: ")) #Takes car speed as user input from keyboard as integer


#Check where the speed falls and tell them how much over the limit they are if necessary
if speed <= 50:
    print("\nYou are driving at/below the speed limit!") #Put \n to print a blank line for formatting purposes

elif (speed > 50) and (speed <=70):
    print("\nYou are %d KM over the limit and will be fined $45!" % (speed-limit))

elif (speed >= 71) and (speed <= 80):
    print("\nYou are %d KM over the limit and will be fined $75!" % (speed-limit))

else:
    print("\nYou are %d KM over the limit and will be fined $150" % (speed-limit))



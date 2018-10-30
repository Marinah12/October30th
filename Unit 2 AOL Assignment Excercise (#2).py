wins = 0

for i in range(6):
    result = input("Did the player win or lose game %d: " % (i+1)) #Print out which game they are on, add 1 to i since it starts at 0

    if result.capitalize() == "W": #Capitalize the input to account for lowercase and uppercase
        wins += 1

#Check how many wins the player got and print out what group they got put into
if wins > 4:
    print("\nThe player won %d games and will be put into Group 1!" % wins)

elif (wins > 2) and (wins < 5):
    print("\nThe player won %d games and will be put into Group 2!" % wins)

elif (wins > 0) and (wins <3):
    print("\nThe player won %d games and will be put into Group 3!" % wins)

else:
    print("\nThe player had a rough showing winning no games, they are eliminated!")

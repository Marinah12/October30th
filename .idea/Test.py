import random
import math

pokemon = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"] #Pokemon Options

bulbasaur_stats = [152, 111, 111, 106] #HP, Attack, Defense, Speed
charmander_stats = [146, 114, 104, 128]
squirtle_stats = [160, 117, 108, 140]
pikachu_stats = [155, 118, 109, 136]

bulbasaur_moves = ["vine whip", "tackle", "growl"] #String representation of the attack names
bulbasaur_moves_types = ["G", "N", "N"] #Type of move eg: G = grass, N = normal

charmander_moves = ["ember", "scratch", "growl"]
charmander_moves_types = ["F", "N", "N"]

squirtle_moves = ["Water Gun", "tackle", "growl"]
squirtle_moves_types = ["W", "N", "N"]

pikachu_moves = ["Thunder Shock", "Quick Attack", "growl"]
pikachu_moves_types = ["E", "N", "N"]

bulbasaur_moves_effects = [45, 40, .1] #Damage/modifier that goes along with the move
charmander_moves_effects = [40, 40, .1]
squirtle_moves_effects = [40,40, .1]
pikachu_moves_effects = [40,40, .1]

for i in range(4):
    print(pokemon[i])

user_pokemon = input("\nPick your Pokemon: ").title() #.title makes the first character capitalized ie: ball ---> Ball
user_stats = 0
opponent_stats = 0
if user_pokemon == "Bulbasaur":
    user_stats = bulbasaur_stats
    user_type = "G"
    user_moves = bulbasaur_moves
    user_moves_types = bulbasaur_moves_types
    user_moves_effects = bulbasaur_moves_effects

if user_pokemon == "Charmander":
    user_stats = charmander_stats
    user_type = "F"
    user_moves = charmander_moves
    user_moves_types = charmander_moves_types
    user_moves_effects = charmander_moves_effects

if user_pokemon == "Squirtle":
    user_stats = squirtle_stats
    user_type = "W"
    user_moves = squirtle_moves
    user_moves_types = squirtle_moves_types
    user_moves_effects = squirtle_moves_effects

if user_pokemon == "Pikachu":
    user_stats = pikachu_stats
    user_type = "L"
    user_moves = pikachu_moves
    user_moves_types = pikachu_moves_types
    user_moves_effects = pikachu_moves_effects

opponent_pokemon = user_pokemon

while opponent_pokemon == user_pokemon: #Make sure the opponent Pokemon is different than user pokemon
    opponent_pokemon = input("\nPick opponent Pokemon: ").title()

if opponent_pokemon == "Bulbasaur":
    opponent_stats = bulbasaur_stats
    opponent_type = "G"
    opponent_moves = bulbasaur_moves
    opponent_moves_types = bulbasaur_moves_types
    opponent_moves_effects = bulbasaur_moves_effects


elif opponent_pokemon == "Charmander":
    opponent_stats = charmander_stats
    opponent_type = "F"
    opponent_moves = charmander_moves
    opponent_moves_types = charmander_moves_types
    opponent_moves_effects = charmander_moves_effects

elif opponent_pokemon == "Squirtle":
    opponent_stats = squirtle_stats
    opponent_type = "W"
    opponent_moves = squirtle_moves
    opponent_moves_types = squirtle_moves_types
    opponent_moves_effects = squirtle_moves_effects

else:

    opponent_stats = pikachu_stats
    opponent_type = "L"
    opponent_moves = pikachu_moves
    opponent_moves_types = pikachu_moves_types
    opponent_moves_effects = pikachu_moves_effects


if opponent_stats[3] > user_stats[3]: #Compare Pokemon speeds to determine who gets to attack first
    first = "O" #Use letters to keep track of who goes first so we can use it with battle loop

else:
    first = "U"

battle = True

while battle == True: #Battle goes on until one persons health is below 0

    count = 0
    while count < 2 and battle == True: #We need to let each Pokemon have a turn, if one pokemon faints after the first turn then we don't need the 2nd turn
        if count == 0 and first == "U" or count == 1 and first == "O": #Use this to determine whose turn it in

            for i in range(3): #Print out which moves the user can pick from
                print("\n", i, ": ", user_moves[i])

            move = int(input("\nPick move: "))
            move_type = user_moves_types[move] #Determine move type, ie: vine whip would be "G" for grass move
            move_damage = user_moves_effects[move]
            #This damage formula is the one used in the real pokemon games
            damage = ((25 * move_damage * (user_stats[1] / opponent_stats[2])) / 50) * ((random.randint(85, 100) / 100.0))  # user_stats[1] = attack stat, opponent_stats[2] = defense stat

        else:
            move = random.randint(0, 2) #Have the move the opponent uses be random, this should give the user a significant advantage
            move_type = opponent_moves_types[move]
            move_damage = opponent_moves_effects[move]
            print("\n%s used %s!" %(opponent_pokemon, opponent_moves[move]))
            damage = ((25 * move_damage * (opponent_stats[1] / user_stats[2])) / 50) * ((random.randint(85, 100) / 100.0))  # opponent_stats[1] = attack stat, user_stats[2] = defense stat

        if move != 2: #The 3rd move is one that alters stats instead of doing damage so we know we can ignore this next step if they use that


            critical_hit = random.randint(0,99) #In pokemon there is a 6% random chance the attack does double damage
            if critical_hit < 6: #We calculate a number between 0 and 99, if it is less than 6 we determine its a critical hit
                print("\nCRITICAL HIT!")
                damage = damage * 2 #If it is a critical hit we double the damage

            if move_type == "G" and opponent_type == "F": #Account for weakness, in this scenario grass is not effective vs fire so the damage is halved
                damage = damage * 0.5

            elif move_type == "F" and opponent_type == "G":
                damage = damage * 2

            elif move_type == "G" and opponent_type == "W":
                damage = damage * 2

            elif move_type == "W" and opponent_type == "G":
                damage = damage * 0.5

            elif move_type == "W" and opponent_type == "F":
                damage = damage * 2

            elif move_type == "F" and opponent_type == "W":
                damage = damage * 0.5

            elif move_type == "L" and opponent_type == "W":
                damage = damage * 2

            elif move_type == "L" and opponent_type == "G":
                damage = damage * 0.5

            if count == 0 and first == "U" or count == 1 and first == "O":
                opponent_stats[0] = opponent_stats[0] - damage #Update opponent health
                print("\n%s has %d health remaining!" % (opponent_pokemon, math.ceil(opponent_stats[0] * 100)/100)) #Use Math.ceil to round
                if opponent_stats[0] <= 0:
                    battle = False

            else:
                user_stats[0] = user_stats[0] - damage #Update user health

                print("\n%s has %d helth remaining!" % (user_pokemon, math.ceil(user_stats[0] * 100)/100))
                if user_stats[0] <= 0:
                    battle = False
        else: #The attack growl lowers the attack stat of the other Pokemon by a percentage
            if count == 0 and first == "U" or count == 1 and first == "O": #Determine whos turn it is
                opponent_stats[1] = opponent_stats[1] * (1 - move_damage) #Lower attack of opponent
                print("%s had it's attack lowered!" % (opponent_pokemon))

            else:
                user_stats[1] = user_stats[1] * (1 - move_damage)
                print("%s had it's attack lowered!" % (user_pokemon))

        count = count + 1 #Update which turn we are on

if user_stats[0] <= 0: #Figure out who won by checking health
    print("\n%s has no HP remaining and has fainted!" % (user_pokemon))

else:
    print("\n%s has no HP remaining and has fainted!" %(opponent_pokemon))
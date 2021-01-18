'''
Handels Spend phase
'''
import hud as h
import random as r

def feed_crew(food, crew):
    '''
    Feed crew
    '''

    # set food_consumed equal to number of crew
    food_consumed = crew

    # remove the food consumed from the supply and display results
    food -= food_consumed

    # if the player has food remaining after feeding the crew display food consumed 
    # otherwise skip to loss on food end of game message
    if food > 0:

        print(f"Your crew consumes {food_consumed} units of food.")
        print("")

    return food

def crystal_burn(power):
    '''
    Check for crystal burnout
    '''

    # create variables good, burned, and burn_rate
    good = 0
    burned = 0
    burn_rate = 20

    # for each power crystal roll d100 
    for b in range(0, int(power)):

        roll = r.randint(1, 100)

         # if result is equal or less than burn_rate add +1 burned
        if roll <= burn_rate:

            burned += 1

        # if not add +1 good
        elif roll > burn_rate:

            good += 1

    # set power equal to good
    power = good

    # print and return results
    print(f"{str(burned)} of your power crystals have burned out!")
    print('')

    return power


def spend_fuel(fuel):
    '''
    Spend fuel and move ship
    '''

    # begin fueling loop
    fueling = True
    while fueling:

        # get user input
        print("How much fuel will you spend?")
        print('')
        print("Spend 1 fuel to move 1 distance.")
        print("Spent 3 fuel to move 2 distance.")
        print("Spend 6 fuel to move 3 distance.")
        print("Spent 10 fuel to move 4 distance.")
        print("Spend 15 fuel to move 5 distance.")
        print('')
        amount = input()

        # if user input is valid set fule_spent and distance_traveled amounts
        if amount == '1':
            fuel_spent = 1
            distance_traveled = 1

        elif amount == '3':
            fuel_spent = 3
            distance_traveled = 2

        elif amount == '6':
            fuel_spent = 6
            distance_traveled = 3    

        elif amount == '10':
            fuel_spent = 10
            distance_traveled = 4

        elif amount == '15':
            fuel_spent = 15
            distance_traveled = 5

        # if input is not valid print error message and restart loop
        else:
            print("command is invalid please input 1, 3, 6, 10, or 15.")
            print("")
            continue

        # if fuel spent is greater than fuel restart loop
        if fuel_spent > fuel:

            print("You do not have that much fuel.")
            print('')
            continue

        # if fuel spent is not greater than fuel restart break loop
        else:

            break
    # adjust fule and distance totals
    fuel -= fuel_spent
    
    # print user's choice
    print("")
    print(f"You have spent {fuel_spent} fuel.")
    print(f"You will travel {distance_traveled} during the travel phase.")  
    print("")

    return fuel, distance_traveled


def spend_phase(fuel, food, power, hull, crew, morale, g_dist, distance):
    '''
    Spends resources during the spend phase
    '''

    # phase intro message
    print("Press ENTER to begin the Spend Phase!")
    input()

    # spend food
    food = feed_crew(food, crew)

    if food > 0:

        # check for crystal burnout
        power = crystal_burn(power)

    if (food > 0) and (power > 0) and (fuel > 0):

            # display HUD
            h.hud(fuel, food, power, hull, crew, morale)

            # display distance
            h.status(distance, g_dist)

            # spend fuel
            fuel, distance_traveled = spend_fuel(fuel)

    # if player has fuel set distance traveled to 1 to avoid out of fuel loss message
    # if player has no fuel
    else:

            if fuel > 0:

                distance_traveled = 1

            else:

                distance_traveled = 0

    return fuel, food, power, hull, crew, morale, distance_traveled

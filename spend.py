import random

def spend_fuel(fuel, distance):
    '''
    Spend fuel and move ship
    '''

    fueling = True

    while fueling == True:

        print("How much fuel do you want to spend?")
        print('')
      
        print("a) Spend 1 fuel move 1 distance.")
        print("b) Spent 3 fuel move 2 distance.")
        print("c) Spend 6 fuel move 3 distance.")
        print("d) Spent 10 fuel move 4 distance.")
        print('')

        amount = input()

        if amount == "a":
            fuel_spent -= 1
            distance_traveled -= 1       

        elif amount == "b":
            fuel -= 3
            distance -= 2
            fueling = False
       
        elif amount == "c":
            fuel -= 6
            distance -= 3
            fueling = False

        elif amount == "d":
            fuel -= 10
            distance -= 4
            fueling = False

        else:
            print("command is invalid please input A, B, C, or D.")
            print("")

    return fuel, distance

def spend_food(food, crew):

    cooking = True

    # begin food  spending loop
    while cooking == True:

        print("You have ")
        print('')
        print("How will you ration you food?")
        print('')
        print("a) Abundance  - spend 2X crew food. (Morale + 10)")
        print("b) Sufficient - spend 1X crew food.")
        print("c) Meger - spend .5X crew food. (Morale - 10)")
        print("d) Fasting - spend 0 food. (-1 crew, and -20 morale)")

        catering = input()

        # check for bad input
        if catering in ('a','b','c','d'):


            # assign food_consumed ammount based on selection
            if catering == 'a':

                food_consumed = int(crew) * 2

            elif catering == 'b':

                food_consumed = int(crew)

            elif catering == 'c':

                food_consumed = int(crew/2)

            elif catering == 'd':

                food_consumed = 0

            # Check that food_consumed is less than total food if it is reduce food by food consumed
            if food_consumed <= food:

                # adjust food, morale, and crew
                if catering == 'a':

                    food -= food_consumed
                    morale += 10

                elif catering == 'b':

                    food -= food_consumed

                elif catering == 'c':

                    food -= food_consumed
                    morale -= 10

                elif catering == 'd':

                    food -= food_consumed
                    morale -= 20
                    crew -= 1


            # if food consumed grater than food display error message and restart loop
            else:

                print("You do not have enough food for this option.")
                continue

            

            # stop loop
            break

        # if input is bad display error message and restart loop
        else: 
            
            print("Invalid entry. Please enter 'a' 'b' 'c' or 'd'.)
            continue





def spend(fuel, food, power, hull, crew, morale, distance):
    '''
    Spends resources during the spend phase
    '''

    # phase intro message 
    print("This is the spend phase.")
    print("During this phase you will:")
    print("Spend fuel to move the ship closer to home")
    print("Spend food to keep crew alive")
    print("determine if any of your power crystals have burnt out")
    print('')

    # spend fuel
    fuel, distance = spend_fuel(fuel, distance)

    # spend food
    food, crew = spend_food(food, crew)

    # check for crystal burnout
    power = burnout(power)

    return fuel, food, power, hull, crew, morale, distance
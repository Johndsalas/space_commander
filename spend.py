import random
import hud as h

# Beginning Values
fuel = 30
food = 50
power = 10
hull = 5
crew = 10
burn_rate = 10
morale = 100
distance = 20
day = 10


# def spend_food(food, crew, morale):
#     '''
#     Spend food
#     '''

#     cooking = True

#     # begin food spending loop
#     while cooking == True:

#         print(f"You have {food} total food")
#         print('')
#         print("How will you ration you food?")
#         print('')
#         print("a) Abundantly  - spend 2X crew food. (Morale + 10)")
#         print("b) Sufficiently - spend 1X crew food.")
#         print("c) Megerly - spend .5X crew food. (Morale - 10)")
#         print("d) Sparingly - spend 0 food. (-1 crew, and -20 morale)")
#         print('')

#         catering = input()

#         # assign food_consumed ammount based on selection
#         # if selection is invalid restart loop
#         if catering == 'a':

#             food_consumed = int(crew) * 2
#             morale_change = 10
#             crew_change = 0

#         elif catering == 'b':

#             food_consumed = int(crew)
#             morale_change = 0
#             crew_change = 0

#         elif catering == 'c':

#             food_consumed = round(int(crew)/2)
#             morale_change = -10
#             crew_change = 0

#         elif catering == 'd':

#             food_consumed = 0
#             morale_change = -20
#             crew_change = 1

#         else:
        
#             print("Invalid entry. Please enter a, b, c, d.")
#             continue

#         # check if food is grater or equal to food_consumed
#         # if it is adjust totals, print results, and break loop
#         # if not display error and restart loop

#         if food >= food_consumed:

#             food -= food_consumed
#             morale += morale_change
#             crew -= crew_change

#             print(f"You have spent {food_consumed} food.")
#             print(f"Morale has changed by {morale_change}.")
#             print('')
            
#             if crew_change > 0:

#                 print("You have lost 1 crew!!!")
#                 print('')

#             cooking = False
     
#         else:

#             continue

#     return food, crew, morale

def feed_crew(food, crew):
    '''
    Feed crew if possible. If not remove starved crew members
    '''

    # set food_consumed equal to number of crew
    food_consumed = crew

    # if there is enough food to feed the crew, remove the food consumed from the supply and display results
    if food_consumed <= food:

        food -= food_consumed

        print(f"Your crew consumes {food_consumed} units of food.")
        print(f'You have {food} units of food remaining.')
        print("")

    # if there is not enough food to feed the crew, remove all food from the supply and remove starved crew and dislpay results
    elif food_consumed > food:

        crew_starved = crew - food

        crew -= crew_starved

        print(f"You only had enough food to feed {food} of your crew.")
        print(f"{crew_starved} of your crew have starved.")
        print("")

        food = 0

    return crew, food


def crystal_burn(power,burn_rate):
    '''
    Check for crystal burnout
    '''

    good = 0
    burned = 0

    # for each power crystal roll d100 
    # if result is equal or less than burn_rate add +1 burned
    # if not add +1 good
    for r in range(0,int(power)):

        roll = random.randint(1,100)

        if roll <= burn_rate:

            burned += 1

        elif roll > burn_rate:

            good += 1

    # set power equal to good 
    power = good

    # print and return results
    print(f"{str(burned)} of your power crystals have burned out!")
    print(f"You have {str(power)} crystals remaning.")
    print('')

    return power, burn_rate




def spend_fuel(fuel, distance):
    '''
    Spend fuel and move ship
    '''
    fueling = True

    # begin fueling loop
    while fueling:

        # get user input
        print("How much fuel do you want to spend?")
        print('')
      
        print("a) Spend 1 fuel to move 1 distance.")
        print("b) Spent 3 fuel to move 2 distance.")
        print("c) Spend 6 fuel to move 3 distance.")
        print("d) Spent 10 fuel to move 4 distance.")
        print('')

        amount = input()

        # if user input is valid set fule_spent and distance_traveled amounts and end loop
        # if not print error message and restart loop
        if amount == "a":
            fuel_spent = 1
            distance_traveled = 1    
            break

        elif amount == "b":
            fuel_spent = 3
            distance_traveled = 2 
            break
       
        elif amount == "c":
            fuel_spent = 6
            distance_traveled = 3    
            break

        elif amount == "d":
            fuel_spent = 10
            distance_traveled = 4  
            break

        else:
            print("command is invalid please input a, b, c, or d.")
            print("")
            continue

    # adjust fule and distance totals
    fuel -= fuel_spent
    distance -= distance_traveled

     # print user's choice
    print(f"You have spent {fuel_spent} fuel.")
    Print(f"You will traveled {distance_traveled} during the travel phase.")  
    print("")

    return fuel, distance


def spend(fuel, food, power, hull, crew, burn_rate, morale, distance):
    '''
    Spends resources during the spend phase
    '''

    # phase intro message 
    print("Begin Production phase!")
    print("")

    h.hud(fuel, food, power, hull, crew, morale)

    # spend food
    food, crew = feed_crew(food, crew)

    # check for crystal burnout
    power, burn_rate = crystal_burn(power, burn_rate)

    # spend fuel
    fuel, distance = spend_fuel(fuel, distance)

    return fuel, food, power, hull, crew, burn_rate, morale, distance

spend(fuel, food, power, hull, crew, burn_rate, morale, distance)
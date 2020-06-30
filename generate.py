import random

def gen(fuel, food, power, hull, crew, morale):
    '''
    Generate resources once during each turn 
    '''

    # number of crew assigned to each resource
    fuel_crew = 0
    food_crew = 0
    power_crew = 0
    hull_crew = 0
    morale_crew = 0

    # pelalty to production chance for each reasorce
    fuel_pen = 0
    food_pen = 0
    power_pen = 0
    hull_pen = 0
    morale_pen = 0

    # chance to produce each reasorce 
    fuel_chance = (morale - fuel_pen)
    food_chance = (morale - food_pen)
    power_chance = (morale - power_pen)
    hull_chance = (morale - hull_pen)
    morale_chance = (morale - morale_pen)

    # number of resorces produced on success
    fuel_prod = 1
    food_prod = 3
    power_prod = 1
    hull_prod = 1
    morale_prod = 5

    print("Beginning Production Phase!!!")
    print('')
    print(f"Your total crew is {crew}.")
    print(f"Each crew assigned to fuel has a {fuel_chance}% chance to produce {fuel_prod} fuel.")
    print(f"Each crew assigned to power has a {power_chance}% chance to produce {power_prod} power crystals.")
    print(f"Each crew assigned to hull has a {hull_chance}% chance to repair {hull_prod} damage to the hull.")
    print(f"Each crew assigned to morale has a {morale_chance}% chance to improve the crew's morale by {morale_prod}%.")
    print('')

    while 1>0:

        print("How many crew members will you assign to fuel.") 
        fuel_crew = input()

        print("How many crew members will you assign to food.")
        food_crew = input()

        print("How many crew members will you assign to power.")
        power_crew = input()

        print("How many crew members will you assign to hull.")
        hull_crew = input()

        print("How many crew members will you assign to morale.")
        morale_crew = input()

        print('')

        if fuel_crew.isdigit() == True and food_crew.isdigit() == True and power_crew.isdigit() == True and hull_crew.isdigit() == True and morale_crew.isdigit() == True:

            assigned = int(fuel_crew) + int(food_crew) + int(power_crew) + int(hull_crew) + int(morale_crew)

            if assigned <= crew:

                crew_check = True
                
                while crew_check:
            
                    print(f"You have assigned {fuel_crew} crew to fuel.") 
                    print(f"You have assigned {food_crew} crew to food.")
                    print(f"You have assigned {power_crew} crew to power.")
                    print(f"You have assigned {hull_crew} crew to hull.")
                    print(f"You have assigned {morale_crew} crew to fuel.")
                    print('')

                    if assigned < crew:

                        print("You have not assigned all of your crew members!!!")
                        print('')

                    print("Proceed with the current assignment? (y/n)")
                    print('')
                    acknowledge = input()

                    if acknowledge in ('y','n'):
                        break

                    else:
                        
                        print("Invalid command please type 'y' or 'n")
                        print('')
                
                if acknowledge == 'y':

                    # define resources generated 
                    fuel_gen = 0
                    food_gen = 0
                    power_gen = 0
                    hull_gen = 0
                    morale_gen = 0
                    
                    # calculate resorces generated this turn
                    # for each crew assigned to a resorce roll a 100 sided die
                    # if that die rolls at or below resource_chance add resource_prod to resorce_gen

                    # Fuel
                    for r in range(0, int(fuel_crew)):

                        if int(random.randrange(1,101)) <= fuel_chance:

                            fuel_gen += fuel_prod
                
                    # Food
                    for r in range(0, int(food_crew)):

                        if int(random.randrange(1,101)) <= food_chance:

                            food_gen += food_prod
                            
                    # Power
                    for r in range(0, int(power_crew)):

                        if int(random.randrange(1,101)) <= power_chance:

                            power_gen += power_prod
                            
                    # Hull
                    for r in range(0, int(hull_crew)):

                        if int(random.randrange(1,101)) <= hull_chance:

                            hull_gen += hull_prod
                            
                    # Morale
                    for r in range(0, int(morale_crew)):

                        if int(random.randrange(1,101)) <= morale_chance:

                            morale_gen += morale_prod

                    # add generated resources to total resource
                    fuel += fuel_gen
                    food += food_gen
                    power += power_gen
                    hull += hull_gen
                    morale += morale_gen

                    # Check for resource caps

                    if hull > 5:

                        print("Hull cannot exceed 5")
                        print('')
                        hull = 5

                    if morale > 100:

                        print("morale cannot exceed 100")
                        morale = 100

                    # end loop
                    break

                elif acknowledge == 'n':

                    print("Reasign your crew.")

            elif assigned > crew:

                print(f"Number of crew member's assigned exceeds total number of crew. you may only assign a total of {crew} crew")

        else:

            print("Invalid Command please input only numbers during this phase.")

    # display resoures generated this turn
    print('')
    print(f"Fuel generated this turn: {fuel_gen} ")
    print(f"Food generated this turn: {food_gen}")
    print(f"Power generated this turn: {power_gen}")
    print(f"Hull generated this turn: {hull_gen}")
    print(f"Morale generated this turn: {morale_gen}")
    print('')

    return fuel, food, power, hull, crew, morale
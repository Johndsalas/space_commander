import hud as h
import random as r

def assign_crew():

    # get input for crew assigned to fuel
    print("How many crew members will you assign to fuel?")
    
    fuel_crew = input()
    print(fuel_crew)

    # get imput for crew assigned to food
    print("How many crew members will you assign to food?")
    
    food_crew = input()
    print(food_crew)

    # get imput for crew assigned to power
    print("How many crew members will you assign to power crystals?")
    
    power_crew = input()
    print(power_crew)

    # get imput for crew assigned to hull
    print("How many crew members will you assign to hull?")

    hull_crew = input()
    print(hull_crew)

    # get imput for crew assigned to morale
    print("How many crew members will you assign to morale?")
    
    morale_crew = input()
    print(morale_crew)

    # print space between next block of text
    print('')

    return fuel_crew, food_crew, power_crew, hull_crew, morale_crew


def check_crew_assignment(fuel_crew, food_crew, power_crew, hull_crew, morale_crew, crew):

    # Check for non-numeric input
    if not (fuel_crew.isdigit() and food_crew.isdigit() and power_crew.isdigit() and hull_crew.isdigit() and morale_crew.isdigit()):

        # if non-numeric input is found propt user and return false
        print("Input is incorrect. Please input only numbers")
        print("")
        return False

    else:

        # get total of assigned crew
        assigned = int(fuel_crew) + int(food_crew) + int(power_crew) + int(hull_crew) + int(morale_crew)

        # if assigned crew > crew prompt user and return false
        if assigned > crew:

            print("You assigned too many crew members.")
            print("")
            return False

        # if assigned crew <= crew 
        else:

            # display crew assignments
            print(f"You have assigned {fuel_crew} crew to fuel.") 
            print(f"You have assigned {food_crew} crew to food.")
            print(f"You have assigned {power_crew} crew to power.")
            print(f"You have assigned {hull_crew} crew to hull.")
            print(f"You have assigned {morale_crew} crew to morale.")
            print('')

            # if assigned crew < crew display warning
            if assigned < crew:

                print("You have not assigned all of your crew members!!!")
                print('')

            # create loop to ask if user wishes to proceed with the current selection
            crew_check = True

            while crew_check:

                # prompt user for verification and get input
                print("Proceed with the current assignment? (y/n)")
                print('')
                acknowledge = input()

                # if input is not valid restart the loop
                if acknowledge not in('y', 'n'):

                    print("Invalid command please type 'y' or 'n")
                    print('')
                    continue

                # if y return True
                if acknowledge == 'y':

                    return True

                # if n return False
                elif acknowledge == 'n':

                    return False

def generate(fuel_crew, food_crew, power_crew, hull_crew, morale_crew, fuel_chance, food_chance, power_chance, hull_chance, morale_chance, fuel_prod, food_prod, power_prod, hull_prod, morale_prod):

    # define resources generated
    fuel_gen = 0
    food_gen = 0
    power_gen = 0
    hull_gen = 0
    morale_gen = 0

    # calculate resorces generated this turn
    # for each crew assigned to a resource roll a 100 sided die
    # if that die rolls at or below resource_chance add resource_prod to resorce_gen

    # Fuel
    for c in range(0, int(fuel_crew)):

        if r.randint(1,100) <= fuel_chance:

            fuel_gen += fuel_prod

    # Food
    for c in range(0, int(food_crew)):

        if r.randint(1,100) <= food_chance:

            food_gen += food_prod
            
    # Power
    for c in range(0, int(power_crew)):

        if r.randint(1,100) <= power_chance:

            power_gen += power_prod
            
    # Hull
    for c in range(0, int(hull_crew)):

        if r.randint(1,100) <= hull_chance:

            hull_gen += hull_prod
            
    # Morale
    for c in range(0, int(morale_crew)):

        if r.randint(1,100) <= morale_chance:

            morale_gen += morale_prod

    # display generated resources
    print(f"Fuel generated: {fuel_gen} ")
    print(f"Food generated: {food_gen}")
    print(f"Power Crystals generated: {power_gen}")
    print(f"Hull repaired: {hull_gen}")
    print(f"Morale generated: {morale_gen}")
    print('')

    return fuel_gen, food_gen, power_gen, hull_gen, morale_gen


def is_capped(fuel, food, hull, power, morale):

     # Check for resource caps
    if fuel > 40:

        print("You can only store up to 40 fuel")
        print('')
        fuel = 40

    if food > 50:

        print("You can only store up to 50 food")
        print('')
        food = 50

    if hull > 6:

        print("Hull cannot exceed 5")
        print('')
        hull = 6

    if power > 15:

        print("You can only store up to 15 power crystals")
        print('')
        power = 15

    if morale > 100:

        print("morale cannot exceed 100")
        print('')
        morale = 100

    return fuel, food, hull, power, morale


def production_phase(fuel, food, power, hull, crew, morale):
    '''
    Generate resources
    '''

    # number of crew assigned to each resource
    fuel_crew = 0
    food_crew = 0
    power_crew = 0
    hull_crew = 0
    morale_crew = 0

    # set additional amount subtracted from morale during prodiction test
    fuel_pen = 15
    food_pen = 0
    power_pen = 10
    hull_pen = 20
    morale_pen = 0

    # chance to produce each reasorce
    fuel_chance = (morale - fuel_pen)
    food_chance = (morale - food_pen)
    power_chance = (morale - power_pen)
    hull_chance = (morale - hull_pen)
    morale_chance = (morale - morale_pen)

    # number of resorces produced on success
    fuel_prod = 3
    food_prod = 5
    power_prod = 3
    hull_prod = 1
    morale_prod = 5

    # display information for the beginning of the production phase
    print("Press ENTER to begin the Production Phase!")
    input()
    print('')

    h.hud(fuel, food, power, hull, crew, morale)

    print(f"You mas assign {crew} crew members to produce resources")
    print('')
    print(f"Each crew assigned to fuel has a {fuel_chance}% chance to produce {fuel_prod} fuel.")
    print(f"Each crew assigned to food has a {food_chance}% chance to produce {food_prod} food.")
    print(f"Each crew assigned to power has a {power_chance}% chance to produce {power_prod} power crystals.")
    print(f"Each crew assigned to hull has a {hull_chance}% chance to repair {hull_prod} damage to the hull.")
    print(f"Each crew assigned to morale has a {morale_chance}% chance to improve the crew's morale by {morale_prod}%.")
    print('')

    # create loop for assigning crew
    giving_orders = True

    while giving_orders:

        # assign crew to resources
        fuel_crew, food_crew, power_crew, hull_crew, morale_crew = assign_crew()

        # Check for valid input and user validation
        if check_crew_assignment(fuel_crew, food_crew, power_crew, hull_crew, morale_crew, crew):
            break
    
    # get generated resources and display them
    fuel_gen, food_gen, power_gen, hull_gen, morale_gen = generate(fuel_crew, food_crew, power_crew, hull_crew, morale_crew, fuel_chance, food_chance, power_chance, hull_chance, morale_chance, fuel_prod, food_prod, power_prod, hull_prod, morale_prod)        
    
    # add generated resources to total resource
    fuel += fuel_gen
    food += food_gen
    power += power_gen
    hull += hull_gen
    morale += morale_gen

    # check for capped resources
    fuel, food, hull, power, morale = is_capped(fuel, food, hull, power, morale)

    return fuel, food, power, hull, crew, morale

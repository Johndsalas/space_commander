def assign_crew():

    # get input for crew assigned to fuel
    print("How many crew members will you assign to fuel.")
    fuel_crew = input()

    # get imput for crew assigned to food
    print("How many crew members will you assign to food.")
    food_crew = input()

    # get imput for crew assigned to power
    print("How many crew members will you assign to power.")
    power_crew = input()

    # get imput for crew assigned to hull
    print("How many crew members will you assign to hull.")
    hull_crew = input()

    # get imput for crew assigned to morale
    print("How many crew members will you assign to morale.")
    morale_crew = input()

    # print space between next block of text
    print('')

    return fuel_crew, food_crew, power_crew, hull_crew, morale_crew

assign_crew()
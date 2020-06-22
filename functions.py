
def rules_text():
    '''
    Displays rules text
    '''
    print("These are the rules!")
    print('')
    print("Press 'enter' to continue.")
    print('')
    input()


def hud(fuel, food, power, hull, crew, moral, distance,day):
    '''
    Heads up display for game stats
    '''
    print(" _____")
    print("|{:^5}|".format("Day"))
    print("|{:^5}|".format(day))
    print(" -----")
    print(" ____________________________________________")
    print("|{:^6}|{:^6}|{:^7}|{:^6}|{:^6}|{:^8}|".format("Fuel", "Food", "Power", "Hull", "Crew", "Morale"))
    print("|{:^6}|{:^6}|{:^7}|{:^6}|{:^6}|{:^8}|".format(fuel, food, power, hull, crew, moral))
    print(" --------------------------------------------")
    print("")
    print(" ____________________")
    print("|{:^20}|".format("Remaining Distance"))
    print("|{:^20}|".format(distance))
    print(" --------------------")
    print("")

def gen(fuel, food, power, hull, crew, morale, distance):

    # fuel_crew = 0
    # food_crew = 0
    # power_crew = 0
    # hull_crew = 0
    # morale_crew = 0

    # print("This is the generation phase. In this phase you will assign crew members to generate resorces (fuel, food, power, hull, crew, morale).")
    # print('')
    # print(f"Your total crew is {crew}.")
    # print('')

    # while gathering == True:

    #     print("How many crew members will you assign to fuel.")
    #     fuel_crew = input()

    #     print("How many crew members will you assign to food.")
    #     food_crew = input()

    #     print("How many crew members will you assign to power.")
    #     power_crew = input()

    #     print("How many crew members will you assign to hull.")
    #     hull_crew = input()

    #     print("How many crew members will you assign to morale.")
    #     morale_crew = input()

    #     if fuel_crew + food_crew + power_crew + hull_crew + morale_crew = crew:
            
    #         print(f"You have assigned {fuel_crew} crew to fuel.") 
    #         print(f"You have assigned {food_crew} crew to food.")
    #         print(f"You have assigned {power_crew} crew to power.")
    #         print(f"You have assigned {hull_crew} crew to hull.")
    #         print(f"You have assigned {morale_crew} crew to fuel.")

    

    return fuel, food, power, hull, crew, morale, distance

def fuel(fuel, distance):
    '''
    Gets input for fule usage changes fule amount and distance
    '''
   
    print("How much fuel do you want to spend today?")
    print("")

    fueling = True

    while fueling == True:
      
        print("a) Spend 1 fuel move 1 distance.")
        
        if fuel > 3:
            print("b) Spent 3 fuel move 2 distance.")

        if fuel > 6: 
            print("c) Spend 6 fuel move 3 distance.")

        if fuel > 10:
            print("d) Spent 10 fuel move 4 distance.")

        print("")

        amount = input()

        if amount == "a":
            fuel -= 1
            distance -= 1       
            fueling = False

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

def event(fuel, food, power, hull, crew, morale, distance):

    print("This is the event phase. Events happen in this phase")
    input()

    return fuel, food, power, hull, crew, morale, distance

def loss(fuel, food, hull, crew, morale, running):

    if fuel < 1:
        print("You have lost due to running out of fuel!")
        running = False
        return running
    if food < 1:
        print("You have lost due to running out of food!")
        running = False
        return running
    if hull < 1:
        print("You have lost due to running out of hull!")
        running = False
        return running
    if crew < 1:
        print("You have lost due to running out of crew!")
        running = False
        return running
    if morale < 1:
        print("You have lost due to running out of morale!")
        running = False
        return running
    else:
        running = True
        return running

def win(distance, running):

    if distance < 1:
        print("You have won the game!!!")
        running = False
        return running
    else:
        running = True
        return running
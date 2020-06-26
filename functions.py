
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
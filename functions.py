
def rules_text():
    '''
    Displays rules text
    '''
    print("These are the rules!")
    print('')
    print("Press 'enter' to continue.")
    print('')
    input()


def hud(fuel, food, power, hull, crew, moral, distance):
    '''
    Heads up display for game stats
    '''
    
    print(" ____________________________________________")
    print("|{:^6}|{:^6}|{:^7}|{:^6}|{:^6}|{:^8}|".format("Fuel", "Food", "Power", "Hull", "Crew", "Morale"))
    print("|{:^6}|{:^6}|{:^7}|{:^6}|{:^6}|{:^8}|".format(fuel, food, power, hull, crew, moral))
    print(" --------------------------------------------")
    print("")
    print(" ____________________")
    print("|{:^20}|".format("Remaining Distance"))
    print("|{:^20}|".format(distance))
    print(" --------------------")


def hud(fuel, food, power, hull, crew, morale, distance,day):
    '''
    Heads up display for game stats
    '''
    print('')
    print(" ______________________________________")
    print("|{:^38}|".format(" Days Until the Garquackien Invasion!"))
    print("|{:^38}|".format(day))
    print(" --------------------------------------")
    print(" _____________________________________________________")
    print("|{:^6}|{:^6}|{:^16}|{:^6}|{:^6}|{:^8}|".format("Fuel", "Food", "Power Crystals", "Hull", "Crew", "Morale"))
    print("|{:^6}|{:^6}|{:^16}|{:^6}|{:^6}|{:^8}|".format(fuel, food, power, str(hull)+'/5', crew, str(morale)+'%'))
    print(" -----------------------------------------------------")
    print(" ____________________")
    print("|{:^20}|".format("Remaining Distance"))
    print("|{:^20}|".format(distance))
    print(" --------------------")
    print("")


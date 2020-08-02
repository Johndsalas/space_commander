

def hud(fuel, food, power, hull, crew, morale, distance, day):
    '''
    Heads up display for game stats
    '''

    print(" _____________________________________________________")
    print("|{:^6}|{:^6}|{:^16}|{:^6}|{:^6}|{:^8}|".format("Fuel", "Food", "Power Crystals", "Hull", "Crew", "Morale"))
    print("|{:^6}|{:^6}|{:^16}|{:^6}|{:^6}|{:^8}|".format(fuel, food, power, str(hull)+'/5', crew, str(morale)+'%'))
    print(" -----------------------------------------------------")

def travel(distance, day):

    print('')
    print(" _____________________________________")
    print("|{:^37}|".format(" Days Until the Garquackien Invasion"))
    print("|{:^37}|".format(day))
    print(" -------------------------------------")
    print(" _____________________")
    print("|{:^21}|".format("Distance from Earth"))
    print("|{:^21}|".format(distance))
    print(" ---------------------")
    print("")

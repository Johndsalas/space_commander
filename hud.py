


def hud(fuel, food, power, hull, crew, morale, distance,day):
    '''
    Heads up display for game stats
    '''
    print('')
    print(" _____")
    print("|{:^5}|".format("Day"))
    print("|{:^5}|".format(day))
    print(" -----")
    print(" ____________________________________________")
    print("|{:^6}|{:^6}|{:^7}|{:^6}|{:^6}|{:^8}|".format("Fuel", "Food", "Power", "Hull", "Crew", "Morale"))
    print("|{:^6}|{:^6}|{:^7}|{:^6}|{:^6}|{:^8}|".format(fuel, food, power, str(hull)+'/5', crew, str(morale)+'%'))
    print(" --------------------------------------------")
    print(" ____________________")
    print("|{:^20}|".format("Remaining Distance"))
    print("|{:^20}|".format(distance))
    print(" --------------------")
    print("")
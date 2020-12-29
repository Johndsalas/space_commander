

def hud(fuel, food, power, hull, crew, morale):
    '''
    Heads up display for game stats
    '''

    print(" ________________________________________________________")
    print("|{:^7}|{:^7}|{:^16}|{:^7}|{:^6}|{:^8}|".format("Fuel", "Food", "Power Crystals", "Hull", "Crew", "Morale"))
    print("|{:^7}|{:^7}|{:^16}|{:^7}|{:^6}|{:^8}|".format(str(fuel)+'/40', str(food)+'/60', str(power)+'/15', str(hull)+'/5', crew, str(morale)+'%'))
    print(" --------------------------------------------------------")
    print("")

def status(distance, week):

    print('')
    print(" __________________________________")
    print("|{:^34}|".format("Garquackians distance from Earth"))
    print("|{:^34}|".format(week))
    print(" ----------------------------------")
    print(" __________________________")
    print("|{:^26}|".format("Your distance from Earth"))
    print("|{:^26}|".format(distance))
    print(" --------------------------")
    print("")

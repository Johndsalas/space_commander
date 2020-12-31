'''
Create boxes for displaying resource and distance information
'''

def hud(fuel, food, power, hull, crew, morale):
    '''
    display for resources
    '''

    # display each resource in its own box with current and max number of that resource underneth it
    print(" ________________________________________________________")
    print("|{:^7}|{:^7}|{:^16}|{:^7}|{:^6}|{:^8}|".format("Fuel", "Food", "Power Crystals", "Hull", "Crew", "Morale"))
    print("|{:^7}|{:^7}|{:^16}|{:^7}|{:^6}|{:^8}|".format(str(fuel)+'/40', str(food)+'/60', str(power)+'/15', str(hull)+'/6', crew, str(morale)+'%'))
    print(" --------------------------------------------------------")
    print("")

def status(distance, g_dist):
    '''
    display for distances
    '''
    # display garquackian's current distance from Earth
    print(" __________________________________")
    print("|{:^34}|".format("Garquackian's distance from Earth"))
    print("|{:^34}|".format(g_dist))
    print(" ----------------------------------")
    # display player's current distance from Earth
    print(" __________________________")
    print("|{:^26}|".format("Your distance from Earth"))
    print("|{:^26}|".format(distance))
    print(" --------------------------")
    print("")


def rules_text():
    '''
    Displays rules text
    '''
    print("In space command you take on the role of a spaceship capton who's vessel has ben lost in enemy space.")
    print("During game play you will descide how to best manage your ships resources including it's crew, fuel, power, food, and morale.")
    print("How you manage these reasources will determin wether you and your crew make it home alive.")
    print('')
    input("Press any key to continue.")

    print("Resources")
    print("---------")
    print('')
    print("CREW: During the production phase you will assign your crew to produce resources your ship.")
    print('')
    print("FOOD: Each day during the allocation phase you will spend food to feed your crew.")
    print("      The ammount you spend will have an effect on the ship's morale of your ship and your total number of crew.")
    print('')
    print("POWER: Your ship is powered my power crystals that supply a large amount of energy, but are unstable.")
    print("       Each power crystal in your supply has a chance of burning out each day.")
    print("       This is checked during the allocation phase.")
    print("       If you ever have less than 1 power crystal in your supply, your ship will lose life support and you will lose the game.")
    print('')
    print("FUEL: Each day during the allocation phase you will be able to spend fuel in order to more the ship.")
    print("      The the amount of distance moved is determined by how much fuel is spent.")
    print('')
    print("MORALE: When crew are assigned to produce resources during the production phase the chance that they are successful is dependent on the ship's morale.")
    print("        Higher morale means higher chance of success. Lower morale means a lower chance of success.")
    print("        If your ship's morale ever reaches 0. Your crew has been overcome by dispare or anarchy, and you have lost the game.")
    print('')
    input("Press any key to continue.")

    print("Other Game Terms")
    print("----------------")
    print('')

    print("The game takes place in three phases.")
    print("The Production Phase")
    print("The Allocation Phase")
    print("The Event Phase")
    print('')
    input("Press any key to continue.")

    print("During the event phase you will assign crew members to the production of resources that your ship will need to complete it's journy.")
    print("Each crew member assigned to resource has a chance to create more of that resource.
    print("The chance is equal to the morale of the ship minus the difficulty of producing that resource.")
    print("successful crew members will produce an amount of that resource equal to the peoduction value of that resource.")
    print("Chance to produce and production value will be displayed when you make your choice.")
    print('')
    input("Press any key to continue.")




def menu():

    print("Welcome to space commander.")
    print("press 'enter' to continue.")

    input()

    menu = True

    # begin loop for menu
    while menu == True:

        # display choices
        print("What would you like to do?")
        print('')
        print("a) See Rules. (suggested for first time players)")
        print("b) Play Game!!!")
        print("c) Exit Game")
        print("")

        # store user input
        selection = input()

        # if a show rules and continue loop
        if selection == 'a': 
            rules_text()
        
        # if 2 stop menu loop and begin game loop
        elif selection == 'b':
            running = True
            menu = False
            

        # if 3 turn off menu loop and game loop to get to exit
        elif selection == 'c':
            running = False
            menu = False

        # if other give invalad command prompt and continue loop
        else: 
            print("Command is invalid please enter a, b, or c.")
            print('')

    return running
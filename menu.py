
def rules_text():
    '''
    Displays rules text
    '''
    print("In space command you take on the role of a spaceship capton who's vessel has ben lost in enemy space.")
    print("During game play you will descide how to best manage your ships resources including it's crew, fuel, power, food, hull, and morale.")
    print("How you manage these reasources will determin wether you and your crew make it home alive.")
    print('')
    input("Press any key to continue.")

    print("Winning and Losing")
    print("------------------")
    print("If DISTANCE is reduced to 0 and you make it to the Home Phase of the game you win!!!")
    print('')
    print("If CREW, POWER, HULL or MORALE are ever reduced to 0 you lose the game!!!")

    print("Losing")

    print("Resources")
    print("---------")
    print('')
    print("CREW: During the production phase you will assign your crew to produce resources your ship.")
    print('')
    print("FOOD: Each day during the allocation phase you will spend food to feed your crew.")
    print("      The ammount you spend will have an effect on the crew's morale and wellbeing .")
    print('')
    print("POWER: Your ship is powered my power crystals that supply a large amount of energy, but are unstable.")
    print("       Each power crystal in your supply has a chance of burning out each day.")
    print('')
    print("FUEL: Each day during the allocation phase you will be able to spend fuel in order to more the ship.")
    print("      The the amount of distance moved is determined by how much fuel is spent.")
    print('')
    print("Hull: Represents the ships hull integrity. Crew assigned to generate hull will repaire a portion of the damaged hull if any.")
    print("      Hull cannot be repaired above 5. If hull ever reaches zero the ship falls apart and you lose the game.")
    print('')
    print("MORALE: When crew are assigned to produce resources during the production phase the chance that they are successful is dependent on the ship's morale.")
    print("        Higher morale means higher chance of success. Lower morale means a lower chance of success.")
    print("        Morale cannot be raised above 100%")
    print('')
    input("Press any key to continue.")

    print("Other Game Terms")
    print("----------------")
    print('DAY: Shows the number of days you have been on your journy including the current day.')
    print('')
    print("DISTANCE: Shows the total remaining distance your ship must traveled in order to reach home.")
    print("          If your ship reaches home you win the game!")
    print('')
    input("Press any key to continue.")

    print("Game Phases")
    print("-----------")
    print("HUD phase")
    print("Production Phase")
    print("Allocation Phase")
    print("Event Phase")
    print('')
    input("Press any key to continue.")

    print("HUD Phase")
    print("---------")
    print("Each game round begins with the HUD phase.")
    print("During the HUD phase you will see three displays:")
    print("The first displays the DAY.")
    print("The second shows the amount of each reasource that is in your supply.")
    print("On day one this will reflect your starting supplies.")
    print("On subsaquent days this will reflect resources added or subtracted to your supply based on decitions you make throughout the game.")
    print("The last display will show the total remaining distance your ship will need to move to reach home and winn the game.")
    print("After the HUD phase play proceeds to the production phase")
    print('')
    input("Press any key to continue.")

    print("Production Phase")
    print("----------------")
    print("Each game round begins with the production phase.")
    print("During the production phase you will assign crew members to the production of resources that your ship will need to complete it's journy.")
    print("Resources that can be produced are fuel, power, food, hull, and morale. (See Resources for full discription.)")
    print("Each crew member assigned to resource has a chance to create more of that resource.")
    print("The chance is equal to the crew's morale minus the difficulty of producing that resource.")
    print("successful crew members will produce an amount of that resource equal to the peoduction value of that resource.")
    print("Chance to produce and production value will be displayed when you make your choice.")
    print("After resources are produces they are added to your supply.")
    print('')
    input("Press any key to continue.")

    print("Allocation Phase")
    print("----------------")
    print("The allocation phase takes place in three steps")
    print("Power")
    print("Food")
    print("Fuel")
    print('')
    input("Press any key to continue.")

    print("Power Step")
    print("----------")
    print("During this step the game will check to see if any of your power crystals have burned out.")
    print("Power crystals that burn out are no longer useful and are removed from your supply.")
    print("During this step each of your power crystals have a 15 percent chance of burning out.")
    print("If you ever have less than one power crystal in your supply, the ship will lose power and you will lose the game!")
    print("After the Power step play moves to the Food Step")
    print('')
    input("Press any key to continue.")

    print("Food Step")
    print("---------")
    print("During this phase you will choose from a list of options how to ration your food for the day.")
    print("You may only choose an option if you have enough food in your supply to spend on that option.")
    print("Spending food plentifully will boost morale, but wastes food.")
    print("Spending food frugally will sap morale but will save food in the supply for latter use.")
    print("After the food step play proceeds to the Fuel Step.")
    print('')
    input("Press any key to continue.")

    print("Fuel Step")
    print("---------")
    print("During this step you will choose from a list of options how much fuel to spend that day.")
    print("The more fuel you spend the closer you get to home and winning the game.")
    print("This is shown by a decrease in DISTANCE in your HUD.")
    print("However this will drastically impact the ships fuel effeciency, resulting in needing more total fuel to funish the journy home.")
    print("After the fuel step the allocation phase is complete. Play passes to the Event Phase.")
    print("Note: If this step would cause DISTANCE to become 0 or less you do not will immediatly.")
    print("      You must still survive the upcoming event for the day. If you do you will win the game.")
    print('')
    input("Press any key to continue.")

    print("Event Phase")
    print("-----------")
    print("The Event Phase begins be revealing a random event.")
    print("Events represent complications that you and your crew have encountered.")
    print("Most events will requier you to chose between two or more unplesant options, such as sacrificing some amount of resources or another.")
    print("Once you have made your choice (assuming there is one) the event will adjust your supply as needed to fulfill the event.")
    print("When this is done the Event phase is over and play proceeds to the Home Phase.")

    print("Home Phase")
    print("----------")
    print("During this phase the game checks to see if you have reduced distance to 0 or less.")
    print("If you have the game is over and you have won!")
    print("If you have not the game proceeds back to the HUD phase and a new day begins.")

    print("Days will continue indefinantly looping through each phase until you have won or lost the game.")

    

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
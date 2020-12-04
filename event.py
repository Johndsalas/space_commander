
import hud as h
import random as r

def get_event(fuel, food, power, hull, crew, morale):

    # list of events
    event_list = [  "Gravitational Force",
                    "Over Rationed",
                    "Contamination",
                    "Navigational Malfunction",
                    "Aliens",
                    "Territory Dispute",
                    "Garquackien Fighters",
                    "Room to Grow",
                    "Deterioration",
                    "Asteroids",
                    "Stench",
                    "Despair",
                    "Recreation",
                    "Ware and Tare",
                    "Relations",
                    "Defueling",
                    "Hording",
                    "Stealing",
                    "Blockade",
                    "Dissenters",
                    "Boarded"                   ]

    # create loss variables
    lost_fuel = r.randint(1,10)
    lost_food = r.randint(1,20)
    lost_power = r.randint(1,5)
    lost_hull = r.randint(1,3)
    lost_crew = r.randint(0,3)
    lost_morale = r.randint(1,20)

    # get random event
    event = r.choice(event_list)

    # carryout chosen event (display text, give choice if applocable, modify lost variables, display result text)
    resolving_event = True
    if event == "Gravitational Force":

        print(event)
        print('')
        print("While passing by a large star your ship is caught in its gravitational well.")
        print("You manage to escape, but not without burning through some of your fuel reserves.")
        print("")

        fuel -= lost_fuel

        print(f"You have lost {lost_fuel} fuel.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    elif event == "Over Rationed":

        print(event)
        print('')
        print("You discover that your food reserves have not been rationed correctly. You could use some of ")
        print("your fuel to stop at a nearby planet and restock the missing food or maintain your current course.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Restock: loose 1-10 fuel.")
            print("b) Maintain Course: lose 1-20 food.")
            print("")
            choice = input()

            if choice == "a":

                fuel -= lost_fuel 
                print(f"You have lost {lost_fuel} fuel.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                food -= lost_food
                print(f"You have lost {lost_food} food.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Contamination":
        
        print(event)
        print('')
        print("A strange mold, poisons to humans, has been found growing on some of the ship's food.")
        print("You had to destroy some of the food reserves to prevent the mold from spreading.")
        print("")

        food -= lost_food

        print(f"You have lost {lost_food} food.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    elif event == "Navigational Malfunction":

        print(event)
        print('')
        print("The ship’s navigational system is malfunctioning, causing it to recommend a longer ")
        print("travel route than is necessary. You could use power crystals to feed additional ")
        print("power to the navigation system allowing it to reboot and correct the error ")
        print("immediately, or you could spend fuel to keep the ship on schedule and allow the ")
        print("navigation system to reboot on its own.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Reboot: lose 1-5 power crystals")
            print("b) Stay the Course: lose 1-10 fuel")
            print("")
            choice = input()

            if choice == "a":

                power -= lost_power
                print(f"You have lost {lost_power} power crystals.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                fuel -= lost_fuel
                print(f"You have lost {lost_fuel} fuel.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Aliens":

        print(event)
        print('')
        print("Hostel alien life forms are clinging to your ship disrupting you travel and ")
        print("imperaling your crew. You could lure the creatures away by jettisoning some ")
        print("of your food reserves or use power crystals to create a electric discharge")
        print("strong enough force them off the ship.")
        print("")

        while resolving_event:
            
            print("What are your orders?")
            print("a) Lure Them Away: lose 1-20 food")
            print("b) Force Them Off: lose 1-5 power crystals")
            print("")
            choice = input()

            if choice == "a":

                food -= lost_food
                print(f"You have lost {lost_food} food.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                power -= lost_power
                print(f"You have lost {lost_power} power crystals.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Space Pirates":

        print(event)
        print('')
        print("Your journey requires passage through a hostile region of space. Space Pirates")
        print("controlling this region have placed capture mines throughout it, in the hopes")
        print("of commandeering any ship that happens to blunder into them. These mines emit a sonic")
        print("frequency that shatters power crystals while leaving the rest of the ship intact.")
        print("You manage to avoid most of the mines, but not all of them...")
        print('')

        power -= lost_power

        print(f"You lose {lost_power} power crystals")
        print("")

    elif event == "Garquackien Fighters":

        print(event)
        print('')
        print("Several Garquackien fighter ships have dropped out of hyperspace and are preparing ")
        print("fire on your ship. You cold spent some fuel to engage in evasive maneuvers and avoid")
        print("taking fire or you could maintain your current course which will take you out of their")
        print("range, but not without sustaining some fire.")
        print('')

        while resolving_event:

            print("What are your orders?")
            print("a) Maintain Heading: lose 1-3 hull")
            print("b) Evasive Maneuvers: lose 1-10 fuel")
            print("")
            choice=input()

            if choice == "a":

                hull -= lost_hull
                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                fuel -= lost_fuel
                print(f"You have lost {lost_fuel} fuel.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue
        

    elif event == "Room to Grow":

        print(event)
        print('')
        print("The vegetation you are cultivating for the ship’s food supply, is not yielding the expected")
        print("amount. You could renovate the ship, clearing out our more space for growing food and weakening")
        print("the ship’s hull or you could do nothing and make do with less food.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Renovate: lose 1-3 hull")
            print("b) Don't Renovate: lose 1-20 food")
            print("")
            choice = input()

            if choice == "a":

                hull -= lost_hull
                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                food -= lost_food
                print(f"You have lost {lost_food} food.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Deterioration":

        print(event)
        print('')
        print("The maintenance system that keeps the hull in good repair has malfunctioned. You could use ")
        print("some of your power crystals to fix the damage by powering up some of the ship’s repair bots ")
        print("or you could allow the hull to become damaged.")
        print("")
        
        while resolving_event:

            print("What are your orders?")
            print("a) Repair the ship: lose 1-5 power crystals")
            print("b) Save the Crystals: lose 1-3 hull")
            print("")
            choice = input()

            if choice == "a":

                power -= lost_power

                print(f"You have lost {lost_power} power crystals.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                hull -= lost_hull

                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Asteroids":

        print(event)
        print('')
        print("You find your self in the middle of an asteroid field. As you pilot your")
        print("way out you can hear the sound of space rocks making impacts on your ship.")
        print("")

        hull -= lost_hull

        print(f"You have sustained {lost_hull} damage to the hull.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    elif event == "Stench":

        print(event)
        print('')
        print("Apparently, someone though it would be funny to mix stink fluid with part or your fuel supply.")
        print("When the mixed fuel is burned in the ship’s propulsion system, it fills the ship with a foul ")
        print("smelling odor. You could throw out the 'prank' fuel or endure the stench and the effect it's")
        print("having on the crew’s morale.")
        print("")

        while resolving_event:
            
            print("What are your orders?")
            print("a) Destroy the 'Prank' Fuel: lose 1-10 fuel")
            print("b) Use the 'Prank' Fuel: lose 1-20 morale")
            print("")
            choice = input()

            if choice == "a":

                fuel -= lost_fuel

                print(f"You have lost {lost_fuel} fuel.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                morale -= lost_morale

                print(f"You have lost {lost_morale} morale.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    
    elif event == "Despair":

        print(event)
        print('')
        print("Despondency is beginning to take hold of your crew. You could spend some of your food reserves")
        print("to hold a small calibration and raise the crew’s spirits or do nothing and allow the crew's")
        print("morale to fall.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Hold the Celebration: lose 1-20 food")
            print("b) Don't Hold the Celebration: lose 1-20 morale")
            print("")
            choice = input()


            if choice == "a":

                food -= lost_food

                print(f"You have lost {lost_food} food.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                morale -= lost_morale

                print(f"You have lost {lost_morale} morale.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Recreation":

        print(event)
        print('')
        print("Being confined to a small ship is making the crew restless and ill-tempered. You could")
        print("use some power crystals to open the ship’s recreation facilities and releave some of the")
        print("crew's stress or do nothing and allow the crew's morale to fall.")
        print("")
        

        while resolving_event:

            print("What are your orders?")
            print("a) Open the Recreation Facilities: lose 1-5 power crystals")
            print("b) Conserve Power: lose 1-20 morale")
            choice = input()


            if choice == "a":

                power -= lost_power

                print(f"You have lost {lost_power} power crystals.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                morale -= lost_morale

                print(f"You have lost {lost_morale} morale.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Ware and Tare":

        print(event)
        print('')
        print("The ware of the last mission and this one is taking its toll on the hull of you ship.")
        print("You could choose to build physical fortifications in the ship to prevent the ware from")
        print("worsening. However, the fortifications are bulky and would make an already cramped")
        print("ship feel even more so.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Fortify the Ship: lose 1-20 morale")
            print("b) Don't Fortify the Ship: lose 1-3 hull")
            print("")
            choice = input()

            if choice == "a":

                morale -= lost_morale

                print(f"You have lost {lost_morale} morale.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break
                

            elif choice == "b":

                hull -= lost_hull

                print(f"You sustained {lost_hull} damage to your hull.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Relations":

        print(event)
        print('')
        print("‘Relations’ between two of your senior staff members have soured, turning into open hostility.")
        print("What’s worse is they are encouraging their subornments to take sides. You have done what you can")
        print("to discipline your senior staff. However, there is still a lingering air of disharmony andresentment")
        print("among many of the crew.")

        morale -= lost_morale

        print(f"You have lost {lost_morale} morale.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    elif event == "Defueling":

        print(event)
        print('')
        print("A space pirate vessel is attempting to syphon off some of your ships fule. You could")
        print("use force to overcome the smaller vessel and prevent the theft. However, doing so would")
        print("put the lives of your crew at risk.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Remove the Pirates by Force: lose 0-3 crew")
            print("b) Surrender the Fuel: lose 1-10 fuel")
            print("")
            choice = input()

            if choice == "a":

                crew -= lost_crew

                print(f"You have lost {lost_crew} crew.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                fuel -= lost_fuel

                print(f"You have lost {lost_fuel} units of fuel.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Stealing":

        print(event)
        print('')
        print("You have discovered that several power crystals are missing from the ships supply. It is likely,")
        print("that some of the crew have been ‘appropriating’ them for personal use. You could order a ship")
        print("wide search to recover the missing crystals. However, any crew who are caught stealing in a ")
        print("time of crisis would need to be made swift example of, potentially reducing the number of")
        print("remaining crew.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Search the ship: lose 0-3 crew")
            print("b) Ignore the Missing Crystals: lose 1-5 power crystals")
            print("")
            choice = input()

            if choice == "a":

                crew -= lost_crew

                print(f"You have lost {lost_crew} crew.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                power -= lost_power

                print(f"You have lost {lost_power} power crystals.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Hording":

        print(event)
        print('')
        print("Persistent rumors of food shortages have prompted some of the crew to begin hording food")
        print("You could order a ship wide search to recover the missing food. However, any crew who are")
        print("caught stealing in a time of crisis would need to be made swift example of, potentially")
        print("reducing the number of remaining crew.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Search the Ship: lose 0-3 crew")
            print("b) Ignore the Missing Food: lose 1-20 food")
            print("")
            choice = input()

            if choice == "a":

                crew -= lost_crew

                print(f"You have lost {lost_crew} crew.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                food -= lost_food

                print(f"You have lost {lost_food} food.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Blockade":

        print(event)
        print('')
        print("Some of the Garquackiens have gotten ahead of you and set up a blockade.")
        print("You could send your own fighters to clear out the blockade, risking the")
        print("lives of some of your crew, or ram through the blockade causing damage to")
        print("the hull of your ship.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Deploy the fighters: lose 0-3 crew")
            print("b) Ram Through the Blockade: lose 1-3 hull")
            print("")
            choice = input()

            if choice == "a":

                crew -= lost_crew

                print(f"You have lost {lost_crew} crew.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                hull -= lost_hull

                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Dissenters":

        print(event)
        print('')
        print("Fear and despair among the crew has turned into whispers of dissent in a few of them.")
        print("You could conduct a search for the source of those whispers, make an example of them,")
        print("and put a stop to the negetive effect the are having on the crew's moral. However, ")
        print("this will potentially reduce your number of remaining crew.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Make an Example: lose crew")
            print("b) Ignore the Whispers: lose morale")
            print("")
            choice = input()

            if choice == "a":

                crew -= lost_crew

                print(f"You have lost {lost_crew} crew.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            elif choice == "b":

                morale -= lost_morale

                print(f"You have lost {lost_morale} morale.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "Boarded":

        print(event)
        print('')
        print("Without warning, several Garquackien soldiers beam aboard your ship in an attempt to")
        print("commandeer it. Your crew manages to dispatch the invaders, but not without a fight.")
        
        crew -= lost_crew
        
        print(f"You lost {lost_crew} crew.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    return fuel, food, power, hull, crew, morale


def less_than_zero(fuel, food, power, hull, crew, morale):

    if fuel < 0:
        fuel = 0

    if food < 0:
        food = 0
    
    if power < 0:
        power = 0

    if hull < 0:
        hull = 0

    if crew < 0:
        crew = 0

    if morale < 0:
        morale = 0

    return fuel, food, power, hull, crew, morale

def event_phase(fuel, food, power, hull, crew, morale):
    '''
    
    '''

    # set number of events
    num_events = 2

    # display beginning of phase
    print("Press ENTER to begin the Event Phase!")
    input()
    print("")

    # display hud
    h.hud(fuel, food, power, hull, crew, morale)

    # get events
    for x in range(0,num_events):

        fuel, food, power, hull, crew, morale = get_event(fuel, food, power, hull, crew, morale)

        fuel, food, power, hull, crew, morale = less_than_zero(fuel, food, power, hull, crew, morale)

        if ((fuel == 0) or (food == 0) or (power == 0) or (hull == 0) or (crew == 0) or (morale == 0)):

            break

    return fuel, food, power, hull, crew, morale

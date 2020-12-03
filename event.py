
import hud as h
import random as r

fuel = 100
food = 100
power = 100
hull = 100
crew = 10
morale = 100
distance = 20
week = 10

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
                    "Asteroid Field",
                    "Mixed",
                    "Feast",
                    "Recreation",
                    "Worse",
                    "Relations",
                    "Syphon",
                    "Hording",
                    "Stealing",
                    "Blockade",
                    "Decenters",
                    "Boarded"                     ]

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
        print("your fuel to stop at a nearby planet and restock the missing food or maintain your current ")
        print("course and make do with the missing food. ")
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
        print("travel route than is necessary. You could spend power crystals to feed additional ")
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
        print("controlling this region have placed capture mines throughout the region in the hopes")
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
        print("fire on your ship. You cold spent some of your fuel reserves to engage in evasive ")
        print("maneuvers and avoid taking fire or you could maintain your current course which will ")
        print("soon take you out of their range, but not without sustaining some fire.")
        print('')

        while resolving_event:

            print("What are your orders?")
            print("a) Maintain Heading: lose 1-3 hull")
            print("b) Evasive Maneuvers: lose 1-10 fuel ")
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
        print("the ship’s hull or you could do nothing and make do with the less food.")
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

    elif event == "asteroid_field":

        print(event)
        print('')
        print("Curse that navigation computer, it’s led you straight into an asteroid field. As you begin trying ")
        print("to pilot your way out you can hear the sound of space rocks making an impact on your ship.")
        print("")

        hull -= lost_hull

        print(f"You have sustained {lost_hull} damage to the hull.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    elif event == "mixed":

        print(event)
        print('')
        print("Apparently, someone though it would be funny to mix a stink fluid made from a Scaal sweat")
        print("gland with part or your fuel supply. When the mixed fuel is burned in the ship’s propulsion system,")
        print(" it fills the ship with a smell that is most foul. Having to endure the smell is having a negative")
        print("impact on the crew’s morale. Will you endure the smell is having a negative impact on the crew’s")
        print("morale. Will you continue to use the continue to use the “prank” fuel or will you destroy it.")
        print("")

        while resolving_event:
            
            print("What are your orders?")
            print("a) Jettison the “prank” fuel: lose 1-10 fuel")
            print("b) Continue to use the “prank” fuel: lose 1-20 morale")
            print("")
            choice = input()

            if choice == "a":

                fuel -= lost_fuel

                print(f"You have lost {lost_fuel} units of fuel.")
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

    
    elif event == "feast":

        print(event)
        print('')
        print("Despondency is beginning to take hold of your crew. Reflecting upon the sudden loss of Star Gazer 1,")
        print("the space station they called home, their own dire situation, and the fate of the earth if they should")
        print("fail, has been too much to process. You consider holding a small calibration to raise the crew’s")
        print("spirits. A few hours of food, song, and dancing will keep crew’s mind off of their struggles for")
        print("long enough to restore some of their sanity. However, hosting such an event would require")
        print("dipping into the ship’s food reserve.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Hold the celebration: lose food")
            print("b) Conserve supplies: lose 1-20 morale")
            print("")
            choice = input()


            if choice == "a":

                food -= lost_food

                print(f"You have lost {lost_food} units of food.")
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

    elif event == "recreation":

        print(event)
        print('')
        print("Being confined to a small ship is making the crew restless and ill-tempered. As a result, overall ")
        print("morale has begun to drop. You consider opening the ship’s recreation facilities in the hopes ")
        print("that the illusion of open space will do something to combat the crew’s feeling of confinement.")
        print("opening these facilities will require spending some of the ship’s power crystal supply.")
        print("")
        

        while resolving_event:

            print("What are your orders?")
            print("a) Open the recreation facilities: lose 1-5 power crystals")
            print("b) Conserve power: lose 1-20 morale")
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

    elif event == "worse":

        print(event)
        print('')
        print("After running a diagnostic on the hull of your ship, you discover that much of the damage")
        print("sustained in the attack on Star Gazer 1, is worse than it appears. You could choose to build")
        print("physical fortifications in the ship to prevent the damage from worsening. However, the")
        print("fortifications are bulky and would make an already cramped ship feel even more so. Morale")
        print("could suffer as a result.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Repair the ship: lose 1-20 morale")
            print("b) It’ll hold together: lose 1-3 hull")
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

    elif event == "relations":

        print(event)
        print('')
        print("‘Relations’ between two senior staff members have soured, turning into open hostility. What’s")
        print("worse is they are encouraging their subornment crew members to take sides. You have done")
        print("what you can to discipline your senior staff. However, there is still a lingering air of disharmony")
        print("and resentment among many of the crew.")

        morale -= lost_morale

        print(f"You have lost {lost_morale} morale.")
        print("")
        print("Press ENTER to continue")
        input()
        print('')

    elif event == "syphon":

        print(event)
        print('')
        print("An Eminore pirate vessel has attaches itself to your ship and is beginning to steal its fuel. You")
        print("could use force to overcome the smaller vessel and prevent the theft. However, doing so would ")
        print("put the lives of your crew at risk.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Remove the aliens by force: lose 0-3 crew")
            print("b) We have plenty of fuel: lose 1-10 fuel")
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

    elif event == "stealing":

        print(event)
        print('')
        print("You have discovered that several power crystals are missing from the ships supply. It is likely,")
        print("that some of the crew have been ‘appropriating’ them for personal use. You could order a ship")
        print("wide search to recover the missing crystals. However, any crewmembers who are caught stealing")
        print("in a time of crisis would need to be made swift example of, potentially reducing the number of")
        print("remaining crew. ")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Search the ship: lose 0-3 crew")
            print("b) Ignore the missing crystals: lose 1-5 power crystals")
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

    elif event == "hording":

        print(event)
        print('')
        print("Persistent rumors of food shortages have prompted some of the crew to begin hording food")
        print("You could order a ship wide search to recover the missing food. However, any crewmembers")
        print("who are caught stealing in a time of crisis would need to be made swift example of, potentially")
        print("reducing the number of remaining crewmembers.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Search the ship: lose 0-3 crew")
            print("b) Ignore the missing food: lose 1-20 food")
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

                print(f"You have lost {lost_food} units of food.")
                print("")
                print("Press ENTER to continue")
                input()
                print('')
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "blockade":

        print(event)
        print('')
        print("Some of the Garquackiens have gotten ahead of you and set up a blockade. With no way to")
        print("navigate around it, you are forced to confront the blockade head on. You could send fighters to")
        print("clear out the blockade, risking the lives of some of your crew, or ram through the blockade")
        print("causing damage to the hull of your ship.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Deploy the fighters: lose 0-3 crew")
            print("b) Ramming Speed: lose 1-5 hull")
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

    elif event == "decenters":

        print(event)
        print('')
        print("Fear and despair among the crew has turned into whispers of mutiny from a few them. You")
        print("remain confident that your crew will not betray you. However, such whispering is having a")
        print("negative effect on the crew’s morale. You could conduct a search to round up the whisperers")
        print("and make an example of them. This would put a stop to their whispering and restore morale.")
        print("However, this will potentially reduce the number of remaining crew.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Make an example: lose crew")
            print("b) Confront the whisperers privately: lose morale")
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

    elif event == "boarded":

        print(event)
        print('')
        print("Without warning, several Garquackien soldiers beam aboard your ship in an attempt to")
        print("commandeer it. Your crew manages to dispatch the invaders, but not without a fight.")
        
        crew -= lost_crew
        
        print(f"You lost {lost_crew} crew in during the battle.")
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

event_phase(fuel, food, power, hull, crew, morale)



    
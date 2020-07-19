
# Beginning Values
fuel = 30
food = 50
power = 5
hull = 5
crew = 10
burn_rate = 10
morale = 70
distance = 20
day = 1

import random as r

def event(fuel, food, power, hull, crew, burn_rate, morale, distance):
    '''
    generate a random event for each day
    '''
    # set resolving event to true
    resolving_event = True

    # creare lost variables
    lost_fuel = 0
    lost_food = 0
    lost_power = 0
    lost_hull = 0
    lost_crew = 0
    lost_morale = 0

    # get rndome event
    event_list = ["gravitational_force","restock","contamination","navigational_malfunction","lifeform","magnetic_field","ambush","confined","deterioration","astroid_field","mixed","feast","recreation","spacewalk","relations","syphon","hording","stealing","taking_fire","decenters","boarded"]

    event = r.choice(event_list)

    # print event name
    print(f"{event}")

    # carryout chosen event (display text, give choice if applocable, modify lost variables, display result text)
    if event == "gravitational_force":

        print("Your ship passes by a large star and is nearly caught in its gravity well. ")
        print("Through clever piloting you manage to escape the star’s pull,")
        print("but not without burning through some of your fuel reserves.")
        print("")

        lost_fuel += r.randint(1,10)

        print(f"You have lost {lost_fuel} units of fuel.")
        print("")

    elif event == "restock":

        print("You discover that your food reserves have been stocked to regulation.")
        print("There is a habitable planet not too far from you,")
        print("that you could use to replenish the missing supply.")
        print("However, that would mean spending fuel on the supply run.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Restock supplies: loose 1-10 fuel.")
            print("b) Continue without restocking: lose 1-20 food.")
            print("")
            choice = input()

            if choice == "a":

                lost_food += r.randint(1,10)
                print(f"You have lost {lost_fuel} units of fuel.")
                print("")
                break

            elif choice == "b":

                lost_food += r.randint(1,20)
                print(f"You have lost {lost_food} units of food.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "contamination":
        
        print("A strange mold, poisons to humans, has been found growing on some of the ship's food.")
        print("Some of the ship's food had to be destroyed to keep the mold from spreading.")
        print("")

        lost_food += r.randint(1,20)

        print(f"You have lost {lost_food} units of food.")
        print("")

    elif event == "navigational_malfunction":

        print("The ship’s navigational systems seem to be malfunctioning.")
        print("The system is recommending a longer travel route than is necessary.")
        print("Feeding additional power to the navigation system would allow it to reboot ")
        print("and correct the navigational error, at the cost of power crystals.")
        print("Alternatively, spending additional fuel would keep the ship on schedule")
        print("in spite of the longer route, allowing the navigation system normally ")
        print("scheduled daily bootup.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Feed the navigation system additional power: loose 1-4 power crystals")
            print("b) Spend additional fuel to account for the longer route: loose 1-10 fuel")
            print("")
            choice = input()

            if choice == "a":

                lost_power += r.randint(1,4)
                print(f"You have lost {lost_power} power crystals.")
                print("")
                break

            elif choice == "b":

                lost_fuel += r.randint(1,10)
                print(f"You have lost {lost_fuel} units of fuel.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "lifeform":

        print("Strange alien life forms have begun attaching themselves to your ship.")
        print("They seem to be in search of food, and you are hoping against hope that you and your crew will not become snacks.")
        print("The crew suggests luring the creatures away by jettisoning enough food to get their attention.")
        print("Alternatively, you could use some of your power crystals to create a power surge strong enough to forcibly remove the creatures.")
        print("")

        while resolving_event:
            
            print("What are your orders?")
            print("a) lure creatures away: lose 1-20 food")
            print("b) create power surge: lose 1-5 power crystals")
            print("")
            choice = input()

            if choice == "a":

                lost_food += r.randint(1,20)
                print(f"You have lost {lost_food} units of food.")
                print("")
                break

            elif choice == "b":

                lost_power += r.randint(1,5)
                print(f"You have lost {lost_power} power crystals.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "magnetic_field":

        print("Your ship has encountered a peculiar time-space anomaly.")
        print("While your crew and ship seem largely undisturbed,")
        print("The anomaly is causing your power crystals to burn out at an accelerated rate.")
        print("")

        lost_power += r.randint(1,5)

        print(f"You lose {lost_power} power crystals")
        print("")

    elif event == "ambush":

        print("Several short range Garquackien ships have dropped out of hyperspace ")
        print("and are preparing to fire on your ship!")
        print("At your current speed and heading you will pace them eventually")
        print("but not without sustaining fire.")
        print("Alternatively, you cold spent some extra fuel and avoid the ships entirely.")
        print("")
        
        while resolving_event:

            print("What are your orders?")
            print("a) Maintain current heading: lose 0-3 hull")
            print("b) Evasive Maneuvers: lose 1-10 fuel ")
            print("")
            choice=input()

            if choice == "a":

                lost_hull += r.randint(0,3)
                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                break

            elif choice == "b":

                lost_fuel += r.randint(1,10)
                print(f"You have lost {lost_fuel} units of fuel.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue
           

    elif event == "confined":

        print("The vegetation you are cultivating for the ship’s food supply, ")
        print("is not yielding the expected amount. ")
        print("You believe that this is due to the small space the vegetation is being stored in.")
        print("You could do some renovation to alleviate this concern, however this may signifyingly damage ")
        print("the hull in the process.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) The crew has to eat: lose 0-3 hull")
            print("b) My first duty is to the ship: lose 1-20 food")
            print("")
            choice = input()

            if choice == "a":

                lost_hull += r.randint(0,3)
                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                break

            elif choice == "b":

                lost_food += r.randint(1,20)
                print(f"You have lost {lost_food} units of food.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "deterioration":

        print("Your ship has seen you through some tough situations, however it is beginning to show its age.")
        print("Some of the hull is beginning to deteriorate, fortunately you have discovered some repair")
        print("bots that can stave off the damage long enough to complete the journey. ")
        print("Of course, bots run on power and activating these bots will cost you some of your power ")
        print("crystals.")
        print("")
        
        while resolving_event:

            print("What are your orders?")
            print("a) Repair the ship: lose 1-5 power crystals")
            print("b) It’ll hold together: lose 0-3 hull")
            choice = input()

            if choice == "a":

                lost_power += r.randint(1,5)

                print(f"You have lost {lost_power} power crystals.")
                print("")
                break

            elif choice == "b":

                lost_hull += r.randint(0,3)

                print(f"You have sustained {lost_hull} damage to the hull.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "asteroid_field":

        print("Your route home necessitates the successful navigation through a tricky asteroid field.")
        print("You worry that your ship’s hull may be damaged in the process.")
        print("Upside, the Garquackiens hunting you would be fools to follow you it.")
        print("")

        lost_hull += r.randint(0,3)

        print(f"You have sustained {lost_hull} damage to the hull.")
        print("")

    elif event == "mixed":

        print("Apparently, someone from another ship though it would be funny to mix a stink fluid made ")
        print("from a morokeeze sweat gland with part or your fuel supply.")
        print("When the mixed fuel is used it fills the ship with a smell so fowl its literally making ")
        print("crewmembers sick and is likely to have a significant effect on the crew’s productivity.")
        print("If you make it through this the admiral will be informed of what you thought of the “joke”.")
        print("In the meantime, you must decide what to do with the fuel.")
            
        while resolving_event:
            
            print("What are your orders?")
            print("a) Jettison the contaminated fuel: lose 1-10 fuel")
            print("b) Grin and bare it: lose 1-20 morale")
            print("")
            choice = input()

            if choice == "a":

                lost_fuel += r.randint(1,10)

                print(f"You have lost {lost_fuel} units of fuel.")
                print("")
                break

            elif choice == "b":

                lost_morale += r.randint(1,20)

                print(f"You have lost {lost_morale} morale.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    
    elif event == "feast":

        print("The dire situation facing your crew is beginning to wear on them.")
        print("Many are beginning to fall into despair, and it may begin to affect their performance.")
        print("Your second in command suggests holding a small social event to raise their spirits.")
        print("However, this would require dipping into the food reserves.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print(f"a) Hold the event: lose {crew} food")
            print("b) Conserve supplies: lose 1-20 morale")
            print("")
            choice = input()


            if choice == "a":

                lost_food += crew

                print(f"You have lost {lost_food} units of food.")
                print("")
                break

            elif choice == "b":

                lost_morale += r.randint(1,20)

                print(f"You have lost {lost_morale} morale.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "recreation":

        print("The crew is becoming restless and tempers are flaring as a result.")
        print("Many have begun to request access to the ship’s recreational facilities.")
        print("These facilities require extra power to run ")
        print("and have been left non-operational to conserve power.")
        print("However, the crew’s current mood demands that you reconsider")
        print("opening these areas.")
        print("")
        

        while resolving_event:

            print("What are your orders?")
            print("a) Let the crew have their fun: lose 1-5 power crystals")
            print("b) Conserve power: lose 1-20 morale")
            choice = input()


            if choice == "a":

                lost_power += r.randint(1,5)

                print(f"You have lost {lost_power} power crystals.")
                print("")
                break

            elif choice == "b":

                lost_morale += r.randint(1,20)

                print(f"You have lost {lost_morale} morale.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "spacewalk":

        print("A thorough diagnostic of the ship has revealed that much of the damage, sustained in the initial ")
        print("Garquackien attack, that was thought to be superficial, may turn into significant damage in the ")
        print("future it left unrepaired. Repairing the damage would require some of the crew to do a ")
        print("spacewalk drawing the crew’s attention to just how dire their situation is.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) It’ll hold together: lose 0-3 hull")
            print("b) Repair the ship: lose 1-20 morale")
            print("")
            choice = input()

            if choice == "a":

                lost_hull += r.randint(0,3)

                print(f"You sustained {lost_hull} damage to your hull.")
                print("")
                break

            elif choice == "b":

                lost_morale += r.randint(1,20)

                print(f"You have lost {lost_morale} morale.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue


    elif event == "relations":

        print("‘Relations’ between two senior staff members have soured, resulting in open hostility, and the")
        print("subornment crew being forced to choose sides. You have done your best to address the")
        print("situation however there still lingers a noticeable air of disharmony and resentment among the")
        print("staff.")
        print("")

        lost_morale += r.randint(1,20)

        print(f"You have lost {lost_morale} morale.")
        print("")

    elif event == "syphon":

        print("An unidentified alien vessel has attached itself to your ship and has begun syphoning fuel out of ")
        print("your reserves. The vessel looks small and on a good day, you do not believe it could carry your ")
        print("ships entire fuel supply. However, this is not a good day and your fuel reserves are not near ")
        print("what they should be. You’ve considered using force to remove the alien. However, your ships ")
        print("remaining guns must be operated manually and at great risk to crewmembers assigned to operate them.")
        print("")

        while resolving_event:

            print("What are your orders?")
            print("a) Remove the aliens by force: lose 0-3 crew")
            print("b) We have plenty of fuel: lose 1-10 fuel")
            print("")
            choice = input()

            if choice == "a":

                lost_crew += r.randint(0,3)

                print(f"You have lost {lost_crew} crew.")
                print("")
                break

            elif choice == "b":

                lost_fuel += r.randint(1,20)

                print(f"You have lost {lost_fuel} units of fuel.")
                print("")
                break

            else:

                print("Please enter a or b.")
                print("")
                continue

    elif event == "hording":

        print("")

    elif event == "stealing":

        print("")

    elif event == "taking_fire":

        print("")

    elif event == "decenters":

        print("")

    elif event == "boarded":

        print("")

    fuel -= lost_fuel
    food -= lost_food
    power -= lost_power
    hull -= lost_power
    crew -= lost_crew
    morale -= lost_morale  

    return fuel, food, power, hull, crew, burn_rate, morale, distance

event(fuel, food, power, hull, crew, burn_rate, morale, distance)
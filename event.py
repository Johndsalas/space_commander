
# Beginning Values
fuel = 100
food = 100
power = 100
hull = 100
crew = 100
burn_rate = 100
morale = 100
distance = 100
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
    event_list = ["gravitational_force","restock","contamination","navigational_malfunction","lifeform","magnetic_field","ambush","confined","deterioration","asteroid_field","mixed","feast","recreation","spacewalk","relations","syphon","hording","stealing","blockade","decenters","boarded"]


    for event in event_list:

        # print event name
        print(f"{event}")
        print("")

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

            print("You discover that your food reserves have not been stocked to regulation.")
            print("Luckely, there is a habitable planet not too far from you.")
            print("You could land there and replenish the missing food supply.")
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
            print("You had to destroy some of the reserves to prevent the mold from spreading.")
            print("")

            lost_food += r.randint(1,20)

            print(f"You have lost {lost_food} units of food.")
            print("")

        elif event == "navigational_malfunction":

            print("The ship’s navigational system is malfunctioning, causing it to recommend a longer travel route ")
            print("than is necessary. You could use some of your power crystals to feed additional power to the ")
            print("navigation system allowing it to reboot and correct the error immediately. Alternatively, you ")
            print("could spend additional fuel to keep the ship on schedule and allow the navigation system to ")
            print("reboot in the morning.")
            print("")
            print("")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) More power: lose 1-5 power crystals")
                print("b) More fuel: lose 1-10 fuel")
                print("")
                choice = input()

                if choice == "a":

                    lost_power += r.randint(1,5)
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

            print("Strange alien life forms have begun attaching themselves to the ship in search of food, and you ")
            print("must prevent your crew becoming the main course. You could lure the creatures away by ")
            print("jettisoning some of your food reserves. Alternatively, you could use some of your power ")
            print("crystals to create a power surge strong enough to fry the invading creatures.")
            print("")

            while resolving_event:
                
                print("What are your orders?")
                print("a) lure the creatures away: lose 1-20 food")
                print("b) fry the invaders: lose 1-5 power crystals")
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

            print("Several short range Garquackien ships have dropped out of hyperspace and are preparing to ")
            print("fire on your ship. You could outpace them at your current speed, but not without sustaining ")
            print("fire. Alternatively, you cold spent additional fuel to engage in evasive maneuvers and avoid ")
            print("taking fire completely.")
            
            while resolving_event:

                print("What are your orders?")
                print("a) Maintain current heading: lose 1-3 hull")
                print("b) Evasive Maneuvers: lose 1-10 fuel ")
                print("")
                choice=input()

                if choice == "a":

                    lost_hull += r.randint(1,3)
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

                    lost_fuel += r.randint(1,10)

                    print(f"You have lost {lost_fuel} units of fuel.")
                    print("")
                    break

                else:

                    print("Please enter a or b.")
                    print("")
                    continue

        elif event == "stealing":

            print("You have discovered several power crystals are missing from the ships supply. It is likely, but ")
            print("not certain, that some of the crew have been stealing them for personal use. You could order a ")
            print("search and send the guilty crew members to the brig. Doing so would recover the lost crystals ")
            print("but would deprive the ship of their services of any guilty crew members for the remainder of ")
            print("the journey.")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) Search the ship: lose 0-3 crew")
                print("b) turn a blind eye for now: lose 1-5 power crystals")
                print("")
                choice = input()

                if choice == "a":

                    lost_crew += r.randint(0,3)

                    print(f"You have lost {lost_crew} crew.")
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

        elif event == "hording":

            print("Persistent rumors of food shortages have prompted some of the crew to begin hording food. ")
            print("You could choose to make an example of the hoarders by searching the ship and throwing ")
            print("anyone caught with extra rations in the brig. This would put a stop to the hording but would ")
            print("deny you the services of any crew member found guilty. Who knows…? Maybe it was rats…?")
            print("Space Rats!")

            while resolving_event:

                print("What are your orders?")
                print("a) Search the ship: lose 0-3 crew")
                print("b) Turn a blind eye for now: lose 1-20 food")
                print("")
                choice = input()

                if choice == "a":

                    lost_crew += r.randint(0,3)

                    print(f"You have lost {lost_crew} crew.")
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

        elif event == "blockade":

            print("Some of the Garquackiens have gotten ahead of you and set up a blockade. With no way to ")
            print("navigate around, you are forced to confront the blockade head on. You could send fighters to ")
            print("clear out the blockade, risking the lives of some of your crew, or ram through the blockade ")
            print("causing damage to the hull of your ship.  ")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) Deploy the fighters: lose 0-3 crew")
                print("b) Ramming Speed: lose 1-5 hull")
                print("")
                choice = input()

                if choice == "a":

                    lost_crew += r.randint(0,3)

                    print(f"You have lost {lost_crew} crew.")
                    print("")
                    break

                elif choice == "b":

                    lost_hull += r.randint(1,5)

                    print(f"You have sustained {lost_hull} damage to the hull.")
                    print("")
                    break

                else:

                    print("Please enter a or b.")
                    print("")
                    continue

        elif event == "decenters":

            print("Fear among the crew has turned into whispers of mutiny. The crew unpersuaded, and you ")
            print("remain confident that they will not betray you. However, such whispering is having a negative ")
            print("effect on the crew’s morale. You could round up the whisperers and send them to the brig this ")
            print("would put a stop to their whispering and restore morale, however this would deny you the ")
            print("services of any of the whispering crew member.")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) Send the whisperers to the brig: lose 0-3 crew")
                print("b) Confront the whisperers privately: lose 1-20 morale")
                print("")
                choice = input()

                if choice == "a":

                    lost_crew += r.randint(0,3)

                    print(f"You have lost {lost_crew} crew.")
                    print("")
                    break

                elif choice == "b":

                    lost_hull += r.morale(1,5)

                    print(f"You have lost {lost_morale} morale.")
                    print("")
                    break

                else:

                    print("Please enter a or b.")
                    print("")
                    continue

        elif event == "boarded":

            print("Without warning, several Garquackien soldiers beame aboard your ship in an attempt to ")
            print("commandeer it. Your crew manages to dispatch the invaders, but not without a fight.")
            
            lost_crew += r.randint(0,3)
            
            print(f"You lost {lost_crew} crew in during the battle.")
            print("")

        fuel -= lost_fuel
        food -= lost_food
        power -= lost_power
        hull -= lost_hull
        crew -= lost_crew
        morale -= lost_morale  

        print(f"Fuel: {fuel}")
        print(f"food: {food}")
        print(f"power: {power}")
        print(f"hull: {hull}")
        print(f"crew: {crew}")
        print(f"moral: {morale}")
        print("")


    #return fuel, food, power, hull, crew, burn_rate, morale, distance

event(fuel, food, power, hull, crew, burn_rate, morale, distance)
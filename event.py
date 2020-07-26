
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
    event_list = ["gravitational_force","restock","contamination","navigational_malfunction","lifeform","territory_dispute","ambush","confined","deterioration","asteroid_field","mixed","feast","recreation","worse","relations","syphon","hording","stealing","blockade","decenters","boarded"]


    for event in event_list:

        # print event name
        print(f"{event}")
        print("")

        # carryout chosen event (display text, give choice if applocable, modify lost variables, display result text)
        if event == "gravitational_force":

            print("Your ship is passing by a large star and is nearly caught in its gravity well. Through clever ")
            print("piloting you manage to escape the star’s pull, but not without burning through some of your ")
            print("fuel reserves. ")
            print("")

            lost_fuel += r.randint(1,10)

            print(f"You have lost {lost_fuel} units of fuel.")
            print("")

        elif event == "restock":

            print("You discover that your food reserves have not been stocked to regulation. Luckily, your ")
            print("scanners have located a habitable planet. You could be use some of your fuel reserves to")
            print("make a detour to the planet the restock your missing food, maintain your current course. ")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) Detour to planet: loose 1-10 fuel.")
                print("b) Stay the course: lose 1-20 food.")
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
            print("could spend some of your fuel reserve to keep the ship on schedule and allow the navigation ")
            print("system to reboot in the morning.")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) Reboot the system: lose 1-5 power crystals)
                print("b) Stay the course: lose 1-10 fuel")
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

            print("Hostel alien life forms are discovered clinging to your ship. They are looking for their next meal, ")
            print("and you are determined to prevent you and your crew from becoming the main course. You ")
            print("could lure the creatures away by jettisoning some of your food reserves. Alternatively, you ")
            print("could use some of your power crystals to create a power surge strong enough to fry the ")
            print("invading creatures.")

            while resolving_event:
                
                print("What are your orders?")
                print("a) Jettison the food: lose 1-20 food")
                print("b) Fry the invaders: lose 1-5 power crystals")
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

        elif event == "territory_dispute":

            print("Your journey home requires a brief passage through Ya’mean space. The Ya’mean do not like ")
            print("visitors; A fact they make well known by placing space mines throughout their borders. These ")
            print("mines emit a sonic frequency that is known to shatter the power crystals that power most")
            print("spaceships. Having no time to reach out diplomatically, you plot a course that should get you in  ")
            print("and out with at least some of your power crystals intact.")

            lost_power += r.randint(1,5)

            print(f"You lose {lost_power} power crystals")
            print("")

        elif event == "ambush":

            print("Several short range Garquackien ships have dropped out of hyperspace and are preparing to ")
            print("fire on your ship. At your current speed you will soon be out of range, but not without ")
            print("sustaining fire and damaging the ship’s hull. Alternatively, you cold spent some of your fuel ")
            print("reserves to engage in evasive maneuvers and avoid taking fire completely.")
            
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

            print("The vegetation you are cultivating for the ship’s food supply, is not yielding the expected")
            print("amount. Vegetation of this type grows better in open environments, making the cramped space")
            print("that has been designated for “agricultural purposes” less than Ideal. You could do some")
            print("renovation to alleviate this concern, however doing so could signifyingly damage the ship’s")
            print("hull.")
            print("")

            while resolving_event:

                print("What are your orders?")
                print("a) Order the renovation: lose 1-3 hull")
                print("b) Preserve the ship: lose 1-20 food")
                print("")
                choice = input()

                if choice == "a":

                    lost_hull += r.randint(1,3)
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

            print("The maintenance system that keeps the hull in good repair has malfunctioned resulting in ")
            print("damage to the hull. You could choose to fix the damage by using some of the ship’s repair bots. ")
            print("However, you would need to power the bots using some of the ship’s power crystals.")
            print("")
            
            while resolving_event:

                print("What are your orders?")
                print("a) Repair the ship: lose 1-5 power crystals")
                print("b) It’ll hold together: lose 1-3 hull")
                choice = input()

                if choice == "a":

                    lost_power += r.randint(1,5)

                    print(f"You have lost {lost_power} power crystals.")
                    print("")
                    break

                elif choice == "b":

                    lost_hull += r.randint(1,3)

                    print(f"You have sustained {lost_hull} damage to the hull.")
                    print("")
                    break

                else:

                    print("Please enter a or b.")
                    print("")
                    continue

        elif event == "asteroid_field":

            print("Curse that navigation computer, it’s led you straight into an asteroid field. As you begin trying ")
            print("to pilot your way out you can hear the sound of space rocks making an impact on your ship.")
            print("")

            lost_hull += r.randint(0,3)

            print(f"You have sustained {lost_hull} damage to the hull.")
            print("")

        elif event == "mixed":

            print("Apparently, someone though it would be funny to mix a stink fluid made from a Scaal sweat")
            print("gland with part or your fuel supply before you left base for your patrol mission. When the")
            print("mixed fuel is burned in the ship’s propulsion system, it fills the ship with a smell that is most")
            print("foul. Having to endure the smell is having a negative impact on the crew’s morale. Will you")
            print("endure the smell is having a negative impact on the crew’s morale. Will you continue to use the ")
            print("continue to use the “prank” fuel or will you destroy it.")
                
            while resolving_event:
                
                print("What are your orders?")
                print("a) Jettison the “prank” fuel: lose 1-10 fuel")
                print("b) Continue to use the “prank” fuel: lose 1-20 morale")
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

            print("Despondency is beginning to take hold of your crew. Reflecting upon the sudden loss of the")
            print("space station they called home, their own dire situation, and the fate of the earth if they should")
            print("fail has been too much to process. You consider holding a small calibration to raise the crew’s")
            print("spirits. A few hours of food, song, and dancing will keep crew’s mind off of their struggles for")
            print("long enough to restore some of their sanity. However, hosting such an event would require")
            print("dipping into the ship’s food reserve.")

            while resolving_event:

                print("What are your orders?")
                print("a) Hold the celebration: lose food")
                print("b) Conserve supplies: lose 1-20 morale")
                print("")
                choice = input()


                if choice == "a":

                    lost_food += r.randint(1,20)

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

        elif event == "worse":

            print("After running a diagnostic on the hull of your ship, you discover that much of the damage")
            print("sustained in the attack on Star Gazer 1, is worse than it appears. You could choose to build")
            print("physical fortifications in the ship to prevent the damage from worsening. However, the")
            print("fortifications are bulky and would make an already cramped ship feel even more so. Morale")
            print("could suffer as a result.")

            while resolving_event:

                print("What are your orders?")
                print("a) Repair the ship: lose 1-20 morale")
                print("b) It’ll hold together: lose 1-3 hull")
                print("")
                choice = input()

                if choice == "a":

                    lost_morale += r.randint(1,20)

                    print(f"You have lost {lost_morale} morale.")
                    print("")
                    break
                   

                elif choice == "b":

                    lost_hull += r.randint(0,3)

                    print(f"You sustained {lost_hull} damage to your hull.")
                    print("")
                    break

                else:

                    print("Please enter a or b.")
                    print("")
                    continue


        elif event == "relations":

            print("‘Relations’ between two senior staff members have soured, resulting in open hostility, and the")
            print("subornment crew are being forced to choose sides. You have done what you can to address the")
            print("situation. However, there is still a lingering air of disharmony and resentment among the staff.")
            print("")

            lost_morale += r.randint(1,20)

            print(f"You have lost {lost_morale} morale.")
            print("")

        elif event == "syphon":

            print("An Eminore pirate vessel has attaches itself to your ship and is beginning to steal its fuel. You")
            print("could use force to overcome the smaller vessel and prevent the theft. However, doing so would ")
            print("put the lives of your crewmembers at risk.")
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
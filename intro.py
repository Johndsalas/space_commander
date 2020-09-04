import  random

def intro(fuel, food, power, hull, crew, morale):

    lost_fuel = random.randint(1,10)
    lost_food = random.randint(1,10) + random.randint(1,10)
    lost_power = random.randint(1,6)
    lost_hull = random.randint(0,3)
    lost_crew = random.randint(0,3)
    lost_morale = random.randint(20,40)

    fuel -= lost_fuel
    food -= lost_food
    power -= lost_power
    hull -= lost_hull
    crew -= lost_crew
    morale -= lost_morale  
    
    print("As you arrive within scanning distance of Star Gazer 1, you find only broken metal and empty space")
    print("where a space station should be. To make matters worse, sensors are picking up several Garquackien")
    print("ships still in the area. Thanks to your years, in the captain’s seat, you quickly piece together")
    print("what has happened. The Garquackiens must have amassed a large armada, the likes of which the ")
    print("universe had never seen, in an attempt to destroy Earth Force and take over the galaxy. It is ")
    print("likely that they attacked here in mass to prevent their real target from readying its defenses, ")
    print("and their real target is Earth! You predict that it will take them 10 Intergalactic Standard Weeks ")
    print("to reach Earth. You must reach earth before they do, and sound the alarm. If you don’t Earth is")
    print("DOOMED!")
    print("")
    print("press ENTER to continue")
    input()
    print("")
    print("The Ships you noticed earlier are beginning to surround you. It seems the Garquackien armada")
    print("left behind a contingent of ships to finish off any Earth Force ships that happened to be away")
    print("during the attack. The Garquacks spared no expense in launching the surprise attack, you think ")
    print("to yourself, but if they think I’m going to die today, then they don’t know Captain ")
    print("*Chough-Chough*!")
    print("")
    print("press ENTER to continue")
    input()
    print("")
    print("You narrowly escape the clutches of the Garquackien kill squad, and have managed avoid ")
    print("detection for the moment. During this respite, your mind turns to the status of your ship and its ")
    print("crew. Your last mission had been successful (for what that was worth) but also taxing. Your ")
    print("resources, crew and even the ship itself, have been under considerable strain already. You can ")
    print("only hope that the ship will hold together until you make it back to earth. With a heavy heart")
    print("you raise your eyes to the HUD and examine what remains of your resources.")

    # print("After escaping the Garquackien ships you recive rhe following status report")
    # print(f"Lost crew members: {lost_crew}")
    # print(f"Damaged fuel reserves: {lost_fuel} units")
    # print(f"Damaged food reserves: {lost_food} units")
    # print(f"Damaged power crystals: {lost_power}")
    # print(f"Damage sustained to hull: {lost_hull}")
    # print(f"The crew's morale is holding at {morale}%")

    return fuel, food, power, hull, crew, morale
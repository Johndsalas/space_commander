import  random

def intro(fuel, food, power, hull, crew, morale):

    lost_fuel = random.randint(1,10)
    lost_food = random.randint(1,10) + random.randint(1,10)
    lost_power = random.randint(1,6)
    lost_hull = random.randint(0,3)
    lost_crew = random.randint(0,3)
    lost_morale = random.randint(20,40)

    # fuel -= lost_fuel
    # food -= lost_food
    # power -= lost_power
    # hull -= lost_hull
    # crew -= lost_crew
    # morale -= lost_morale  
    

    print("You narrowly escape the clutches of the Garquackien kill squad, and have managed avoid ")
    print("detection for the moment. During this respite, your mind turns to the status of your ship and its ")
    print("crew. Your last mission had been successful (for what that was worth) but also taxing. Your ")
    print("resources, crew and even the ship itself, have been under considerable strain already. You can ")
    print("only hope that the ship will hold together until you make it back to earth. With a heavy heart")
    print("you raise your eyes to the HUD and examine what remains of your resources.")
    print("")
    print("press ENTER to continue")
    input()
    print("")

    # print("After escaping the Garquackien ships you recive rhe following status report")
    # print(f"Lost crew members: {lost_crew}")
    # print(f"Damaged fuel reserves: {lost_fuel} units")
    # print(f"Damaged food reserves: {lost_food} units")
    # print(f"Damaged power crystals: {lost_power}")
    # print(f"Damage to hull: {lost_hull}")
    # print(f"The crew's morale is holding at {morale}%")

    return fuel, food, power, hull, crew, morale
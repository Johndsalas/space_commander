import  random


def intro(fuel, food, power, hull, crew, morale):

    lost_fuel = random.randint(1,10)
    lost_food = random.randint(1,10)
    lost_power = random.randint(1,6)
    lost_hull = random.randint(0,2)
    lost_crew = random.randint(0,2)
    lost_morale = 0

    fuel -= lost_fuel
    food -= lost_food
    power -= lost_power
    hull -= lost_hull
    crew -= lost_crew
    morale -= lost_morale

    print("The Story Continues…")
    print("")
    print("You manage to elude or destroy all of the attacking ships, but not without sustaining damage of")
    print("your own. Between this latest attack and completing the last mission your supplies are")
    print("beginning to dwindle. The ship is self-sustaining to a point, if its resources are properly")
    print("managed. You can only hope that the ship will hold together long enough to make it back to")
    print("Earth and raise the alarm. Feeling the weight of your new responsibility, you raise your eyes to ")
    print("the HUD and examine what remains of your resources and crew...")
    print("")
    print("press ENTER to continue")
    input()
    print("")

    print("After escaping the Garquackien ships you receive the following status report:")
    print("")
    print(f"Lost crew members: {lost_crew}")
    print("")
    print(f"Missing fuel reserves: {lost_fuel}")
    print(f"Missing food reserves: {lost_food}")
    print(f"Missing power crystals: {lost_power}")
    print("")
    print(f"Damage to hull: {lost_hull}")
    print("")
    print(f"The crew's morale is at {morale}%")

    return fuel, food, power, hull, crew, morale
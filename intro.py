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
    hull -= lost_power
    crew -= lost_crew
    morale -= lost_morale  
    
    print("The year is 202020, and Space Force Captain, Captain *Chough* (That’s you!) has just returned to base.")
    print("The mission was nothing to write home about, just a routine patrol through the neutral space")
    print("separating Earth from the evil Garquack empire and its quest for galactic domination.")
    print("")
    input("press ENTER to continue")
    print("To your surprise when you arrive back at base you find that it is under attack.")
    print("A large armada of Garquack ships have managed to ambush and decimate the relatively small and unprepared space station.")
    print("Worse yet, from the communications you’ve managed to intercept it’s clear the Garquackiens are on their way to Earth,")
    print("and they are not intent on polite conversation.")
    print("You manage to calculate that it will take 11 galactic standard days for the Garquack armada to reach earth.")
    print("If you can beat them there, even by one day, it will allow Earth to muster its defences and assure victory.")
    print("If you do not, Earth will surely meet the same fate as the destroyed space station you just returned to.")
    print("")
    input("press ENTER to continue")
    print("As you begin issuing orders to your crew, you notice that you have begun taking fire.")
    print("Several of the Garquackien ships have noticed you and are intent on you not spoiling Earth’s surprise. ")
    print("Through masterful captaining you manage to escape, but not without taking substantial damage in the process.")
    print("")
    input("press ENTER to continue")

    print("After escaping the Garquackien ships you recive rhe following status report")
    print(f"Lost crew members: {lost_crew}")
    print(f"Damaged fuel reserves: {lost_fuel} units")
    print(f"Damaged food reserves: {lost_food} units")
    print(f"Damaged power crystals: {lost_power}")
    print(f"Damage sustained to hull: {lost_hull}")
    print(f"The crew's morale is holding at {morale}%")

    return fuel, food, power, hull, crew, morale
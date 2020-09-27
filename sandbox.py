import random as r

# list of events
event_list = ["gravitational_force","restock","contamination","navigational_malfunction","lifeform","territory_dispute","ambush","confined","deterioration","asteroid_field","mixed","feast","recreation","worse","relations","syphon","hording","stealing","blockade","decenters","boarded"]

event_number = 2

getting_events = True

for n in range(1,31):
    # get a number of unique events

    this_weeks_events = []

    while getting_events:

        this_weeks_events.append(r.choice(event_list))

        if len(set(this_weeks_events)) == event_number:

            break

        else:

            continue

    print(list(set(this_weeks_events)))


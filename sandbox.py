

def is_true():

    return True

def is_false():

    return False

loop = True

while loop == True:

    print("start loop")

    if is_true():

        print("is true")

        if is_false():

            print("this should not print")

        else:
            
            print("shold stop loop")
            break


name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way you would like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk across and swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "swim":
        print("You walked for about a few miles and you ran out of water and you died")
    else:
        print("Not valid, you died.")       

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back (corss/back): ").lower()

    if answer == "cross":
        print("You died due to the bridge being old and it collapsed")
    elif answer == "back":
        answer = input("You are back at the checkpoint and found a car, do you want to drive it or instead take the supplies in it? (drive/take) ").lower()

        if answer == "drive":
            input("Great you just crossed the river by taking a long route and found a safe house. (rest/continue)? ")
        elif answer == "take":
            print("You died as it was night and you were encountered by a pack of wolves.")
        else:
            print("Not valid, you died.")

    else:
        print("Not valid, you died.")  

else:
    print("Not valid, you died.")  

print("thank you for playing", name)   



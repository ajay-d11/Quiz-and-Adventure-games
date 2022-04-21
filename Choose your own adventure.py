def adventure():    
    name = input("What is your name?")
    print("Welcome", name, "to the adventure, to play this game, choose between either options given to continue with the story. Good luck...")

    option1 = input("You are hiking and come upon a cave. Do you 'go in' or 'walk around it'?")
    if option1 == "go in":
        option12 = input("You come across a bear. Do you 'touch it' or 'keep walking'?")
        if option12 == "touch it":
            option13 = input("The bear wakes up. Do you 'run' or 'be friends'?")
            if option13 == "run":
                option15 = input("You run out of the cave, but the bear follows. Do you 'fight' or 'accept defeat'?")
                if option15 == "fight":
                    print("You attempt to fight the bear, you swings first but does no damage. The bear then bites your head off. You die.")
                elif option15 == "accept defeat":
                    print("The bear swings at you. You take the hit and bleed out. You die.")
                else:
                    print("Invalid answer, you lose")
            elif option13 == "be friends":
                option17 = input("The bear likes this. Do you 'give hug' or 'high five'?")
                if option17 == "give hug":
                    print("The bear gives you a massive hug but breaks your back. You die.")
                elif option17 == "high five":
                    print("The bear gives you a high five but misses your hand. It swings at your face and rips the skin off. You die.")
                else:
                    print("Invalid answer, you lose")
            else:
                print("Invalid answer, you lose")
    
        elif option12 == "keep walking":
            option14 = input("You go down the cave and find an egg. Do you 'eat it' or 'take it'")
            if option14 == "eat it":
                option16 = input("After you eat it, you start to feel funny. Do you 'drink water' or 'keep walking'?")
                if option16 == "drink water":
                    print("You go to drink water but you ran out. You then fall do the ground of poison. You die.")
                elif option16 == "keep walking":
                    print("You walk down the cave, you feel nauseous and trip and fall down a ravine. You die.")
                else:
                    print("Invalid answer, youn lose")

            elif option14 == "take it":
                option18 = input("A massive spider comes out, it does not like that you took its egg. Do you 'run' or 'hide'?")
                if option18 == "run":
                    print("You attempt to outrun the spider but it shoots its web at you. You get stuck and the spider eats you alive. You die.")
                elif option18 == "hide":
                    print("You run behind a rock. You think you lost the spider but thrn turn around; the last thing you saw was the spiders mouth. You die.")
                else:
                    print("Invalid answer, you lose")
        else:
            print("Invalid answer, you lose")


    elif option1 == "walk around it":
        option3 = input("That is so boring, all the interesting things happen in the cave SMH, now go back and redo this!!! Type redo")
        if option3 == "redo":
            adventure()
    
        else:
            print("Wow okay, be like that, goodbye.")

    else:
        print("Invalid answer, you lose")

adventure()

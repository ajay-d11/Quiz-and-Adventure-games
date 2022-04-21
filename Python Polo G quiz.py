

def game():
        score = 0
        answer1 = input("What is Polo G's record label called?").upper()
        if answer1 == "ODA":
            print("Correct!")
            score += 1
        else: 
            print("Incorrect, the answer is ODA")

        answer2 = input("What does the letter G in Polo G's name stand for?").lower()
        if answer2 == "gucci":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is gucci")

        answer3 = input("What is Polo G's first album called?").lower()
        if answer3 == "die a legend":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is die a legend")

        answer4 = input("Which city is Polo G from?").lower()
        if answer4 == "chicago":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is chicago")

        answer5 = input("What song made Polo G blow up?").lower()
        if answer5 == "finer things":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is finer things")

        answer6 = input("Who was featured on Polo G's song Suicide?").lower()
        if answer6 == "lil tjay":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the anser is Lil Tjay")

        answer7 = input("How many siblings does Polo G have?")
        if answer7 == "3":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is 3")

        answer8 = input("What other popular name does Polo G go by?").lower()
        if answer8 == "capalot":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is capalot")

        answer9 = input("Who was the first artist signed to Polo G's record label?").lower()
        if answer9 == "scorey":
            print("Correct")
            score += 1
        else:
            print("Incorrect, the answer is scorey")

        answer10 = input("Is Polo G the GOAT?").lower()
        if answer10 == "yes":
            print("Correct")
            score += 1
        else:
            print("Incorrect, of course he is the GOAT SMH")

        print("Congrats! you got " + str(score) + " answers right out of 10!")
        print("Your percentage is " + str((score) * 10) + "%")

        play_again = input("Do you want to play again? yes or no: ")
        if play_again == "yes":
            game()
        else:
            print("Adios")




quiz = input("Do you want to play my quiz? Yes or No: ").lower()
if quiz == "yes":
    game()
else:
    print("Wow rude")

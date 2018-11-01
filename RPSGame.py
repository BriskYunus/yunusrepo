from random import randint
mylifebar = 3
pclifebar = 3
z = 0
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False


# make the computer pick one item at random
computer = choices[randint(0, 2)]


while player is False:
    print("")
    print("Select your item!")
    print("Your Health " + str(mylifebar))
    print("Computers Health " + str(pclifebar))


    player = input("Rock, Paper, Scissors?\n")
    print("Player chooses:", player)

    if (player == computer):
        print("Computer chooses: ", computer)
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer chooses: ", computer)
            print("You lose the round,", computer, "covers", player)
            mylifebar = mylifebar - 1
        else:
            print("Computer chooses: ", computer)
            print("You win the round,", player, "smashes", computer)
            pclifebar = pclifebar - 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Computer chooses: ", computer)
            print("You lose the round,", computer, "cuts", player)
            mylifebar = mylifebar - 1

        else:
            print("Computer chooses: ", computer)
            print("You win the round,", player, "covers", computer)
            pclifebar = pclifebar - 1
         

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer chooses: ", computer)
            print("You lose the round,", computer, "smashes", player)
            mylifebar = mylifebar - 1
           
        else:
            print("Computer chooses: ", computer)
            print("You win the round,", player, "cuts", computer)
            pclifebar = pclifebar - 1


    elif player == "Quit":
        exit()
        



    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    player = False
    computer = choices[randint(0, 2)]

    if pchealth is z:
        print("")
        print("*You WIN!*")
        print("")
        player = input("Would you like to play again? y / n\n")
        pclifebar = pclifebar + 3
        mylifebar = mylifebar
        if player == "y":
            player = False
        if player == "n":
            break


    if mylifebar is z:
        print("")
        print("*You LOSE!*")
        print("")
        player = input("Would you like to play again? y / n\n")
        mylifebar = mylifebar + 3
        pclifebar = mylifebar
        if player == "y":
            player = False
        if player == "n":
            break



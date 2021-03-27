from gameComponents import gameVars


    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("Hmmm, it's a draw -_-")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print(" HAHAHA! you lose! player lives:", gameVars.player_lives)
        else:
            print("Oh no, you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print(" HAHAHA!you lose! player lives:", gameVars.player_lives)
        else:
            print("Oh no, you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print(" HAHAHA!you lose! player lives:", gameVars.player_lives)
        else:
            print("Oh no, you win!")
            gameVars.computer_lives -= 1
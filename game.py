


from random import randint

from gameComponents import gameVars, winLose, comp

while gameVars.player_choice is False:
    print("----------------------/ ROCK PAPER SCISSORS GAME */----------------------")
    print('Can you win A.I?) lets try))')
    print('_______________________----------_______________________')
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("================================================")
    print("Choose your weapon! Or type quit to exit\n")
    gameVars.player_choice = input("Choose ROCK, PAPER, or SCISSORS: \n")


    if gameVars.player_choice == "quit":
        print("why?!(")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]




    if gameVars.player_lives == 0:
        winLose.winorlose("Ups, you lost")
    elif gameVars.computer_lives == 0:
        winLose.winorlose("oh no... You won(")
    else:
        gameVars.player_choice = False

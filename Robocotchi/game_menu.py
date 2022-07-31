from numbers_game import Numbers
from rock_scissor_papper import RSP


def choose_game():
    while True:
        game = input("Which game would you like to play? Rock-paper-scissors or Numbers? \n")
        if game == "Rock-paper-scissors":
            rsp = RSP()
            rsp.game_menu()
            break
        elif game == "Numbers":
            numbers_game = Numbers()
            numbers_game.game_menu()
            break
        else:
            print('Please choose a valid option: Numbers or Rock-paper-scissors?')



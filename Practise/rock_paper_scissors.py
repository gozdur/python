
stop = False
while (not stop):
        print("\n################")
        print("1)Rock")
        print("2)Paper")
        print("3)Scissors")
        print("\n################")

        while True:
            selection_player_1 = int(input("Player 1 choose your move: "))
            if selection_player_1 == 1:
                print("Player 1 selected: Rock")
                break
            elif selection_player_1 == 2:
                print("Player 1 selected: Paper")
                break
            elif selection_player_1 == 3:
                print("Player 1 selected: Scissors")
                break
            else:
                print("Wrong choice please type 1, 2, or 3")

        print("\n################")

        while True:
            selection_player_2 = int(input("Player 2 choose your move: "))
            if selection_player_2 == 1:
                print("Player 2 selected: Rock")
                break
            elif selection_player_2 == 2:
                print("Player 2 selected: Paper")
                break
            elif selection_player_2 == 3:
                print("Player 2 selected: Scissors")
                break
            else:
                print("Wrong choice please type 1, 2, or 3")

        print("\n################")
        print("\n################")
        print("\n#####Result#####")
        print("\n")


        if selection_player_1 == selection_player_2:
            print("It's a Draw!")
        elif selection_player_1 == 1 and selection_player_2 == 2:
            print("Player 2 Wins!")
        elif selection_player_1 == 1 and selection_player_2 == 3:
            print("Player 1 Wins!")
        elif selection_player_1 == 2 and selection_player_2 == 1:
            print("Player 1 Wins!")
        elif selection_player_1 == 2 and selection_player_2 == 3:
            print("Player 2 Wins!")
        elif selection_player_1 == 3 and selection_player_2 == 1:
            print("Player 2 Wins!")
        #elif selection_player_1 == 3 and selection_player_2 == 2:
        #    print("Player 2 Wins!")
        else:
            print("Player 2 Wins!")
        print("\n")
        while True:
            answer = input("Stat a new game?(Y/N): ")
            if answer == "Y" or answer == "y":
                print("New game will start")
                break
            elif answer == "N" or answer == "n":
                print("Goodbye!")
                stop = True
                break
            else:
                print("Wrong answer please type Y/N !")

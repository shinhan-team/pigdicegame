from random import randint


class Player:

    def __init__(self):
        self.now_score = 0
        self.total_score = 0

    def roll(self):
        dice_number = randint(1,6)
        if dice_number == 1:
            return
        else:
            self.now_score += dice_number

    def stop(self,now_score):
        self.total_score += now_score
        if self.total_score > 50:
            return


def set_print_format(number):
    if number == 1:
        print("----------------------------Pig Dice Game--------------------")
        print("|                             |                              |")
        print("|         Player 1            |            Player 2          |")
        print("|                             |                              |")
        print(f"|          [  {player_1.now_score}  ]            |             [  {player_2.now_score}  ]          |")
        print("|                             |                              |")
        print("|                             |                              |")
        print("|           Bank              |              Bank            |")
        print("|                             |                              |")
        print(f"|          [  {player_1.total_score}  ]            |             [  {player_2.total_score}  ]          |")
        print("|                             |                              |")
        print("|                             |                              |")
        print("--------------------------------------------------------------")
    elif number == 2:
        print("----------------------------------------Pig Dice Game----------------------------------------")
        print("|                             |                              |                              |")
        print("|         Player 1            |            Player 2          |            Player 3          |")
        print("|                             |                              |                              |")
        print(f"|          [  {player_1.now_score}  ]            |             [  {player_2.now_score}  ]          |             [  {player_3.now_score}  ]          |")
        print("|                             |                              |                              |")
        print("|                             |                              |                              |")
        print("|           Bank              |              Bank            |              Bank            |")
        print("|                             |                              |                              |")
        print(f"|          [  {player_1.total_score}  ]            |             [  {player_2.total_score}  ]          |             [  {player_3.total_score}  ]          |")
        print("|                             |                              |                              |")
        print("|                             |                              |                              |")
        print("---------------------------------------------------------------------------------------------")
    elif number == 3:
        print("-----------------------------------------------------------Pig Dice Game----------------------------------------------------")
        print("|                             |                              |                              |                              |")
        print("|         Player 1            |            Player 2          |            Player 3          |            Player 4          |")
        print("|                             |                              |                              |                              |")
        print(f"|          [  {player_1.now_score}  ]            |             [  {player_2.now_score}  ]          |             [  {player_3.now_score}  ]          |             [  {player_4.now_score}  ]          |")
        print("|                             |                              |                              |                              |")
        print("|                             |                              |                              |                              |")
        print("|           Bank              |              Bank            |              Bank            |              Bank            |")
        print("|                             |                              |                              |                              |")
        print(f"|          [  {player_1.total_score}  ]            |             [  {player_2.total_score}  ]          |             [  {player_3.total_score}  ]          |             [  {player_4.total_score}  ]          |")
        print("|                             |                              |                              |                              |")
        print("|                             |                              |                              |                              |")
        print("----------------------------------------------------------------------------------------------------------------------------")



player_1 = Player()
player_2 = Player()
player_3 = Player()
player_4 = Player()
computer_number = int(input("Choose Enemy number do you want to fight !!(1~3) >> "))
set_print_format(computer_number)

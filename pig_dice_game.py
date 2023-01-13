from random import randint


class Player:

    def __init__(self):
        self.now_score = 0
        self.total_score = 0

    def roll(self):
        dice_number = randint(1,6)
        if dice_number == 1:
            self.now_score = 0
            return dice_number
        else:
            self.now_score += dice_number
            return dice_number

    def stop(self,now_score):
        self.total_score += now_score
        self.now_score = 0
        if self.total_score >= 50:
            return False
        
        return True

    def play_game(self):
        print("Player 1's Turn !")
        dice_number = self.roll()
        print(f"Dice Number : {dice_number} !!")
        if dice_number == 1:
            return dice_number
        set_print_format(computer_number)
        choice = input("Choice !! Roll the dice(Y), or STOP(S) >> ")
        return choice


class Computer:


    def __init__(self):
        self.now_score = 0
        self.total_score = 0

    def roll(self):
        dice_number = randint(1,6)
        if dice_number == 1:
            self.now_score = 0
            return False
        else:
            self.now_score += dice_number
            return True

    def stop(self):
        self.total_score += self.now_score
        self.now_score = 0
        if self.total_score >= 50:
            return False
        
        return True

    def check_over_25(self):
        if self.now_score >= 25:
            self.stop()
            return False
        
        return True


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
computer_number = int(input("Choose Enemy number do you want to fight !!(1~3) >> "))
for i in range(computer_number):
    globals()[f"player_{i+2}"] = Computer()

is_win = False
while True:
    count = 0
    print("Player 1's Trun !")
    if count%(computer_number+1) == 0:
        choice = input("Choice !! Roll the dice(Y), or STOP(S) >> ")
        if choice == 'Y':
            while True:
                choice = player_1.play_game()
                if choice == 1:
                    break
                if choice == 'S':
                    player_1.stop(player_1.now_score)
                    if player_1.total_score >= 50:
                        set_print_format(computer_number)
                        print("YOU WIN!!!!!!!!!!!!!!!!!!!!!!!!!")
                        is_win = True
                        break
                    if player_1.stop(player_1.now_score):
                        break

    if is_win:
        break
    count += 1
    if computer_number == 1:
        print(f"Player {count+1}'s Turn !")
        while player_2.check_over_25():
            if not player_2.roll():
                break

        if player_2.total_score >= 50:
            set_print_format(computer_number)
            print("Game End, Player 2 Win !")
            break
        set_print_format(computer_number)
        count +=1
    elif computer_number == 2:
        print(f"Player {count+1}'s Turn !")
        while player_2.check_over_25():
            if not player_2.roll():
                break

        if player_2.total_score >= 50:
            set_print_format(computer_number)
            print("Game End, Player 2 Win !")
            break
        set_print_format(computer_number)
        count +=1

        print(f"Player {count+1}'s Turn !")
        while player_3.check_over_25():
            if not player_3.roll():
                break

        if player_3.total_score >= 50:
            set_print_format(computer_number)
            print("Game End, Player 3 Win !")
            break
        set_print_format(computer_number)
        count +=1
    elif computer_number == 3:
        print(f"Player {count+1}'s Turn !")
        while player_2.check_over_25():
            if not player_2.roll():
                break

        if player_2.total_score >= 50:
            set_print_format(computer_number)
            print("Game End, Player 2 Win !")
            break
        set_print_format(computer_number)
        count +=1

        print(f"Player {count+1}'s Turn !")
        while player_3.check_over_25():
            if not player_3.roll():
                break

        if player_3.total_score >= 50:
            set_print_format(computer_number)
            print("Game End, Player 3 Win !")
            break
        set_print_format(computer_number)
        count +=1

        print(f"Player {count+1}'s Turn !")
        while player_4.check_over_25():
            if not player_4.roll():
                break

        if player_4.total_score >= 50:
            set_print_format(computer_number)
            print("Game End, Player 4 Win !")
            break
        set_print_format(computer_number)
        count +=1


                
                

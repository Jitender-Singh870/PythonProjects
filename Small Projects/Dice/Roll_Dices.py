from copy import deepcopy
from math import ceil
from random import randint
import os, time


DEBUG = 0


def clear_console():
    """function to empty the console"""
    os.system('cls')



class DiceGame:
    """Dice rolling game class"""
    wall = "│"
    roof = "─"
    top_right = "┐"
    top_left = "┌"
    bot_right = "┘"
    bot_left = "└"
    dot = "●"
    size = 5


    def dice_display(self, list_dice: list):
        """function to print dices
        
        Parameters
        --------------
        list_dice : list
            list of dices to roll build by **build_dices()** func"""
        for inner in list_dice:
            for sign in inner:
                print(sign, end="")
            print()


    def build_dices(self, xlim, ylim, offset_y, roll_pos_list) -> list:
        """function that builds dices"""
        template_square = []
        # xlim = 10
        # ylim = xlim*2 + 1
        for x in range(xlim):
            temp = []
            for y in range(ylim):
                temp.append([x, y])
            template_square.append(temp)
        
        # print(square)
        for inner_list in template_square:
            temp = deepcopy(inner_list)
            for pos in inner_list:
                # print(pos)
                if pos[0] == 0 and pos[1] == 0:
                    temp[inner_list.index(pos)] = self.top_left
                elif pos[0] == 0 and pos[1] == ylim - 1:
                    temp[inner_list.index(pos)] = self.top_right
                elif pos[0] == xlim - 1 and pos[1] == 0:
                    temp[inner_list.index(pos)] = self.bot_left
                elif pos[0] == xlim - 1 and pos[1] == ylim - 1:
                    temp[inner_list.index(pos)] = self.bot_right
                elif (pos[0] == 0 or pos[0] == xlim - 1) and (pos[1] > 0 and pos[1] < ylim-1): # roof
                    temp[inner_list.index(pos)] = self.roof
                elif (pos[0] > 0 and pos[0] < xlim-1) and (pos[1] == 0 or pos[1] == ylim - 1): # walls
                    temp[inner_list.index(pos)] = self.wall
            template_square[template_square.index(inner_list)] = temp

        # for i in square:
        #     print(i)
        dice_list = [[] for _ in range(xlim)]
        # dice list maker
        for per_dice_pos in roll_pos_list:
            if DEBUG : print(f"dice for {per_dice_pos}: ")
            for x, inner in enumerate(template_square):
                for pos in inner:
                    if type(pos) is not list:
                        dice_list[x].append(pos)
                        if DEBUG : print(pos, end="")
                    else:
                        if tuple(pos) in per_dice_pos:
                            dice_list[x].append(self.dot)
                            if DEBUG : print(self.dot, end="")
                        else:
                            dice_list[x].append(" ")
                            if DEBUG : print(" ", end="")
                if DEBUG : print()
        return dice_list
    
    def roll_dice(self, rolls_count: int = 2):
        """rolls the dice depending on size (5 or 7) and count of dices to roll
        
        Parameters
        ------------
        rolls_count: int
            number of dices to roll
        """
        size = self.size
        xlim = size
        ylim = (size*2) + 1
        offset_y = ceil(xlim / 10)
        rolls_dict = {
            1 :  [(int(xlim/2), int(ylim/2))],
            2 : [(1, 1 + offset_y), ( (xlim-1)-1, (ylim-offset_y)-1-1)], # -1 for index, -1 for wall, -offset for dot place correction
            3 : [(int(xlim/2), int(ylim/2)), (1, 1 + offset_y), ( (xlim-1)-1, (ylim-offset_y)-1-1)],
            4 : [(1, 1 + offset_y), ( (xlim-1)-1, (ylim-offset_y)-1-1), (1, ylim-offset_y-1-1), (xlim-1-1, 1 + offset_y)],
            5 : [(int(xlim/2), int(ylim/2)), (1, 1 + offset_y), ( (xlim-1)-1, (ylim-offset_y)-1-1), (1, ylim-offset_y-1-1), (xlim-1-1, 1 + offset_y)],
            6 : [(1, 1 + offset_y), ( (xlim-1)-1, (ylim-offset_y)-1-1), (1, ylim-offset_y-1-1), (xlim-1-1, 1 + offset_y), (int((xlim)/2), 1+offset_y), (int((xlim-1)/2), (ylim-1-1-offset_y))]
        }

        clear_console()
        if rolls_count > 10:
            roll_count_list = []
            while rolls_count > 9:
                roll_count_list.append(10)
                rolls_count = rolls_count - 10
            if rolls_count > 0:
                roll_count_list.append(rolls_count)

            for rolls in roll_count_list:
                dice_rolls_list = [rolls_dict[randint(1, 6)] for _ in range(rolls)]
                # for pos_list in dice_rolls_list:
                printable_dice_list = self.build_dices(xlim=xlim, ylim=ylim, offset_y=offset_y, roll_pos_list=dice_rolls_list)
                self.dice_display(printable_dice_list)
        else:
            dice_rolls_list = [rolls_dict[randint(1, 6)] for _ in range(rolls_count)]
            # for pos_list in dice_rolls_list:
            printable_dice_list = self.build_dices(xlim=xlim, ylim=ylim, offset_y=offset_y, roll_pos_list=dice_rolls_list)
            self.dice_display(printable_dice_list)
        time.sleep(2)

        if DEBUG : print("position of dots in dice: ",dice_rolls_list)
        if DEBUG : print("\nFinal Dice List made for printing: ", printable_dice_list)






## ACTUAL Game begins here:

game = DiceGame()

clear_console()
is_break = True
while(True):
    args = input("\t\t🎲 WELCOME TO Dice Roll 🎲"
                "\n\tWrite 'big' and number of dices to roll if you want bigger dices."
                "\n\tAnd add 'infinity' or 'unli' to enter an infinity loop. \n\tOr write 'exit' to end loop\nEx:"
                "\n\t1. 'big 3' to roll 3 dices of size big"
                 "\n\t2. 'big infinity 5' to enter loop and have bigger dices"
                 "\n\t3. 'unli 5' to have 5 dices and start loop"
                 "\n\t4. '25' to have 25 dice rolls"
                 "\nWrite here: ")
    args = args.lower()
    if "'" in args:
        clear_console()
        print("Without the '' (quotes) ")
        continue

    if 'exit' in args:
        print("Good bye 🎲")
        break

    if not args:
        clear_console()
        print("\nNext time please enter the number of dices to roll or 2 dices will be rolled by default.\n")
        game.roll_dice()
        # if is_break : break
        continue

    if DEBUG : print(f"Arguments of type ('{type(args)}') inputted by user: ('{args}')")

    args = args.strip().lower().replace('  ', ' ').split(' ')

    if len(args) == 1:
        if args[0].isdecimal():
            game.roll_dice(rolls_count=int(args[0]))
            if is_break : break
        else:
            print("Invalid input, enter a valid amount of dices to roll or press enter for default 2 dice rolls,doing a default dice roll:\n")
            game.roll_dice()
            if is_break : break

    if 2 <= len(args) <= 4:
        size = 5
        rolls = 2
        got_rolls = got_size = False
        got_valid = True
        for arg in args:
            if arg.isdecimal():
                if got_rolls is False:
                    got_rolls = True
                    rolls = int(arg)
                else:
                    print("Invalid input, cannot enter more than 1 number or digits separated by spaces. try again\n")
                    got_valid = False
                    if is_break : break
            else:
                if got_size is False:
                    if 'big' in arg:
                        got_size = True
                        if game.size == 7:
                            print("Tip: no need to enter big again in a loop.")
                        game.size = 7
                    elif 'unli' in arg or 'infinity' in arg:
                        is_break = False
                    else:
                        print("Invalid input, possible inputs: 'big', 'unli' or 'infinity' or/and a number separated by space. try again\n")
                        got_valid = False
                        if is_break : break
                else:
                    if 'unli' in arg or 'infinity' in arg:
                        is_break = False
                    else:
                        print("Invalid input, cannot enter more than 2 words. try again\n")
                        got_valid = False
                        if is_break : break
        if got_valid:
            game.roll_dice(rolls_count=rolls)
            if is_break : break

    if len(args) > 3:
        print("Too many inputs received, cannot process, going with a random dice count between 2 and 10:\n")
        dice_rolls = randint(2, 10)
        game.roll_dice(rolls_count=dice_rolls)
        if is_break : break

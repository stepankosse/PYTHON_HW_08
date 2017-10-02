# -*- coding: utf-8 -*-
__author__ = "Stepan Kosse"

import random
import sys
import copy


class Kegs:
    def __init__(self):
        self.kegs_list = list(range(1, 90))
        self.keg_curr = -1

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.kegs_list) > 0:
            self.keg_curr = random.choice(self.kegs_list)
            self.kegs_list.remove(self.keg_curr)
            return self.keg_curr
        else:
            return -1

    def get_text_about_keg_curr(self):
        return "\nНовый бочонок: {0} (осталось {1}).".format(self.keg_curr, len(self.kegs_list))


class Card():
    def __init__(self, type):
        self.card = {x: ["  ", "  ", "  "] for x in range(0, 9)}
        self.count_active_num = 15
        self.type = type
        numbers_list = list(range(1, 90))
        for i in range(0, 3):
            indexes_list = list(self.card.keys())
            for j in range(0, 5):
                curr_index = random.choice(indexes_list)
                indexes_list.remove(curr_index)

                discharge_list = list(range(curr_index * 10, curr_index * 10 + 10))
                for item in discharge_list:
                    if not (item in numbers_list):
                        discharge_list.remove(item)

                self.card[curr_index][i] = random.choice(discharge_list)
                numbers_list.remove(self.card[curr_index][i])

    def __repr__(self):
        footer = "--------------------------"
        if self.type == 0:
            title = "------ Ваша карточка -----\n"
        elif self.type == 1:
            title = "-- Карточка компьютера ---\n"

        print_card = copy.deepcopy(self.card)
        for index in range(0, 3):
            if len(str(print_card[0][index])) == 1:
                print_card[0][index] = str(" {}".format(print_card[0][index]))

        row1 = " ".join(map(str, [print_card[x][0] for x in range(0, 9)]))
        row2 = " ".join(map(str, [print_card[x][1] for x in range(0, 9)]))
        row3 = " ".join(map(str, [print_card[x][2] for x in range(0, 9)]))

        return "{0}\n{1}\n{2}\n{3}\n{4}".format(title, row1, row2, row3, footer)

    def search_number(self, number):
        column = number // 10
        if number in self.card[column]:
            index = self.card[column].index(number)
            self.card[column][index] = "--"
            self.count_active_num += -1
            return 1
        else:
            return 0


class Game():
    def __init__(self):
        self.status_game = -1
        self.kegs = Kegs()
        self.player_card = Card(0)
        self.computer_card = Card(1)
        self.game_go()

    def __repr__(self):
        return "{0}\n{1}\n{2}".format(
            self.kegs.get_text_about_keg_curr(),
            self.player_card,
            self.computer_card
        )

    def game_go(self):
        for keg_item in self.kegs:
            if keg_item != -1:
                print(self)
                self.status_game = -1
                while self.status_game == -1:
                    self.get_result_step()
                    if self.player_card.count_active_num == 0 or self.computer_card.count_active_num == 0:
                        self.status_game = 0

                if self.status_game == 0:
                    self.game_over()
                continue

            break
        self.game_over()

    def get_result_step(self):
        input_data = input("Зачеркнуть цифру?\n(Y/N): ")
        player_result = self.player_card.search_number(self.kegs.keg_curr)
        computer_result = self.computer_card.search_number(self.kegs.keg_curr)
        if input_data == "Y" or input_data == "y":
            if player_result == 0:
                self.status_game = 0
            else:
                self.status_game = 1

        elif input_data == "N" or input_data == "n":
            if player_result == 1:
                self.status_game = 0
            else:
                self.status_game = 1

        else:
            print("Не нужно жать все клавиши подряд! 'Y' или 'N'!")
            self.status_game = -1

    def game_over(self):
        print("GAME OVER!")
        if self.player_card.count_active_num == 0 and self.computer_card.count_active_num == 0:
            print("Ничья!")
        elif self.player_card.count_active_num == 0:
            print("Поздравляю! Ты победил!")
        elif self.computer_card.count_active_num == 0:
            print("Сожалею! Ты проиграл!")
        else:
            print("Игра была прервана.")
        sys.exit(0)

# -*- coding: utf-8 -*-
__author__ = "Stepan Kosse"

import classes as cl


def main():
    user_answer = True
    while user_answer:
        match = cl.Game()

        input_data = input("\nЕщё партейку?\n(Y/N): ")
        if input_data != "Y" and input_data != "y":
            user_answer = False


if __name__ == "__main__":
    main()

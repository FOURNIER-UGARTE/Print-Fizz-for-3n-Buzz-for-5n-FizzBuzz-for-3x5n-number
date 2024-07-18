##!/usr/bin/env python3

#Created by FOURNIER UGARTE Óscar

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Print_Fizz_Buzz_FizzBuzz import Print_Fizz_Buzz_FizzBuzz


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('spectator')
    print('Solution by Óscar FOURNIER UGARTE, next: ')

    start_n = 1
    end_n = 100
    print("Next the result of the method: ")
    print("Print_Fizz_Buzz_FizzBuzz.print_Fizz_Buzz_FizzBuzz_number")
    print(", in a range of:", start_n, "to", end_n)
    for number in range(start_n, end_n + 1):
        Print_Fizz_Buzz_FizzBuzz.print_Fizz_Buzz_FizzBuzz_number(number)
        print()
    print("EOL of the result of the method: ")
    print("Print_Fizz_Buzz_FizzBuzz.print_Fizz_Buzz_FizzBuzz_number")
    print(", in a range of:", start_n, "to", end_n)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Created by Óscar FOURNIER UGARTE
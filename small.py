#!/usr/bin/env python3

# Created by: Ahmad
# Created on: Jan 2021
# This program uses an array


from random import randint


def find_smallest(array):
    smallest = array[0]
    for num in array:
        if num < smallest:
            smallest = num
    return smallest


def main():
    array = []
    for loop in range(10):
        array.append(randint(0, 99))
    print("Here is a list of random numbers:")
    print("\n")
    for loop in range(len(array)):
        print("The random number {} is: {}".format(loop + 1, array[loop]))
    print("\nThe smallest number is", find_smallest(array))
    print("Done.")


if __name__ == "__main__":
    main()

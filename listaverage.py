#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: December 2019
# This program calculates the average of grades using list

import random


def average(grade_list):
    total = 0
    result = 0
    counter = 0
    for number in grade_list:
        total += number
        counter += 1
    result = total / counter
    result = int(result)
    return result


def main():
    # This function gets the input and passes it to another function
    grade_list = []

    # Input and part of Process
    while True:
        grade = input("enter the grade: ")
        if grade == "-1":
            break
        try:
            grade = int(grade)
        except(Exception):
            print("Wrong Input !!!")
            return
        if grade >= 0 and grade <= 100:
            grade_list.append(grade)

    # Passing to another function
    result = average(grade_list)

    # Output
    print("average is {}".format(result))


if __name__ == "__main__":
    main()

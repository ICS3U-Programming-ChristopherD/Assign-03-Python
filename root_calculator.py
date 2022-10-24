#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Oct. 21, 2022
# This module is used to calculate the solutions of a quadratic.


from termcolor import colored
from logging import root
import math

# Defining the root solver function:
def root_solver(a, b, c):

    # Declaring the discriminant variable:
    discriminant = b**2 - 4 * a * c

    # Code executed if the discriminant is equal to or greater than 0:
    if discriminant >= 0:
        unknown_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        unknown_2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # Code executed if the discriminant is less than 0:
    else:
        unknown_1 = complex((-b / (2 * a)), math.sqrt(-discriminant) / (2 * a))
        unknown_2 = complex((-b / (2 * a)), -math.sqrt(-discriminant) / (2 * a))

    # Prints the two real roots if the discriminant is greater than 0:
    if discriminant > 0:
        print(
            colored(
                f"The function has two real roots: {unknown_1} and {unknown_2}",
                "yellow",
            )
        )

    # Prints the single root of the quadratic if the discriminant is equal to 0:
    elif discriminant == 0:
        print(colored(f"The function has one real root: {unknown_1}", "yellow"))

    # Prints the two complex roots of the quadratic if the discriminant is less than 0:
    else:
        print(
            colored(
                f"The function has two complex roots: {unknown_1} and {unknown_2}",
                "yellow",
            )
        )

from random import randint, seed
from random import random


def generateRandomNumber():
    seed(10)
    return randint(0, 1000)


def main():
    machineRand = generateRandomNumber()

    print("Welcome to the Random Number Generator!")

    print("The computer has generated a random number: ", machineRand)


if __name__ == "__main__":
    main()

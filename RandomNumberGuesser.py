from random import randint, seed
from random import random


def generateRandomNumber():
    seed(10)
    return randint(0, 1000)


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


def main():
    machineRand = generateRandomNumber()

    print("Welcome to the Random Number Generator!")
    print("The computer has generated a random number: ", machineRand)
    userInput = input("Please guess the computer's random number: ")
    userInput = int(userInput)

    if (userInput == machineRand):
        print("Congratulations! You have successfully guessed the computer's random number")
        print("The Computer's random number was: ", machineRand)
    else:
        diff = abs(machineRand - userInput)
        print("You did not guess the computer's random number, here are some hints!")
        if(is_prime_number(machineRand)):
            print("The Computer's random number is prime")
        else:
            print("The Computer's random number is not prime")


if __name__ == "__main__":
    main()

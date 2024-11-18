'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out
'''

# ------ IMPORT --------
import random

#------- CODE EXERCISE -------
'''
num1 = random.randrange(1,9)

print("Hello and welcome to GUESS 'THE RIGHT NUMBER!'... The computer has now picked a random number from 1 to 9")
print()
guess = int(input("What number do you think is the right one?"))
print()
print("So, you picked number ",guess,". Let'see if you got it right...")
print()
print()

if num1 == guess:
    print("The number to guess was ",num1," and you picked ",guess,"...")
    print()
    print("WOW! You got it right")

if num1 <= guess:
    print("The number to guess was ",num1," and you picked ",guess,"...")
    print()
    print("Your guess was too high!")

if num1 >= guess:
    print("The number to guess was ",num1," and you picked ",guess,"...")
    print()
    print("Your guess was too low!")
'''

#------- EXTRA 1 -------

'''
num1 = random.randrange(1,9)

print("Hello and welcome to GUESS 'THE RIGHT NUMBER!'... The computer has now picked a random number from 1 to 9")
print()
guess = int(input("What number do you think is the right one?"))
print()
print("So, you picked number ",guess,". Let'see if you got it right...")
print()
print()
   

while num1 < guess:
    print("I am checking...")
    print()
    print("Your guess was too high!")
    print()
    tryagain = input("Do you want to try again? yes to continue or type 'exit'")
    if tryagain == "yes":
        print()
        guess = int(input("What number do you think is the right one?"))
    if tryagain == "exit":
        print()
        print("Ok, hope you had fun!")
        break
                

while num1 > guess:
    print("I am checking...")
    print()
    print("Your guess was too low!")
    print()
    tryagain = input("Do you want to try again? yes to continue or type 'exit'")
    if tryagain == "yes":
        print()
        guess = int(input("What number do you think is the right one?"))
    if tryagain == "exit":
        print()
        print("Ok, hope you had fun!")
        break

if num1 == guess:
    print("I am checking...")
    print()
    print("WOW! You got it right")

'''

# ------- EXTRA 2 ----------


num1 = random.randrange(1,9)
guess = 0
count = 0

print("Hello and welcome to GUESS 'THE RIGHT NUMBER!'... The computer has now picked a random number from 1 to 9")
print()
   

while guess != num1 and guess != "exit":
    guess = input("What's your lucky number?")
    
    if guess == "exit":
        break

    while not type(guess) == int:
        if guess == "exit":
            break
        try:
            guess = int(guess)
        except ValueError:
            guess = input("Enter a number from 1 to 9, it is not that difficult")

    guess = int(guess)
    count += 1

    if guess < num1:
        print("your guess is too low!")

    elif guess > num1:
        print("your guess is too high!")

    else:
        again = input ("You got it in {} guesses. My number was {}. Again y/n?" . format(count,num1))
        if again == "n" or again == "exit":
            break

        if again == "y":
            guess = 0
            count = 0
            num1 = random.randrange(1,9)

        while again != "y" and again != "n" and again != "exit":
            again = input ("y/n?")
            if again == "y":
                guess = 0
                count = 0
                num1 = random.randrange(1,9)



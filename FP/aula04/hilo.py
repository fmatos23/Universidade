# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive

    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    guess = int(input("Enter a number between 1 and 100: "))
    count = 1
    while guess != secret:
        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!!")
        guess = int(input("Enter a number between 1 and 100: "))
        count += 1
    print(f'well done, after {count} tries u did it')

main()

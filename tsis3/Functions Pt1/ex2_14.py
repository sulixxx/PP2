import random

def guess_the_stars():
    name = input("Hello broski! What's your name?\n")
    print(f"Well, my broski - {name}, let's play a game. I've thought of some number of stars between 1 and 10, and you need to guess how many stars I've thought of.")
    secret_stars = random.randint(1, 10)
    taken_guesses = 0
    
    while True:
        guess = input("Take a guess:\n")
        
        if guess.count("*") != len(guess):
            print("Sorry broski, you can only enter *")
            continue
        
        taken_guesses += 1
        
        guess_num = len(guess)
        
        if guess_num < secret_stars:
            print("Your guess is too low broski:(")
        elif guess_num > secret_stars:
            print("Ohh, broski, it's too high, than I've thought of:(")
        else:
            print(f"BOMBOCLAT!!! {name}, you are one of the few who could guess the number of stars in {taken_guesses} guesses!!!")
            break

guess_the_stars()

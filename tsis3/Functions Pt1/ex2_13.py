import random

def guess_the_number () :
    name = str ( input ( "Hello broski! Whats your name?\n"))
    print ( f"Well, my broski - {name}, lets play a game, i just think bout some number from 1 - 20, you need to guess it.")
    secret_number = random.randint ( 1, 20 )
    taken_guesses = 0
    
    while True:
        guess = int ( input ( "Take a guess\n" ))
        taken_guesses += 1
        
        if guess < secret_number :
            print ( "Your guess is too low broski:(")
        elif guess > secret_number :
            print ( "Ohh, broski, its too higher, than i had in my mind:(")
        else :
            print ( f"BOMBOCLAT!!! {name}, you are one of the few who could guess my number in {taken_guesses} guesses!!!")
            break
        
guess_the_number ()

from art import logo
from random import randint
from replit import clear

EASY=10
HARD=5

def level():
    wrong=True
    while wrong:
        difficulty=input("Choose a diffulty level: type 'easy' or 'hard'\n").lower()[0]
        if difficulty=="e" or difficulty=="h":
            wrong=False
        else:
            print("Wrong command! Please enter 'easy' or 'hard'\n")
            wrong=True
    if difficulty=="e":
        return EASY
    else:
        return HARD

def check_guess(guess, num, turns):
    
    if guess==num:
        print(f"\nCongratulations! You have guessed the right number: {num}")
    elif guess>num:
        print("\nToo high!")
        return turns-1
    else:
        print("\nToo low!")
        return turns-1

def game():
    clear()
    print(logo)
    print("Welcome to Guessit! Can you guess the right number?\n")
    
    num=randint(1,100)
    turns=level()
    guess="-"
    while guess!=num:
        print(f"You have {turns} attempt left to guess the number")
        int_float=True
        while int_float:
            try:
                guess=int(input("Guess a number between 1 and 100: "))
                int_float=False
            except:
                print("Wrong input! Please enter a whole number between 1 and 100")
                
        turns=check_guess(guess,num,turns)
        if turns==0:
            print(f"\nYou are out of turn, the number was {num}\nYou lost")
            return
        elif guess!=num:
            print("\nGuess again.")

game()

replay=input("Do you want to play again? Reply 'y' or 'n':  ").lower()[0]

if replay=="y":
    game()
else:
    print("Goodbye!")
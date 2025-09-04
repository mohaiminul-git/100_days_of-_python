
import random
logo = '''  ___  __  __  ____  ___  ___    ____  _   _  ____    _  _  __  __  __  __  ____  ____  ____ 
 / __)(  )(  )( ___)/ __)/ __)  (_  _)( )_( )( ___)  ( \( )(  )(  )(  \/  )(  _ \( ___)(  _ \
( (_-. )(__)(  )__) \__ \\__ \    )(   ) _ (  )__)    )  (  )(__)(  )    (  ) _ < )__)  )   /
 \___/(______)(____)(___/(___/   (__) (_) (_)(____)  (_)\_)(______)(_/\/\_)(____/(____)(_)\_)
                                                                                             
'''
print(logo)

def guess_number():
    print("welcome to the guessing game !")
    print("i am thinking of a number 1 to 100")
    secret_number= random.randint(1,100)
    difficulty_level=str.lower(input("choose difficulty level -> easy,medium,high : "))

    if difficulty_level=="easy":
        max_attempt=10
    elif difficulty_level=="medium":
        max_attempt=7
    else :
        max_attempt=5
    print(f"you have {max_attempt} attemps to guess the number")
    attempt= 0
    while attempt < max_attempt:
        guess= input("Enter your Guess : ")
        
        if not  guess.isdigit():
            print("Invaid Entry, Guess again")
            continue
        guess=int(guess)
        attempt+=1
        print(f"you have {max_attempt-attempt} attempt left")
        if guess < secret_number:
            print("too low")
        elif guess > secret_number:
            print("too high ")
        else:
            print ("congrates, you have guessed the number")
    else:
        print(f"you have lost. The secret number was {secret_number}")

if __name__=="__main__":
    guess_number()


        
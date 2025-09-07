from art import logo
from art import vs
import random
from game_data import data




def higher_lower_game():
    print(logo)
    score=0
    game_should_continue=True
    A=random.choice(data)
    
    

    while game_should_continue:
        
        
        print(f"Compare A: {A['name']},a {A['description']},from {A['country']}.")
        print(vs)
        B=random.choice(data)
        while A==B:
            B=random.choice(data)
        print(f"Compare B:{B['name']},a {B['description']},from {B['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (guess=="a" and A['follower_count'] > B['follower_count']) or (guess=="b" and B['follower_count'] > A['follower_count']):
            score+=1
            print(f"your current score {score}")
            if guess=="a":
                pass
                            
            else:
                A=B
                
        else:
            print(f"you have lost. your score {score}")
            game_should_continue=False

        



higher_lower_game()
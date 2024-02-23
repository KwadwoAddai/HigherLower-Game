import random
import os
from art import logo,vs
from game_data import data
#CLEAR THE SCREEN
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
#FORMAT THE ACCOUNT DATA 
def format_data(account):
    """Format the account data"""
    acc_name = account['name']
    acc_desc = account['description']
    acc_country = account['country']
    return(f"{acc_name}, a {acc_desc}, from {acc_country}")
#CHECK IF USER IS CORRECT
def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
#DISPLAY ART
print(logo)
print("WHO HAS MORE FOLLOWERS ON INSTAGRAM")
user_score = 0
game_over = False
account_b = random.choice(data)
while not game_over:
    #GENERATE RANDOM ACCOUNTS
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    #GET FOLLOWER COUNT
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    #ASK USER TO MAKE A GUESS
    user_choice = input("Who has more IG followers A or B?: ").lower()
    is_correct = check_answer(user_choice,a_followers,b_followers)
    #CLEAR SCREEN
    clear()
    print(logo)
    #GIVE USER FEEDBACK AND SCORE KEEPING
    if is_correct:
        user_score+=1
        print(f"You're right: current score is {user_score}")
    else:
        print(f"You are Wrong: current score is {user_score}")
        game_over = True
    


#MAKE GAME REPEATABLE

#MAKE CURRENT ACCOUNT THE NEXT ACCOUNT





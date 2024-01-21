import art
from game_data import data
import random
import os


def pick_random(list_of_dict):
    """Returns a random IG account from the DB on game_data"""
    db_size=len(list_of_dict)
    num=random.randint(0,db_size-1)
    return list_of_dict[num]

def compare_followers(accounts):
    """Returns the index of IG Account with higher number of followers"""
    if accounts[0]['follower_count'] > accounts[1]['follower_count']:
        return 0
    else:
        return 1

def check_answer(user_guess,list_of_dict):
    """Returns the score increase. 1 if the guess was right or 0 if it was wrong"""
    options=["a","b"]
    if user_guess not in options:
        print("Not an option")
        return 0
    if options.index(user_guess)==compare_followers(list_of_dict):
        return 1      
    else:
        return 0  

def format_account(instagram_account):
    """Takes accounts data and returns printable format"""
    account_name=instagram_account['name']
    account_desc=instagram_account['description']
    account_country=instagram_account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def higher_or_lower_game():
    """User guess which of the 2 IG account randomly choosen from db has more followers.
    If user is right he increase the score in 1 point until he misses, then the game ends"""
    continue_game=True
    score=0
    accounts=[]
    accounts.append(pick_random(data))
    result=1
    while(result):
        accounts.append(pick_random(data)) 
        while accounts[0] == accounts[1]:    #IF A=B validation
            accounts[1]=pick_random(data)
        print(f"Compare A: {format_account(accounts[0])}" )
        print(art.vs)
        print(f"Against B: {format_account(accounts[1])}" )
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        result=check_answer(guess, accounts)
        os.system('cls')
        if result:
            score+=result
            accounts.pop(0)
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.") 
            return 

print(art.logo)
higher_or_lower_game()



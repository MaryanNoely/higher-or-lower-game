import art
from game_data import data
import random
import os


# pick 2 to compare and print -> function

def pick_random(list_of_dict):
    """Returns a random IG account from the DB on game_data"""
    db_size=len(list_of_dict)
    num=random.randint(0,db_size-1)
    print(f"TEST chosen {list_of_dict[num]}")
    return list_of_dict[num]

def compare_followers(accounts):
    """Returns the index of IG Account with higher number of followers"""
    if accounts[0]['follower_count'] > accounts[1]['follower_count']:
        return 0
    else:
        return 1

def guess_result(guess,higher_account):
    """Returns the score increase. 1 if the guess was right or 0 if it was wrong"""
    options=["a","b"]
    if guess not in options:
        print("Not an option")
        return 0
    if options.index(guess)==higher_account:
        return 1      
    else:
        return 0  

def game():
    """User guess which of the 2 IG account randomly choosen from db has more followers.
    If user is right he increase the score in 1 point until he misses, then the game ends"""
    continue_game=True
    score=0
    accounts=[]
    accounts.append(pick_random(data))
    result=1
    while(result):
        accounts.append(pick_random(data)) #Missing IF A=B validation
        print(f"Compare A: {accounts[0]['name']}, a {accounts[0]['description']}, from {accounts[0]['country']}" )
        print(art.vs)
        print(f"Against B: {accounts[1]['name']}, a {accounts[1]['description']}, from {accounts[1]['country']}" )
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        higher_account=compare_followers(accounts)
        result=guess_result(guess, higher_account)
        if result:
            score+=result
            accounts=[accounts[higher_account]]
            os.system('cls')
            print(f"You're right! Current score: {score}.")
        else:
            os.system('cls')
            print(f"Sorry, that's wrong. Final score: {score}.") 
            return

print(art.logo)
game()



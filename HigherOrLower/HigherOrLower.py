from gamedata import data
from gameart import logo
from gameart import vs
import random
import os

def compare(n1,n2):
    if n1>n2:
        return 'a'
    else:
        return 'b'

score = 0
numberofdata = len(data)
randomchoice1 = random.randint(0,numberofdata-1)

def play():
    os.system('clear')
    print(logo)
    global randomchoice1
    global score
    print(f"Compare A: {data[randomchoice1]['name']}, a {data[randomchoice1]['description']}, from {data[randomchoice1]['country']}")
    randomchoice2 = random.randint(0,numberofdata-1)

    if randomchoice2 == randomchoice1:
        while randomchoice2==randomchoice1:
            randomchoice2 = random.randint(0,numberofdata-1)
    print(vs)
    print(f"Against B: {data[randomchoice2]['name']}, a {data[randomchoice2]['description']}, from {data[randomchoice2]['country']}")

    answerfromuser = input("Who has more followers? A or B:   ").lower()

    actualanswer = compare(data[randomchoice1]['follower_count'],data[randomchoice2]['follower_count'])

    if answerfromuser == actualanswer:
        while answerfromuser == actualanswer:
            score = score+1
            print(f"You have answered correctly! Your score is {score}")
            if answerfromuser == 'b':
                randomchoice1 = randomchoice2
            play()
    else:
        print(f"You have guessed incorrectly. Your final score is: {score}")
        start()

def start():
    if input("Press Y to play, N to stop:  ").lower() == 'y':
        global score
        global randomchoice1
        randomchoice1 = random.randint(0,numberofdata-1)
        score = 0
        play()
    else:
        exit()
start()
    

'''

random module ---> Help to generate random values
OTP generation,Story Generation,Game (Rock Papper Scissiors), Number Guessing Game

'''
import random,time
'''
#random number generation --> OTP(time module helps to use time functions)
a = random.randint(1000,9999)
print(a)
for i in range(5):
    time.sleep(2) #sleep(seconds) ---> Helps for waiting period
    print(random.randint(1000,9999))
    #time.sleep(2)

'''
#Playing a Game (Rock Paper Scissiors)
#Two Players --> Game -->
'''

player1 = input("Enter one of these ---> Rock,Paper,Scissors").lower().strip()
player2 = random.choice(["Rock","Paper","Scissors"]).lower()
#print(player1)
print(player2)
if player1 == "rock" and player2 == "paper":
    print("Player2 Won")
elif player1 == "paper" and player2 == "scissors":
    print("Player2 Won")
elif player1 == "scissors" and player2 == "rock":
    print("Player2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player1 Won")
'''


#Get the score for each user and declare the winnerr
#Play the game for 10times ---> Task(Push to Github and Share It (Task))

#Task:2--> Give user a choice --> RPS(1) / NG(2) / 3(study) / Any Number
#No Choice only 1,2,3 ---> Functions

'''
when = ['A long back','Once upon a time','Few Years ago']
who = ['Devara','King in the France','Barbie Queen']
what = ['A magical ','PowerFul Hammer','Unlimitied Arrows']
where = ["Far in the Galaxy", "End of Ocean", "In India"]
how = ["War started", "Both fought for 15 days", "Sad Ending"]
print(random.choice(when)+ " " + random.choice(who))
'''

import segno
print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name="MAnoj SAi",
                         email="manojsai2111@gmail.com",
                         phone="+91 7659802778",
                         url="https://www.linkedin.com/in/manoj-sai-/")
print(qr)
qr.save("mycard.png",scale=10)

#Now Its your turn ---> Explore Modules
#Instagram,Youtube,Email Automation.....


#Build a Virtual Assistant Using Python --> Virtual Environment
#Speak,Respond Back, Greet you, mAke a conversation,Open Browser,
#Locate Google Maps,


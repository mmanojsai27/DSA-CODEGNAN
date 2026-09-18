'''
import random
# ================= RPS GAME =================
def rps():
    player1_score = 0
    player2_score = 0

    for round_number in range(1, 11):
        print("\nRound", round_number)

        player1 = input(
            "Enter one of these ---> Rock, Paper, Scissors: \n"
        ).lower().strip()

        if player1 not in ["rock", "paper", "scissors"]:
            print("Invalid Choice! Try again.")
            continue

        player2 = random.choice(["rock", "paper", "scissors"])

        print("Player2 chose:", player2)

        if player1 == player2:
            print("Tie")

        elif player1 == "rock" and player2 == "paper":
            print("Player2 Won")
            player2_score += 1

        elif player1 == "paper" and player2 == "scissors":
            print("Player2 Won")
            player2_score += 1

        elif player1 == "scissors" and player2 == "rock":
            print("Player2 Won")
            player2_score += 1

        else:
            print("Player1 Won")
            player1_score += 1

        print("Player-1 Score:", player1_score)
        print("Player-2 Score:", player2_score)

    print("\n============= FINAL RESULT =============")
    print("Player-1 Score:", player1_score)
    print("Player-2 Score:", player2_score)

    if player1_score > player2_score:
        print("Player-1 is the Winner")

    elif player2_score > player1_score:
        print("Player-2 is the Winner")

    else:
        print("Match Tied!")


# ================= NUMBER GUESSING GAME =================

def number_guessing():

    print("\n========== NUMBER GUESSING GAME ==========")

    number = random.randint(1, 100)
    attempts = 0

    while True:

        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the correct number.")
            print("Number of attempts:", attempts)
            break

        elif guess < number:
            print("Too Low! Try again.")

        else:
            print("Too High! Try again.")


# ================= STUDY =================

def study():

    print("\n========== STUDY ==========")
    print("Go and study Python!")


# ================= MAIN MENU =================

while True:

    print("\n==============================")
    print("       GAME / STUDY MENU")
    print("==============================")

    print("1. Rock Paper Scissors")
    print("2. Number Guessing")
    print("3. Study")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rps()

    elif choice == "2":
        number_guessing()

    elif choice == "3":
        study()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice! Please enter 1, 2, 3 or 4.")
'''

""" 
from gtts import gTTS
import playsound
text=gTTS('''rohith''')
text.save("audio.mp3")
playsound.playsound("audio.mp3")
"""
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
import pyqrcode
import png


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ika modhalupedadhama")
        audio = r.listen(source,phrase_time_limit = 10)
    data = " "
    try:
        data = r.recognize_google(audio)
        print("you said:",data)
    except sr.UnknownValueError as e:
        print("request failed")
    except sr.RequestError as e:
        print("speak clearly request is failing")
    return data
    #tts = gTTS(data)
    #tts.save("new.mp3")
    #playsound.playsound("new.mp3")
#listen()

def respond(string):
    """function to respond back"""
    print(string)
    tts = gTTS(string)
    tts.save("speech.mp3")
    filename = "speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def va(data):
    """our virtual assistant with the actions"""
    if "how are you" in data:
        listening = True
        respond("you bloody ediot go and study")
    elif "who is your favourite actor" in data:
        listening = True
        respond("i am very big fan of you")
    elif "what are your plans" in data:
        listening = True
        respond("nothing want to have fun with you")
    elif "locate" in data:
        listening = True
        webbrowser.open("https://www.google.com/maps/search/"+ data.replace("locate",""))
        respond("Located")
    elif "open Google" in data:
        listening=True
        webbrowser.open("https://www.google.com")
        respond("opened")
    elif "open YouTube" in data:
        listening = True
        webbrowser.open("https://www.youtube.com/watch?v=JqFzhcWo3EU")
        respond("enjoy your song")
    elif "play a game" in data:
        listening = True
        webbrowser.open("https://poki.com/")
        respond("enjoy your gaming")
    elif "create QR code" in data:
        listening = True
        link = input("enter text or url for qrcode: ")
        qr = pyqrcode.create(link)
        qr.png("qrcode.png",scale=5)
        respond("qrcode created successfully")
    elif "stop talking" in data:
        listening = False
        respond("cool cool... chaduvuko velli")
    try:
        return listening
    except UnboundLocalError as e:
        print("make sure to speak louder")

respond("aya sher........")
listening = True
while listening:
    data = listen()
    listening = va(data)

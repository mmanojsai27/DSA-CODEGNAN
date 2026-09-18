from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
import pyqrcode
import random


# =====================================================
# LISTEN FUNCTION
# =====================================================

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nika modhalupedadhama")

        audio = r.listen(source, phrase_time_limit=10)

    data = ""

    try:

        data = r.recognize_google(audio)

        print("you said:", data)

    except sr.UnknownValueError:

        print("request failed")

    except sr.RequestError:

        print("speak clearly request is failing")

    return data.lower()


# =====================================================
# RESPOND FUNCTION
# =====================================================

def respond(string):

    """function to respond back"""

    print(string)

    tts = gTTS(string)

    filename = "speech%s.mp3" % str(uuid.uuid4())

    tts.save(filename)

    playsound.playsound(filename)

    os.remove(filename)


# =====================================================
# ROCK PAPER SCISSORS GAME
# =====================================================

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

        player2 = random.choice(
            ["rock", "paper", "scissors"]
        )

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


# =====================================================
# NUMBER GUESSING GAME
# =====================================================

def number_guessing():

    print("\n========== NUMBER GUESSING GAME ==========")

    number = random.randint(1, 100)

    attempts = 0

    while True:

        try:

            guess = int(
                input("Guess a number between 1 and 100: ")
            )

            attempts += 1

            if guess == number:

                print(
                    "Congratulations! You guessed the correct number."
                )

                print("Number of attempts:", attempts)

                break

            elif guess < number:

                print("Too Low! Try again.")

            else:

                print("Too High! Try again.")

        except ValueError:

            print("Please enter numbers only.")


# =====================================================
# STUDY
# =====================================================

def study():

    print("\n========== STUDY ==========")

    print("Go and study Python!")


# =====================================================
# QR CODE GENERATOR
# =====================================================

def create_qr():

    print("\n========== QR CODE GENERATOR ==========")

    link = input(
        "Enter text or URL for qrcode: "
    ).strip()


    if link == "":

        respond("Please enter a valid URL or text")

        return


    filename = input(
        "Enter filename for QR code: "
    ).strip()


    if filename == "":

        respond("Filename cannot be empty")

        return


    # Add .png only if user didn't enter it

    if not filename.endswith(".png"):

        filename = filename + ".png"


    qr = pyqrcode.create(link)

    qr.png(filename, scale=5)


    print("QR Code saved as:", filename)

    respond("QR code created successfully")


# =====================================================
# VIRTUAL ASSISTANT
# =====================================================

def va(data):

    """our virtual assistant with the actions"""

    listening = True


    # -------------------------------------------------
    # HOW ARE YOU
    # -------------------------------------------------

    if "how are you" in data:

        respond(
            "you bloody ediot go and study"
        )


    # -------------------------------------------------
    # FAVOURITE ACTOR
    # -------------------------------------------------

    elif "who is your favourite actor" in data:

        respond(
            "i am very big fan of you"
        )


    # -------------------------------------------------
    # PLANS
    # -------------------------------------------------

    elif "what are your plans" in data:

        respond(
            "nothing want to have fun with you"
        )


    # -------------------------------------------------
    # TIME
    # -------------------------------------------------

    elif "time" in data:

        respond(time.ctime())


    # -------------------------------------------------
    # LOCATE
    # -------------------------------------------------

    elif "locate" in data:

        location = data.replace(
            "locate", ""
        ).strip()


        webbrowser.open(
            "https://www.google.com/maps/search/"
            + location
        )

        respond("Located")


    # -------------------------------------------------
    # OPEN GOOGLE
    # -------------------------------------------------

    elif "open google" in data:

        webbrowser.open(
            "https://www.google.com"
        )

        respond("Google opened")


    # -------------------------------------------------
    # OPEN YOUTUBE
    # -------------------------------------------------

    elif "open youtube" in data:

        webbrowser.open(
            "https://www.youtube.com/watch?v=JqFzhcWo3EU"
        )

        respond("Enjoy your song")


    # -------------------------------------------------
    # PLAY ONLINE GAME
    # -------------------------------------------------

    elif "play a game" in data:

        webbrowser.open(
            "https://poki.com/"
        )

        respond("Enjoy your gaming")


    # -------------------------------------------------
    # ROCK PAPER SCISSORS
    # -------------------------------------------------

    elif "rock paper scissors" in data:

        respond(
            "Starting Rock Paper Scissors game"
        )

        rps()


    # -------------------------------------------------
    # NUMBER GUESSING
    # -------------------------------------------------

    elif "number guessing" in data:

        respond(
            "Starting number guessing game"
        )

        number_guessing()


    # -------------------------------------------------
    # STUDY
    # -------------------------------------------------

    elif "study" in data:

        study()


    # -------------------------------------------------
    # CREATE QR CODE
    # -------------------------------------------------

    elif "create qr code" in data:

        create_qr()


    # -------------------------------------------------
    # STOP
    # -------------------------------------------------

    elif "stop talking" in data or "stop" in data:

        listening = False

        respond(
            "cool cool... chaduvuko velli"
        )


    # -------------------------------------------------
    # UNKNOWN COMMAND
    # -------------------------------------------------

    else:

        print("Command not recognized")


    return listening


# =====================================================
# START VIRTUAL ASSISTANT
# =====================================================

respond("aya sher........")


listening = True


while listening:

    data = listen()

    listening = va(data)

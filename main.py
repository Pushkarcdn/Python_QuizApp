# KBC theme music ------------

import pygame  # to support music
import base64  # to support tne in binary format
import io  # to play encoded tune


def dir_tune():
    pygame.mixer.init()
    pygame.mixer.music.load(
        "tune.mp3"
    )  # Replace with the actual path to your tune file
    pygame.mixer.music.play()


def binary_tune():
    pygame.mixer.init()
    tune_data = base64.b64decode(
        """
            #binary code of a tune here
    """
    )
    tune_stream = io.BytesIO(tune_data)
    pygame.mixer.music.load(tune_stream)
    pygame.mixer.music.play()


dir_tune()
# binary_tune()

# KBC Music ends here
# KBC Logic stats here---------

opt1 = [
    "Which of the following is not a programming language ?",
    "Swift",
    "C#",
    "PHP",
    "GO",
    3,
    1000,
]
opt2 = [
    "What is a collection of webpages called ?",
    "WWW",
    "Website",
    "Web",
    "None of these",
    2,
    2000,
]
opt3 = [
    "Which is the first language in history of computer programming ?",
    "C",
    "Ruby",
    "ForTRAN",
    "Perl",
    3,
    3000,
]
opt4 = [
    "What does DNS stands for ?",
    "Domain Name System",
    "Domain Name Server",
    "Dot-Net Sync",
    "None of these",
    1,
    4000,
]
opt5 = ["When was Pushkar born ?", "2062", "2063", "2061", "2059", 3, 5000]

money = 0

print(" \n  !!! WELCOME TO KBC !!!")

print(" \nYour Questions are:")

for list in [opt1, opt2, opt3, opt4, opt5]:
    question = list[0]
    value1 = list[1]
    value2 = list[2]
    value3 = list[3]
    value4 = list[4]

    print(" \n\nQuestion for RS.", list[6], "\n\n" + question, "\n")
    print(
        " Options are: \n",
        "1.",
        value1,
        "\t",
        "2.",
        value2,
        "\n",
        "3.",
        value3,
        "\t",
        "4.",
        value4,
        "\n",
    )

    answer = int(input(" Answer: "))
    if answer == list[5]:
        money = list[6]
        print(" \nCongrats! You won RS.", money)
    else:
        print(" \n\nOops! Wrong answer")
        print(" \nYour total amount won is RS.", money)
        break

if money == 5000:
    print(" \nYou have answered all the questions correctly")

input(" \nThanks for Playing.\n\nPress Enter to exit!\n\n")

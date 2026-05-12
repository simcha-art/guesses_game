from random import randint


def display_menu():
    message = "GUESSES GAME/n" \
    "You should guess the letters to fill all empty places in the word." \
    "You have limited number of rong guesses" 
    print(message)


def is_user_start_playing():
    message = "If you want to play, click 'Y', else click 'N': "
    choice = input(message).upper() == "Y"
    return choice


def display_goodby():
    message = "See you next time!"
    print(message)


WORDS_TO_GUESS = [
    "Apple",
    "Blueberry",
    "House",
    "Runtime",
    "Smartest",
    "Tablecloth",
    "Windows",
    "Happiness",
    "Cloud",
    "Bread"
]


def choose_random_word():
    i = randint(0, len(WORDS_TO_GUESS) - 1)
    return WORDS_TO_GUESS[i]



    
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
    "Blue",
    "House",
    "Run",
    "Smart",
    "Table",
    "Window",
    "Happy",
    "Cloud",
    "Bread"
]



    
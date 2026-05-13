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


def display_beautifully(msg):
    line = "=" * len(msg)
    beautifull_msg = f"{line} \n{msg} \n{line}"
    print(beautifull_msg)


def display_goodby():
    message = "See you next time!"
    display_beautifully(message)

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

def word_by_guesses(word:str, indexes = None):
    guested = ["*"] * len(word)
    if indexes:
        for i in indexes:
            guested[int(i)] = word[int(i)]
    return "".join(guested)


number_of_guesses = 10


def display_state_of_game(guessed_word: str, guesses_number:int):
    message = f"Guessed_word:    {guessed_word},            guesses remained:     {guesses_number}"
    display_beautifully(message)


def user_guess():
    def is_valid_input():
        return len(guess) == 1 and "a" <= guess <= "z"
    

    guess = ""
    while not is_valid_input():
        guess = input("Choose one English letter:\n").lower()

        if not is_valid_input():
            print("ERROR: INVALID INPUT!")

    return guess


    
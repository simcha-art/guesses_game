from random import randint


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

MAX_GUESSES = 10

def display_menu():
    game_name = "GUESSES GAME" 
    display_beautifully(game_name)
    game_rules = "You should guess the letters to fill all empty places in the word. You have limited number of wrong guesses" 
    display_beautifully(game_rules)

def is_user_start_playing():
    message = "If you want to play, click 'Y', else click 'N': "
    choice = input(message).upper() == "Y"
    return choice


def display_beautifully(message):
    line = "=" * len(message)
    beautifull_message = f"\n{line} \n{message} \n{line}\n"
    print(beautifull_message)


def display_goodby():
    message = "See you next time!"
    display_beautifully(message)



def choose_random_word():
    i = randint(0, len(WORDS_TO_GUESS) - 1)
    return WORDS_TO_GUESS[i]





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


def is_correct_guess(word: str, guess: str):
    return guess in word


def update_simbols_word(simbols_word: str, real_word: str, guess: str):
    simbols_word = list(simbols_word)
    for i in range(len(real_word)):
        if guess == real_word[i]:
            simbols_word[i] = real_word[i]
    return "".join(simbols_word)


def is_word_complete(guessed_word: str):
    if "*" in guessed_word:
        return False
    return True


def display_success():
    message = "Congratulation! You have guessed the word!"
    display_beautifully(message)


def display_loss(real_word: str):
    message = f"Sorry, You missed it!, the word was '{real_word}'"
    display_beautifully(message)


def main():
    display_menu()
    start = is_user_start_playing()
    if not start:
        display_goodby()
        return

    real_word = choose_random_word().lower()
    guessed_word = "*" * len(real_word)
    number_of_guesses = MAX_GUESSES

    end = False
    while not end:
        display_state_of_game(guessed_word, number_of_guesses)
        guess = user_guess()

        if is_correct_guess(real_word, guess):
            guessed_word = update_simbols_word(guessed_word, real_word, guess)
            if is_word_complete(guessed_word):
                display_beautifully(guessed_word)
                display_success()
                end = True

        else:
            number_of_guesses -= 1
            if number_of_guesses == 0:
                display_loss(real_word)
                end = True
    
    display_goodby()

if __name__ == "__main__":
    main()
            



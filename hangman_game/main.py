import random
from list_to_string import list_to_string
from get_all_index import get_all_index
from ascii_hangman import hangman

word_collection = [
    "STUTTGART",
    "AZERBAIJAN",
    "UZBEKISTAN",
    "SAPPORO",
    "KARABURAGI",
    "SAMARINDA",
    "SVENSTAVIK",
    "ALBUQUERQUE",
]
picked_word = word_collection[random.randint(0, len(word_collection) - 1)]
picked_word_as_list = list(picked_word)

# Create blank underbars to show how many strings does the word have
blank_bars = []
for strin in picked_word:
    blank_bars += "_"


# Game start
life_left = 6
game_completed = False

print(hangman[life_left])
print(list_to_string(blank_bars))

while life_left > 0 and not game_completed:
    user_entered = input("Guess the letter!\n").upper()
    letter_does_exists = user_entered in picked_word_as_list

    # Handle entered letter
    if letter_does_exists:
        index_of_letters = get_all_index(picked_word_as_list, user_entered)

        for key in index_of_letters:
            blank_bars[key] = user_entered

        game_completed = not "_" in blank_bars

        print(hangman[life_left])
        print(list_to_string(blank_bars))

    else:
        life_left -= 1
        print(hangman[life_left])
        print(list_to_string(blank_bars))

# Game completed
if life_left == 0:
    print(">>>>    YOU LOST    <<<<")
else:
    print(">>>>    YOU WIN!    <<<<")

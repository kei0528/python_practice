import random

user_selected = int(
    input(
        "What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scisoors.\n"
    )
)

options = ["Scissors", "Rock", "Paper"]
random_option_index = random.randint(0, 2)
option = options[random_option_index]

print(f"You selected {options[user_selected]}")
print(f"Computer selected {option}")

if user_selected == random_option_index:
    print("You can try again!")
elif (
    (user_selected == 0 and random_option_index == 1)
    or (user_selected == 1 and random_option_index == 2)
    or (user_selected == 2 and random_option_index == 0)
):
    print("You lost the game!")
else:
    print("You won the game!")

from random import randint
from cafe_data import cafes


def get_random_cafe():
    random_index = randint(0, len(cafes) - 1)
    return cafes.pop(random_index)


def get_cafe_follower(cafe):
    return cafe["follower"]


def compare_cafe(cafe1, cafe2):
    print(
        f"""
     1. {cafe1['name']} in {cafe1['location']}   or   2. {cafe2['name']} in {cafe2['location']}
          """
    )
    selected = input("Which coffee shop does have more followers? Enter 1 or 2 \n")

    cafes = [cafe1, cafe2]
    cafes_sorted_by_follower = sorted(
        cafes, key=get_cafe_follower, reverse=True
    )  # Sort by follower count. index 0 have more follower than index 1

    selected_cafe = 0

    while selected_cafe == 0:
        if selected == "1":
            selected_cafe = cafe1
        elif selected == "2":
            selected_cafe = cafe2
        else:
            selected = input("Please enter correct value. 1 or 2? \n")

    return {
        "result": selected_cafe["name"] == cafes_sorted_by_follower[0]["name"],
        "winner": selected_cafe,
    }


can_continue = True
current_selected = get_random_cafe()

while can_continue and len(cafes) > 1:
    cafe2 = get_random_cafe()
    answer = compare_cafe(current_selected, cafe2)

    can_continue = answer["result"]
    current_selected = answer["winner"]

    if can_continue:
        print("Correct answer!")

if not can_continue:
    print("You Lost!")

if len(cafes) < 2:
    print("Congratuation!")

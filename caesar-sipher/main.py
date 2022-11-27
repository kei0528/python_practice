alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

can_start = True


def start_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while not direction == "decode" and not direction == "encode":
        direction = input("Please type correct value. 'encode' or 'decode' \n")

    text = input("Type your message:\n").lower()

    shift_input = input("Type the shift number:\n")

    while not shift_input.isdigit():
        shift_input = input("Value is not correct. Please enter the number: \n")

    shift = int(shift_input)

    if direction == "decode":
        shift = -shift

    cipher_text = []

    for string in text:
        if not string in alphabet:
            cipher_text.append(string)

        else:
            index_of_string = alphabet.index(string)
            index_of_string_after_processing = index_of_string + shift
            if index_of_string_after_processing > len(alphabet) - 1:
                index_of_string_after_processing = (
                    index_of_string_after_processing % len(alphabet)
                )

            elif index_of_string_after_processing < -(len(alphabet) - 1):
                index_of_string_after_processing = index_of_string_after_processing % -(
                    len(alphabet)
                )

            cipher_text.append(alphabet[index_of_string_after_processing])

    print(
        f"""
  /////////////////////////////////////////////////////////////////

  Here's result --- >> {''.join(cipher_text)}

  ////////////////////////////////////////////////////////////////
        """
    )

    play_agein = input('Do you want try again? "yes" or "no": \n') == "yes"

    if play_agein:
        start_cipher()


start_cipher()

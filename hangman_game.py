import random

word_list = [
    "CRICKET", "SOCCER", "FOOTBALL", "WORCESTERSHIRE", "TEA",
    "SUPERCALIFRAGILISTICEXPIALIDOCIOUS", "BASEBALL",
    "RIBHAV", "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
    "ANISH", "YASHVIR", "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA",
    "RAJVIR", "SKIBIDI", "SIGMA", "FANUMTAX", "RIZZLER", "OHIO",
    "ZIPEI", "SIU", "LOSER", "ZESTY", "BRUH", "BANO", "TRASH",
    "USTED", "USUCK", "WASTED", "OTONO", "DEAD", "PYTHON",
    "QUAZJEX", "OOOOOOOOOMMMMMMMMMYYYYYYYYYYYYYYYYYYYYYYYYYYYYYGGGGGGGGGGGGGGGOOOOOOOOOOOOOOOOOOOODDDDDDDDDDDDDDDDDD",
]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

selected_word = random.choice(word_list)
progress = ["_"] * len(selected_word)
number_incorrect = 0
guessed_letters = []

while True:
    print(HANGMAN_STAGES[number_incorrect])
    print(*progress)
    print("Guessed Letters:", *guessed_letters)

    valid_letter = False
    while valid_letter == False:
        print("Guess a letter:")
        letter = input("> ").upper()
        if letter in guessed_letters:
            print("You have already guessed this letter")
        elif letter.isalpha() and len(letter)==1:
            valid_letter = True
        else:
            print("Invalid letter, try again")

    guessed_letters.append(letter)

    for i in range(len(selected_word)): # _ _ _ _ _ _ _ to _ a _ _ _ _ _
        if selected_word[i] == letter:
            progress[i] = letter
    
    if not letter in selected_word:
        number_incorrect += 1
    
    if number_incorrect == 6:
        print(HANGMAN_STAGES[6])
        print("You lost! The word was " + selected_word)
        break

    if not "_" in progress:
        print(HANGMAN_STAGES[number_incorrect])
        print("You won? The word was " + selected_word)
        break
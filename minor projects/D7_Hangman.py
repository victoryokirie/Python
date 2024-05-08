#step 1
import random
word_list = ["adventure", "promise", "pomegranade"]

#choose a random word
chosen_word = random.choice(word_list)
print(chosen_word)
#create an empty list call display and let each hidden letter be represented by "_"
display = []

word_length = len(chosen_word)

lives = 6

for letter in chosen_word:
    display.append("_")
print(display)
#ask the user a guess a letter
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    #check if the letter guessed by the user is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Your guess {guess} is not in the chosen word")
        lives -=1
        if lives == 0:
            end_of_game= True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
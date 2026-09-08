
import random

print("Welcome to hangman game!")
tries = 8
words = ["apple", "chair", "water", "dog", "ground"]


chosen_word = random.choice(words) # ex: apple 
dashed_list = ["_" for item in chosen_word] # ex: '_', '_' , '_' ,'_' ,'_' 
joined = " ".join(dashed_list) # ex: _ _ _ _ _ 
print(joined)
while tries > 0:
    print(f"Tries left: {tries}")
    check = input("Guess the letter: ")

    if len(check) > 1:
        print("")
        print("Write only one character")
        continue

    if check in dashed_list:
        print("")
        print("That letter has already been guessed") 
        continue

    if check in chosen_word:
        for index, letter in enumerate(chosen_word):
            if check == letter: 
                dashed_list[index] = letter
                joined = "".join(dashed_list)
        if joined == chosen_word:
            print(joined)
            print("Congratulations, you won!")
            break
        print("")
        print(joined) # to print after loop ends
    else:
        print("")
        print(joined)
        print("Try Again")
        tries = tries - 1
        if tries == 0:
            print("No tries left")
            print(f"The word is {chosen_word}")

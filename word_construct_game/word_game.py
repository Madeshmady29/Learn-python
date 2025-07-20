import random
import nltk
from nltk.corpus import words

nltk.download('words')
english_words = set(words.words())

def generate_letters(n=7):
    return random.choices('abcdefghijklmnopqrstuvwxyz', k=n)
    
def is_valid_word(word, letters, english_words):
    word = word.lower()
    if word not in english_words:
        return False
    
    temp_letters = letters.copy()
    for letters in word:
        if letters in temp_letters:
            temp_letters.remove(letters)
        else:
            return False
    return True
    
def play_game():
    score = 0
    letters = generate_letters()
    print("Welcome to the word construction gane")
    print(f"Your letters are: {' '.join(letters)}")
    print("Construct a word using the letters provided.")

    while True:
        user_input = input("Your word: ").lower()
        if user_input == 'quit':
            break

        if is_valid_word(user_input, letters.copy(), english_words):
            print("Valid word!")
            score += len(user_input)
        else:
            print("Invalid word. Try again.")

        print(f"Your current score is: {score}\n")  

    print (f"Game over! Your final score is: {score}")

if __name__ == "__main__":
    play_game()


                    


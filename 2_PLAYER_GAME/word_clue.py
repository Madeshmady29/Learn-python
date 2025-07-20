import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def word_guess_game():
    print("Welcome to the Word Guess Game!")
    print("player 1: Enter a secret word and a clue.")
    secret_word = input("Enter the secret word: ").lower().strip()
    clue = input("Enter a clue for the secret word: ").strip()

    clear_screen()
    print("player 2: Try to guess the secret word!")
    print(f"Clue: {clue}")

    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts+1}/{max_attempts} - Your guess: ").lower().strip()
        if guess == secret_word:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            print("Incorrect guess. Try again.")
            attempts += 1

    if attempts == max_attempts:
        print(f"Game over! The secret word was '{secret_word}'")
    
if __name__ == "__main__":
     word_guess_game()

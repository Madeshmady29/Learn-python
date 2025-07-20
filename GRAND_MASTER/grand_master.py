import random
import time
import os

def generate_sequence(length):
    return [str(random.randint(0,9)) for _ in range(length)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    print("Welcome to the Memory Game!")
    print("Try to remember the sequence of numbers.")
    print("type 'exit' to quit the game at any time.")

    level = 1
    while True:
        sequence = generate_sequence(level)
        print(f"\nLevel {level}: Memorize this sequence:")
        print(" ".join(sequence))

        time.sleep(2 + level *0.2)
        clear_screen()

        user_input = input("Enter the sequence: ").strip()
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break
        if user_input == ' '.join(sequence):
            print("Correct! Moving to the next level.")
            level += 1
        else:
            print(f"Wrong! The correct sequence was: {' '.join(sequence)}")
            print(f"You reached level {level}. Game Over!")
            break

if __name__ == "__main__":
    play_game()


import random

def roll_dice():
    return random.randint(1, 12)

def main():
    print("Welcome to the Dice Roller Simulator!")

    while True:
        user_input = input("Press [R] to roll or [Q] to quit: ").lower()

        if user_input == 'r':
            result = roll_dice()

            print (f"you rolled a dice and got: {result}\n")
        elif user_input == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input, please try again.\n")
                  
if __name__ == "__main__":
    main()


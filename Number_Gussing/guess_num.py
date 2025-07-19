import  random
def number_gussing_game():
    print("Welcome to the number gussing game")
    print("I am thinking of a number between 1 and 100")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:

            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Enter a valid number")

if __name__ == "__main__":
    number_gussing_game()




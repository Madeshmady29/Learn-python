from datetime import datetime
def get_birthdate():
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_input, "%Y-%m-%d")
        return birth_date
    except ValueError:
        print("Invalid format. Please use YYYY-MM-DD.")
        return get_birthdate()
    
def calculate_age(birth_date):
    today = datetime.today()
    age =  today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age
def main():
    print("Welcome to the Age Calculator!")
    birth_date = get_birthdate()
    age = calculate_age(birth_date)
    print(f"You are {age} years old.")
if __name__ == "__main__":
    main()
    
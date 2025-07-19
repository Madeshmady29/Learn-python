import os

TASKS_FILE = 'tasks.txt'

def main():
    while True:
        print("\nTO-DO List")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Remove Tasks")
        print("4. Exit")

        choice = input ("Enter your choice: ")

        if choice == "1":
            print("adding tasks...")
        elif choice == "2":
            print("Showing tasks...")
        elif choice == "3":
            print("Removing tasks...")
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("your choice is not valid, please try again.")

if __name__ == "__main":
    main()

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("N tasks found.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate (tasks, 1):
            print(f"{i}. {task}")

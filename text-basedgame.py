
import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("Welcome to the world of Mercenary ")
    time.sleep(1)
    print("Your goal is to save a girl who is the daughter of the military chief.")
    time.sleep(1)

def choose_path():
    print("Choose your path:")
    print("1. Go to left (save the girl)")
    print("2. Go to right (Decline the job)")
    return input("Enter 1 or 2: ")

def left_path():
    print("You chose to go left.")
    time.sleep(1)
    print("You encounter number 1 ,who is one of the people who can kill people like us!")
    time.sleep(1)
    decision = input("Do you want to fight or run? (fight/run): ")
    if decision.lower() == "fight":
        print("You defeated the number 1 and continue your journey.")
        print("You save the military chief's daughter and the military chief give you some rewards")
        print("Congratulations! You have completed the adventure.")
        time.sleep(1)
    else:
        print("You run away from the number 1.")
    time.sleep(1)


def right_path():
    print("You chose to go right.")
    time.sleep(1)
    print("They captured you")
    time.sleep(1)
    print("The military chief gave order to kill you")
    time.sleep(1)
    print("You was being executed.")
    time.sleep(1)
    print("You died!")
    time.sleep(1)
    print("Game Over!")
    time.sleep(1)

def main():
    introduction()

    while True:
        choice = choose_path()

        if choice == "1":
            left_path()
        elif choice == "2":
            right_path()
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
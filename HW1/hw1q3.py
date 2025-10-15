#hw1q3.py
print("Hw1q3, Exploding Dice Simulator")

import random

# Global variables to track statistics
total_rolls = 0
roll_counts = [0, 0, 0, 0, 0, 0]  # indices 0-5 correspond to numbers 1-6
explosions = 0
trigger_number = 6  # the number that causes the die to explode

def roll_die():
    global total_rolls, explosions
    result = random.randint(1, 6)
    total_rolls += 1
    roll_counts[result - 1] += 1
    print(f"You rolled a {result}!", end='')

    # Check for explosion
    if result == trigger_number:
        explosions += 1
        print(" The die explodes!\n(Rolling again for explosion...)")
        roll_die()  # recursive roll for explosion
    else:
        print()  # newline for normal roll

def view_total_rolls():
    print(f"Total rolls made: {total_rolls}")

def view_statistics():
    print("Roll statistics:")
    for i in range(6):
        count = roll_counts[i]
        # Calculate percentage
        percentage = (count / total_rolls * 100) if total_rolls > 0 else 0
        line = f"Number {i+1}: Rolled {count} times ({percentage:.2f}%)"
        # Add explosion note if it's the trigger number
        if i+1 == trigger_number:
            line += f" with {explosions} explosions"
        print(line)

def main():
    while True:
        print("\nMenu:")
        print("1. Roll Dice")
        print("2. View Total Rolls")
        print("3. View Roll Statistics")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            roll_die()
        elif choice == '2':
            view_total_rolls()
        elif choice == '3':
            view_statistics()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
MIN_SCORE = 0
MAX_SCORE = 10

# Get a list of scores from the keyboard
def get_score_list():
    while True:
        try:
            scores = list(map(int, input(f"Enter scores between {MIN_SCORE} and {MAX_SCORE}, separated by spaces: ").split()))
            # validate scores
            if all(MIN_SCORE <= s <= MAX_SCORE for s in scores):
                return scores
            else:
                print(f"All scores must be between {MIN_SCORE} and {MAX_SCORE}. Try again.")
        except ValueError:
            print("Please enter only integers separated by spaces.")

# Find the smallest, largest, sum, average and mode
def process_scores(score_list):
    if not score_list:
        return None, None, 0, 0, None

    smallest = min(score_list)
    largest = max(score_list)
    total = sum(score_list)
    average = total / len(score_list)
    mode = max(set(score_list), key=score_list.count)

    return smallest, largest, total, average, mode

def show_menu():
    print("\n=== MENU ===")
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the total of scores")
    print("4. Find the average score")
    print("5. Find the mode (most frequent) score")
    print("6. Exit")

def main():
    print("Finding the smallest, largest, sum, average or mode")

    score_list = get_score_list()
    sm, lg, total, average, mode = process_scores(score_list)

    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("The smallest score is", sm)
            elif choice == 2:
                print("The largest score is", lg)
            elif choice == 3:
                print("The total of scores is", total)
            elif choice == 4:
                print("The average score is", f"{average:.2f}")
            elif choice == 5:
                print("The mode (most frequent) score is", mode)
            elif choice == 6:
                print("Bye")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
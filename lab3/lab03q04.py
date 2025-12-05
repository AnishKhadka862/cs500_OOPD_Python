def print_table(foods, votes):
    print("\nFOOD            LIKE   DISLIKE")
    print("-------------------------------")
    for i in range(len(foods)):
        print(f"{foods[i]:12}   {votes[i][0]:<5}  {votes[i][1]}")


def cafeteria_survey():
    foods = ["Pizza", "Hot Dog", "Ham", "Cheese"]
    votes = [[0, 0],   # [like, dislike]
             [0, 0],
             [0, 0],
             [0, 0]]

    while True:
        print_table(foods, votes)

        print("\nWhich food do you want to vote on?")
        for i in range(len(foods)):
            print(f"{i+1}. {foods[i]}")

        print("5. Exit")

        choice = int(input("Enter choice: "))
        if choice == 5:
            break

        if choice < 1 or choice > 5:
            print("Invalid choice.")
            continue

        print("1. Like")
        print("2. Dislike")
        vote = int(input("Enter your vote: "))

        if vote == 1:
            votes[choice-1][0] += 1
        elif vote == 2:
            votes[choice-1][1] += 1
        else:
            print("Invalid vote")


cafeteria_survey()
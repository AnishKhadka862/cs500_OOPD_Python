def get_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest


def get_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


def get_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total


def get_average(lst):
    return get_sum(lst) / len(lst)


def get_mode(lst):
    # Build frequency array
    # Since scores are unknown, find max value
    max_val = lst[0]
    for n in lst:
        if n > max_val:
            max_val = n

    freq = [0] * (max_val + 1)

    for n in lst:
        freq[n] += 1

    # Find the most frequent
    mode = 0
    highest_count = freq[0]

    for i in range(len(freq)):
        if freq[i] > highest_count:
            highest_count = freq[i]
            mode = i

    return mode


def menu():
    scores = []
    count = int(input("How many scores? "))

    for _ in range(count):
        scores.append(int(input("Enter score: ")))

    print("\n1. Smallest")
    print("2. Largest")
    print("3. Sum")
    print("4. Average")
    print("5. Mode")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Smallest =", get_smallest(scores))
    elif choice == 2:
        print("Largest =", get_largest(scores))
    elif choice == 3:
        print("Sum =", get_sum(scores))
    elif choice == 4:
        print("Average =", get_average(scores))
    elif choice == 5:
        print("Mode =", get_mode(scores))
    else:
        print("ERROR: Invalid choice")


menu()
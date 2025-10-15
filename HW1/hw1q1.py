# hw1q1.py
print("Hw1q1, Letter to Digit Decipher")

#assign groups of letters to digits
group_1 = ['A', 'D', 'G', 'J', 'M']
group_2 = ['E', 'F', 'T', 'U', 'V']
group_3 = ['B', 'E', 'K', 'L', 'O']
group_4 = ['H', 'S', 'W', 'X', 'Y']
group_5 = ['C', 'F', 'N', 'P', 'Q']
group_6 = ['I', 'Y', 'Z']
group_7 = ['H', 'I', 'R', 'S', 'T']
group_8 = ['Z']

# user input
letter = input("Enter a letter to decipher: ")

# echo print
print("You entered:", letter)

# check for valid uppercase letter
if len(letter) != 1 or not letter.isupper():
    print("No matching digit exists for this character.")
else:
    possible_digits = []

    # Check which groups contain the letter in the list
    if letter in group_1:
        possible_digits.append(1)
    if letter in group_2:
        possible_digits.append(2)
    if letter in group_3:
        possible_digits.append(3)
    if letter in group_4:
        possible_digits.append(4)
    if letter in group_5:
        possible_digits.append(5)
    if letter in group_6:
        possible_digits.append(6)
    if letter in group_7:
        possible_digits.append(7)
    if letter in group_8:
        possible_digits.append(8)

    if possible_digits:
        # If multiple digits, return the largest
        print("The corresponding digit is", max(possible_digits))
    else:
        print("No matching digit exists for this character.")
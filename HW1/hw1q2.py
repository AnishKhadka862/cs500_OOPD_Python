#hw1q2.py
print("Hw1q2, five-character Palindrome Checker")

# ask for user input
s = input("Enter a five-character string: ")

# Check input length
if len(s) != 5:
    print("Error: Invalid input: Please enter a five-character string.")
else:
    # Convert string to list for modification
    chars = list(s)
    
    # Track mismatches
    mismatches = []

    # Check pairs manually (0-based indices)
    if chars[0] != chars[4]:
        mismatches.append((0, 4))
    if chars[1] != chars[3]:
        mismatches.append((1, 3))

    if len(mismatches) == 0:
        print(s, "is already a palindrome.")
    elif len(mismatches) == 1:
        # Only one mismatch → can fix with one replacement
        i, j = mismatches[0]
        # Replace left index to match right
        replacement_index = i + 1  # report as 1-based index
        replacement_char = chars[j]
        chars[i] = chars[j]
        print(f"{s} is not a palindrome. Replace character {replacement_index} with '{replacement_char}' to make it become a palindrome.")
        
        # Convert to uppercase manually
        revised_string = ''
        for c in chars:
            if 'a' <= c <= 'z':
                revised_string += chr(ord(c) - ord('a') + ord('A'))
            else:
                revised_string += c
        print("Revised string with uppercase:", revised_string)
    else:
        # More than one mismatch → cannot fix with single replacement
        print(f"{s} is not a palindrome. No single character replacement can make it one.")
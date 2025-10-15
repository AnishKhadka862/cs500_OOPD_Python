#lab 01 question 01
print("Lab 01 Question 02: Check if the input string is palindrome or not ")

string = input("Enter a string: ")

left = 0
right = len(string) - 1
is_palindrome = True
#I used a while loop that checks each character at the beginining and the end until they meet
while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

#if we encounter any unmatched character, the input string is not a palindrome
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
#lab 01 question 01
print("Lab 01 Question 01: Capitalize each word and add fullstop at th end if there is none")

#prompt user for a sentence
str_input = input("please enter a sentence: ")

#process each character to capitalize the first letter of the word
result = ""
pre = " "

for ch in str_input:
    if pre == " " and ch != " ":
        result += ch.capitalize()
    else:
        result += ch
    pre = ch
    
#print the result string
print("The output is " , result + ".")

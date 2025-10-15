#lab02q03
print("Word List Processor\n")

words = []

# Input loop
while True:
    word = input("Enter a word: ")
    if word == "Exit" or word == "exit":
        break
    words.append(word)

# Print original list
print("original list:")
print(words)

# print sorted list
sorted_list = sorted(words)
print("sorted list:")
print(sorted_list)


print("unique words:")

for i in range(len(words)):
    duplicate_found = False
    for j in range(i):
        if words[i] == words[j]:
            duplicate_found = True
            break
    if not duplicate_found:
        print(words[i], end=",")
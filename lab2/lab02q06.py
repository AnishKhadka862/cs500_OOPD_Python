#lab02q06.py
print("Print a centered triangle of symbols")
def triangle_of_symbols(height, symbol):
    for i in range(height):
        # Number of symbols in current row
        num_symbols = 2 * i + 1
        # Number of spaces to center the symbols
        num_spaces = height - i - 1
        # Print spaces followed by symbols
        print(' ' * num_spaces + symbol * num_symbols)

def main():
    height = int(input("Enter the height: "))
    symbol = input("Enter the symbol: ")
    
    triangle_of_symbols(height, symbol)

# Call main function
if __name__ == "__main__":
    main()
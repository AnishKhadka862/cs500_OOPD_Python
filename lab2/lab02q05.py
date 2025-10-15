#lab02q05
print('Print a rectangle of symbols')
def rectangle_of_symbols(height, width, symbol):
    for i in range(height):
        # Print the symbol 'width' times in each row
        print(symbol * width)

def main():
    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))
    symbol = input("Enter the symbol: ")
    
    rectangle_of_symbols(height, width, symbol)

# Call the main function
if __name__ == "__main__":
    main()
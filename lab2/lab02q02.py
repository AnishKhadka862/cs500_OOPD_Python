# lab02q02
print("Certificate of Deposit (CD) calaculator\n")


# Prompt for user inputs
principal = float(input("Enter initial investment amount: "))
apy = float(input("Enter annual percentage yield (APY): "))
months = int(input("Enter number of months for the CD term: "))
frequency = input("Enter compounding frequency (monthly, quarterly, annually): ").strip().lower()

# Determine compounding periods per year
if frequency == "monthly":
    n = 12
elif frequency == "quarterly":
    n = 4
elif frequency == "annually":
    n = 1
else:
    print("Invalid compounding frequency, Please enter monthly, quarterly, or annually.")
    exit()

# Convert APY to decimal
r = apy / 100

print()
if frequency == "annually":
    print("Year    CD Value")
    print("------- --------")
else:
    print("Month   CD Value")
    print("------- --------")

for m in range(1, months + 1):
    if frequency == "monthly":
        # Compounds every month
        value = principal * (1 + r / n) ** m
    elif frequency == "quarterly":
        # Compounds every 3 months
        value = principal * (1 + r / n) ** (m // 3)
    elif frequency == "annually":
        # Compounds once per 12 months
        value = principal * (1 + r / n) ** (m // 12)

    # Print results (month or year depending on frequency)
    if frequency == "annually":
        print(f"{m:<7} ${value:,.2f}")
    else:
        print(f"{m:<7} ${value:,.2f}")
# Calculate and display total interest earned
final_value = value
total_interest = final_value - principal
print(f"\nTotal interest earned: ${total_interest:,.2f}")
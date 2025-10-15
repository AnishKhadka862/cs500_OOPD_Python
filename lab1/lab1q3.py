#lab 01 question 03
print("Lab 01 Question 03: A simple payroll system")

#Defined Constants
REG_WAGE = 14.5
REG_HOURS = 40
FIRST_5H_OT = REG_WAGE * 1.5
OVER_45_HOURS = REG_WAGE * 2.0
TAX_RATE = 0.28 

while True:
    hours = float(input("\nEnter the number of hours worked: "))

    #if <= that 40, just calculate with REG_WAGE
    if hours <= REG_HOURS:
        gross_pay = hours * REG_WAGE
        
    #if <= 45, calculate with REG_WAGE for first 40 hours, FIRST_5H_OT upto 45 hours
    elif hours <= REG_HOURS + 5:
        gross_pay = (REG_HOURS * REG_WAGE) + ((hours - REG_HOURS) * FIRST_5H_OT)
    #if more than 45 hours, REG_WAGE for first 40 hours, 1.5 times upto 45, 2 times above 45 hours
    else:
        gross_pay = (REG_HOURS * REG_WAGE) + (5 * FIRST_5H_OT) + ((hours - REG_HOURS - 5) * OVER_45_HOURS)

    taxes = gross_pay * TAX_RATE
    net_pay = gross_pay - taxes

    print("\n**Employee Pay Summary**\n")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Taxes Withheld (28%): ${taxes:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

    # Ask for another employee
    another = input("Do you have another employee (yes/no)? ").strip().lower()
    if another != "yes":
        print("Exiting payroll system...")
        break
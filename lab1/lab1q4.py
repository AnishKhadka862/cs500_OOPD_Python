#lab 01 question 04
print("lab01q04: Movie Ticket Recipt\n")

#number of tickets for adult, child and senior
adult_tickets = int(input("Number of adult tickets: "))
child_tickets = int(input("Number of child tickets: "))
senior_tickets = int(input("Number of senior tickets: "))

#input for movie on weekday, weekend or holiday
day_type = input("Is the movie showing on a weekday (w), weekend (e), or holiday (h)? ").lower()

if day_type == "w":  #Weekday
    adult_price = 12.50
    child_price = 8.00
    senior_price = 9.00
else:  #Weekend (e) or Holiday (h)
    adult_price = 15.00
    child_price = 10.00
    senior_price = 11.50

subtotal = (adult_tickets * adult_price) + (child_tickets * child_price) + (senior_tickets * senior_price)

#Check and give 10% discount if 5 or more tickets
total_tickets = adult_tickets + child_tickets + senior_tickets
discount_rate = 0.10 if total_tickets >= 5 else 0
discount_amount = subtotal * discount_rate
total = subtotal - discount_amount

#Print Receipt
print("\nMovie Ticket Receipt\n")
print(f"Adult Tickets (x{adult_tickets}): ${adult_price:.2f} each")
print(f"Child Tickets (x{child_tickets}): ${child_price:.2f} each")
print(f"Senior Tickets (x{senior_tickets}): ${senior_price:.2f} each")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discount (5+ tickets): {int(discount_rate*100)}%")
print(f"Discount amount: ${discount_amount:.2f}")

print(f"\nTotal: ${total:.2f}")
print("\nThank you for coming to the movies!")
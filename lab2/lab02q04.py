#lab02q04
print("time shift calculator")

# Input time as two integers
hour = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59): "))
shift = int(input("Enter a time shift in mins: "))

# Convert to total minutes
total_minutes = hour * 60 + minute

# Calculate before and after
before_minutes = (total_minutes - shift) % (24 * 60)
after_minutes = (total_minutes + shift) % (24 * 60)

# Convert back
before_hour = before_minutes // 60
before_minute = before_minutes % 60
after_hour = after_minutes // 60
after_minute = after_minutes % 60

# Print results
print(f"{before_hour:02d}:{before_minute:02d}")
print(f"{after_hour:02d}:{after_minute:02d}")
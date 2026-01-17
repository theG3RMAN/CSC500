num_years = int(input("Enter the number of years: "))

total_rainfall = 0.0
total_months = num_years * 12

for year in range(1, num_years + 1):
    print(f"\nYear {year}:")

    for month in range(1, 13):
        rainfall = float(input(f"  Enter rainfall for month {month}: "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / total_months

print(f"\nNumber of months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds :"))
lots = float(input("Enter lots : "))
total_lots = (20*32*talents) + (pounds*32) + lots
total_grams = total_lots*13.3
kilograms = total_grams/1000
grams = total_grams % 1000
print(f"The weight is {kilograms}  kilograms and {grams} grams")
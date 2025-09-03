numbers = []
while True:
   number_enter = input("Enter a number(empty to quit):")
   if number_enter == "":
       break

   number = float(number_enter)
   numbers.append(number_enter)

numbers.sort(reverse=True)

greatest_numbers = numbers[:5]
print("Five greatest numbers are:", greatest_numbers)


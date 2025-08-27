zander_length = float(input("Please enter your zander length: "))
if zander_length >= 42 :
    print("The fish has caught")

else:
    print("The fish has released to the lake")
    difference = 42 - zander_length
    print(f"The zander is {difference} below")
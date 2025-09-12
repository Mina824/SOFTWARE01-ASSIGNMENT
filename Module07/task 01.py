seasons = ["Winter" , "Spring" , "Summer" , "Autumn"]

month = int(input("Enter the number of month (1-12): "))

if 1 <= month <= 12:
    if month in (12, 1, 2):
        season = seasons[0]
    elif month in (3, 4, 5):
        season = seasons[1]
    elif month in (6,7,8):
        season = seasons[2]
    else :
        season = seasons[3]

    print(f"The season is {season}.")
else:
    print(" Invalid input.")
gender = input("Enter a gender male/female: ")
if gender != "male" or "female":
    print("invalid gender")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))
if gender == "female":
    if hemoglobin_value < 117:
        print("The hemoglobin is low")
    elif hemoglobin_value > 155:
        print("The hemoglobin is high")
    else:
        print("The hemoglobin is normal")

if gender == "male":
    if hemoglobin_value < 134:
        print("The hemoglobin is low")
    elif hemoglobin_value > 164:
        print("The hemoglobin is high")
    else:
        print("The hemoglobin is normal")

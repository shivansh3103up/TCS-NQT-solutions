FEE_BELOW_17 = 200
FEE_17_TO_40 = 400
FEE_ABOVE_40 = 300
patient_ages = []
while True:
    age_input =input("Enter age value (press Enter without a value to stop): ")
    if age_input == "":
        break
    age = int(age_input)
    if 0 < age <= 120:
        patient_ages.append(age)
    else:
        print("Invalid age! Please enter a valid age between 1 and 120.")
total_earnings = 0
for age in patient_ages:
    if 0 < age < 17:
        total_earnings += FEE_BELOW_17
    elif 17 <= age <= 40:
        total_earnings += FEE_17_TO_40
    elif age > 40 and age <= 120:
        total_earnings += FEE_ABOVE_40
print("Total earning of the day are:",total_earnings)

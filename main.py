Weight = float(input("Enter your weight in (kg): "))
Height = float(input("Enter your height in (m): "))
bmi = Weight/Height **2
if bmi < 18.5:
    print("your bmi is:", rounded_bmi)
    print("underweight")

elif bmi < 18.5 and bmi > 25:
    print("your bmi is:", rounded_bmi)
    print("healthy")

elif bmi > 25 and bmi < 30:
    print("your bmi is:", rounded_bmi)
    print("overweight")

elif bmi > 30:
    print("your bmi is:", rounded_bmi)
    print("obese")

else:
    print("no reaction")


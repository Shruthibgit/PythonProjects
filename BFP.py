weight = 0
height = 0
age = 0

def bfp_calculator():
    height_meters = height * 0.3048  # converting to meters
    bmi = weight / (height_meters ** 2)
    print("Your BMI is ", round(bmi,2))

    if gend == 'm':
        bfp = (1.20*bmi)+(0.23*age)-16.2
        print("Your Body fat percentage = ", round(bfp,2))

    elif gend == 'f':
        bfp = (1.20 * bmi) + (0.23 * age) - 5.4
        print("Your Body fat percentage = ", round(bfp,2))

while True:
 try:
     weight = float(input("Enter you weight in kg: "))
     height = float(input("Enter you height in inches: "))
     age = int(input("Enter your age: "))
     gen = input("Enter your gender M/F: ")
     gend = gen.lower()
 except:
     print("Please enter the valid data!!!!")
     continue
 else:
     bfp_calculator()
 break

print("Thank you!!")

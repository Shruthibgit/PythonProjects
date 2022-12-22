weight = 0
height = 0
while True:
 try:
     weight = float(input("Enter you weight: "))
     height = float(input("Enter you hight: "))
 except:
     print("Please enter the valid data!!!!")
     continue
 else:
     bmi = weight / (height*height)
     print(f"You BMI is : {bmi} ")
     break

print("Thank you for using BMI calculator!!")
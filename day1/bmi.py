weight=float(input ("Enter weight(kg):"))
height=float(input ("Enter height(m):"))
bmi=weight/(height**2)
print("BMI=",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal Weight ")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")

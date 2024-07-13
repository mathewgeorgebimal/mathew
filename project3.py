"""Underweight:BMI less than 18.5
Normal weight:BMI between 18.5 and 24.9
Overweight:BMI between 25 and 29.9
Obesity:
Class I (Moderate obesity): BMI between 30 and 34.9
Class II (Severe obesity): BMI between 35 and 39.9
Class III (Very severe or morbid obesity): BMI of 40 and above"""

height = float(input("enter your height in meters"))
weight = float(input("enter your weight in kg"))
bmi = (weight)/(height*height)
if bmi < 18.5 and bmi > 0:
    print("you are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("you,re weight is normal")
elif bmi >= 25 and bmi <= 29.9:
    print("you aare overweight")
elif bmi >=30 :
    if bmi >= 30 and bmi <= 34.9:
        print("you are in class 1 obesity")
    elif bmi >=35 and bmi <=39.9:
        print("you are in class 2 obesity")
    else:
        print("you are in class 3 obesity")
else:
    print("type in correct height and weight")

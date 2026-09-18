#Control Block (if,elif,else,

#BMI Usecase -->BMI (Body Mass Index)

#weight --> kgs
#height --> metres
#feet -->12 inches --> inch --> 2.54cm

#BMI = (weight) / ((height)**2)

#weight = 75
'''
weight = float(input("Enter the weight in kgs:"))
height = float(input("ENter the height in inches:"))
bmi = (weight) / ((height)**2)
print(bmi)
'''
'''
no_of_to_user_input = int(input("Enter the Values:"))
for i in range(no_of_to_user_input):
    weight = float(input("Enter the weight in kgs:"))
    height = float(input("ENter the height in inches:"))
    name = input("Enter the name:")
    if weight > 0 and height > 0:
        bmi = (weight) / ((height)**2)
        if bmi < 18.5:
            print(f'{name} is into Underweight category and BMI is {bmi}')
        elif 18.5 <= bmi <= 24.9:
            print(f'{name} is into Normal Weight category and BMI is {bmi}')
        elif 25 <= bmi <= 29.9:
            print(f'{name} is into Overweight category and BMI is {bmi}')
        elif bmi >= 30:
            print(f'{name} is into Obesity category and BMI is {bmi}')
    else:
        print("Make Sure To Enter Only Positive Values..")
        
#Task --> Store the results of name,weight,height --> BMI into a collections
'''

#Repetitions --> while
#Same above task we need to handle the errors (Exception Handling) and also
#Make user strictly to enter only numeric values

while True:
    try:
        name = input("Enter Your Name:")
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in meters:"))
        if weight > 0 and height > 0:
            break
    except Exception as e:
        print(f'The Error is {e}')
bmi = (weight) / ((height)**2)
if bmi < 18.5:
    print(f'{name} is into Underweight category and BMI is {bmi}')
elif 18.5 <= bmi <= 24.9:
    print(f'{name} is into Normal Weight category and BMI is {bmi}')
elif 25 <= bmi <= 29.9:
    print(f'{name} is into Overweight category and BMI is {bmi}')
elif bmi >= 30:
    print(f'{name} is into Obesity category and BMI is {bmi}')
else:
    print("Make Sure To Enter Only Positive Values..")
                
     
            

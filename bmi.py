def BMI(height, weight) :
    bmi = weight/(height**2)

    if (bmi < 18.5) :
        return -1

    elif (bmi >= 18.5 and bmi <= 25) :
        return 0

    elif (bmi > 25) :
        return 1

height = float(input('Enter height: '))
weight = float(input('Enter weight: '))
value = BMI(height, weight)
print('You are '  + str(value))
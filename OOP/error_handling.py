# Error Handling
while True:
    age = input('What is your age? ')
    try:
        age = int(age)
        print(98/age)
        
    except ValueError:
        print('Please enter number')
    except ZeroDivisionError:
        print('Please enter age greater than zero')
    else:
        print('Thank you')
        break
    finally:
        print(f'User Entered \"{age}\" as age')

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)

print(sum(2,8))
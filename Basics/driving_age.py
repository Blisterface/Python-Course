def check_driving_age(age=0):
    if int(age)<18:
        print('Sorry, you\'re too young to drive this car. Poweirng pff')
    elif int(age)>18:
        print('Powering on. Enjoy the ride!')
    elif int(age)==18:
        print('Congratulations on your first year of driving. Enjoy the ride')

#age = input('What is your age?: ')
if __name__ == '__main__':
    check_driving_age()
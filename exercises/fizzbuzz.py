fizz = 3
buzz = 5

for i in range(1,101):
    if i %(fizz*buzz)==0:
        print("FizzBuzz")
    elif i%fizz == 0:
        print("Fizz")
    elif i%buzz == 0:
        print("Buzz")
    else:
        print(i)
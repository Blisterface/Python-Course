# Read lines from a csv file and print out the information from the second line

file = open('csvdata.txt','r')
lines = [var.strip() for var in file.readlines()]
lines = lines[1:]
for line in lines:
    name,age,uni,deg = line.split(',')
    print(f'Name: {name}\t Age: {age}\t University: {uni}\t Degree: {deg}')
file.close()

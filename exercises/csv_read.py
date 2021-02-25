# Read lines from a csv file and print out the information from the second line

count = 0
file = open('csvdata.txt','r')
while True:
    line = file.readline()
    count+=1
    if not line:
        break
    print('Name: {}\t Age: {}\t University: {}\t Degree: {}'.format(line.split(',')))
file.close()

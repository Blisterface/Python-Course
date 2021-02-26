import json

file = open('friends_json.txt')

file_contents = json.load(file) # reads file and turn it into a dictionanry
file.close()
heading = "Name \t Age \t University \t Degree\n"
print(heading + "_"*2*len(heading))

for record in file_contents['friends']:
    print(f"{record['name']}\t {record['Age']}\t{record['University']}\t{record['Degree']}")


cars = [
    {'make': 'Ford', 'Model': 'Fiesta'},
    {'make': 'Ford', 'Model': 'Focus'},
    {'Make':'Volvo', 'Model':'XC40'},
    {'Make':'Volvo', 'Model':'XC60'},
    {'Make':'Volvo', 'Model':'XC90'},
    {'Make':'BMW', 'Model':'3 Series'},
]

json_dump = json.dumps(cars,indent=4)

with open('cars.json','w') as output:
    output.writelines(json_dump)
output.close()

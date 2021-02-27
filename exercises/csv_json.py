import json

with open('csv_file.txt','r') as file:
    file_contents = [line.strip() for line in file.readlines()]


lines = [line.split(',') for line in file_contents]

data = []
for line in lines:
    record = {'club':line[0],'country':line[2],'city':line[1]}
    data.append(record)
print(data)

with open('json_file_clubs.txt','w') as writer:
    json.dump(data,writer)

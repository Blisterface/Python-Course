# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into .txt
# Your code starts here:

import json

file = open('csv_file.txt','r')
file_lines = [line.strip() for line in file.readlines()]
file.close()
lines = [var.split(',') for var in file_lines]


clubs = []

for line in lines:
    club = {'club':line[0], 'city':line[1], 'country':line[2]}
    clubs.append(club)


file_writer = json.dumps(clubs,indent=4)

with open('json_file.txt','w') as writer:
    writer.writelines(file_writer)
writer.close()

# Ask user for a list of three friends
# For each friend, tell the user if whether they are nearby
# For each nearby friend, save their name in nearby.txt file


friends = open('people.txt','r')
names = friends.readlines()
friends.close()


print(names)

friends_list = []

print("Enter names of three friends to determine if they are in same neibourhood ")
for i in range(3):
    name = input(f"Enter the name of the {i}th name: ")
    friends_list.append(name)


nearby_friends = open('nearby.txt','a')
for line in names:
    friend = line.strip()
    if friend in friends_list:
        print(f'{friend} is nearby')
        nearby_friends.write(friend+'\n')


friend_ages = {'Rolf':24, 'Matt':23, 'Joe':32, 'Shun':30}

for name in friend_ages:
    print(name)
for name, age in friend_ages.items(): #destructuring the dictionary
    print(f'{name} is {age} years old')
for age in friend_ages.values():
    print(age)


friends = ['Joe','Sizwe','Matt','Andy','Gray']
last_seen_days = [4,3,8,12,8]

last_seen ={friends[i]:last_seen_days[i] for i in range(len(friends))}

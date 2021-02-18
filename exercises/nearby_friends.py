nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()
friend_name = input('Enter the name of your friend: ')
user_friends.add(friend_name)
nearby = nearby_people.intersection(user_friends)

print(nearby)
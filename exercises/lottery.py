lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name':'Raul',
        'numbers':{23, 7, 12, 9, 6}
    },
    {
      'name':'Dave',
      'numbers':{4, 8, 21, 6, 11}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

print(f"{players[0]['name']} got {len(players[0]['numbers'].intersection(lottery_numbers))} numbers correctly")
print(f"{players[1]['name']} got {len(players[1]['numbers'].intersection(lottery_numbers))} numbers correctly")
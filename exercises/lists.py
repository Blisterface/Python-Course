friends = [{"Joseph":32}, {"Mark":30}, {"Danny":29}]

print(friends[0])

people = [
    ["Rose",24],
    ["James",30],
    ["Anna",28],
    ["Joe",56]
]
print(people[2])

art = {"Rolf","Anne","Jen"}
science = {"Jen","Charlie","Mark"}

art_but_not_science = art.difference(science)
science_and_art = art.intersection(science)
print(art_but_not_science)
print(science_and_art)
class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()
super_list.append(3)
super_list.append(7)
super_list.append(6)
print(len(super_list))
print(super_list[0])
import os
my_file = open('data.txt','r')
file_content = my_file.read()
my_file.close()


name_list = file_content.split('\n')

print(name_list)
new_file = open('string.txt','a')

new_file.write("This is a new file.\n")

new_file.close()
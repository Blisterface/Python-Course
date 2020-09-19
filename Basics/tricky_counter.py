my_list = [1,2,3,4,5,6,7,8,9,10]
my_list_sum = 0
for i in my_list:
    my_list_sum+=i
#print(my_list_sum)

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
pixel = ''#initialise the pixel to an empty string
for y in picture:
    string=''
    for x in y:
        if x==0:
            pixel =' '
        else:
            pixel ='*'
        string +=pixel
    print(string)

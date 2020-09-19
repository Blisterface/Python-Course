performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2:00pm', 
                'Enchanted Elephants':'5:00pm'}
for performance,time in performances.items():
    print(performance,': ',time,sep='')

order = input("What would you like to see(Q to quit): ")
performance_list=[]
while(order.upper()!='Q'):
    found=performances.get(order)
    if found:
        performance_list.append(order)
    else:
        print(f'{order} is not in the list')
    order=input("Would you like to order anything else(Q to quit): ")

print(f'You are watching the following perfomances: {performance_list}')
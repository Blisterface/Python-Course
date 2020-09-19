performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}

schedule_file = open('schedule.txt','w')
for performance,time in performances.items():
    schedule_file.write(performance + ' - ' + time + '\n')
schedule_file.close()

performance_list = []
read_file = open('schedule.txt','r')
for line in read_file:
    line=line.strip()
    performance_list.append(line)
read_file.close()
print(performance_list)

stuff = {}
schedule_file = open('schedule.txt', 'r')
for line in schedule_file:
    (show,time)=line.split(' - ')
    time=time.strip()#remove leading spaces and line breaks
    stuff[show]=time
schedule_file.close()

for performance,time in stuff.items():
    print(performance + ': ' + time,sep='')
print(stuff)
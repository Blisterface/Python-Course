"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# Read the questions from the file

quest = open('questions.txt','r')
quest_line = [line.strip() for line in quest.readlines()]
quest.close()


#seperate the question and results
quest_list = [line.split('=') for line in quest_line]

# map the question to the result
actual_quest = {}
for var in quest_list:
    actual_quest[var[0]] = var[1]

score = 0
for var in actual_quest:
    ans = input(f'{var}=')
    if ans == actual_quest[var]:
        score+=1

output = open('result.txt','w') 
output.write(f'Your final score is {score}/{len(actual_quest)}.\n')
output.close()


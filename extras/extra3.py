import json

with open('../files/questions.json','r') as file:
    content = file.read()
    #print((content))
data = json.loads(content)
index = 0
correct = 0
#transforms json string to list
#print(type(data))
while index<len(data):
    element = data[index]
    print(element['question'])
    for i in element['options']:
        print(f"{element['options'].index(i)+1}-{i}")
    user_choice = input('Choose the correct answer:')
    if int(user_choice) == element['correct']:
        print('Congrats you have gotten the right answer')
        correct= correct+1
    else:
        print('Sorry you have gotten the wrong answer')
    index = index + 1
    continue

print(f"You have gotten {correct} of {len(data)} right")



#today_date= input("enter today's date:")
#mood = input('rate your mood from 1 to 10:')
#thoughts = input('Let us know about your thoughts:')

#file_path = f"../files/{today_date}.txt"
#with open(file_path,'w') as file:
    #file.write(mood+'\n'+thoughts)

user_password = input('enter a password:')
conditions = {}
if len(user_password)>8:
    conditions['length']=True
else:
    conditions['length']=False
digit=False
for i in user_password:
    if i.isdigit():
        digit=True
conditions['digits']=digit
uppercase=False
for i in user_password:
    if i.isupper():
        uppercase=True
conditions['uppercaseLetter']=uppercase
print(conditions.values())
print(all(conditions.values()))
if all(conditions.values()):
    print('Strong password')
else:
    print('weak password')


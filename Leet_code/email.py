
#import email.utils
import re

n= int(input())
users =dict()
for i in range(n):
    temp = input()
    temp =temp.split(' ')
  #  print(temp)
    users[temp[0]]=temp[1]

#print(users)
print('output :')
for key, value in users.items():
    #print(value)
    if re.match(r'<[A-Za-z]([a-zA-Z0-9]|-|\.|_)*@[A-Za-z]*\.[A-Za-z]{1,3}>',value):
        print(key, value)

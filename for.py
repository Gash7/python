import random
#Count of Head
result=['Head','Tail','Head','Tail','Head','Tail','Head','Tail','Head','Tail','Head','Tail']
#abc=result.count('Head')
#print(abc)
count=0
for i in result:
    if i =='Head':
       count +=1

print(count)


for i in range(0,4):
    for j in range(0, 3):
        print('*',end='  ')

    print('\n')



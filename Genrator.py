n=eval(input('Enter the Number of students'))
d={}
for i in range(n):
        name=input('Enter student Name:')
        marks=input('Enter Student Marks')
        d[name]=marks

        print(d)

while True:
    name=input('Enter Student Marks')
    marks=d.get(name,-1)
    if marks==-1:
        print('Student Not Available')
    else:
        print('Marks of {}:{}'.format(name,marks))
    option=input('Do you want to add '
                 '')







'''
#WAP to find Vowels in string
word=input('Enter some word')
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,v)

word=input('Enter A string')
d={}

for x in word:
    d[x]=d.get(x,0)+1
print(d)
for k,v in sorted(d.items()):
    print('{} occuered {} times'.format(k,v))




iter=eval(input('Enter number of iterations'))
Student_Roll_number=input('Enter the Student Roll Number')
Student_Name=input('Enter Name of Student')
Student_Age=input('Enter Age of Student')
d={}
i=0

class Student:
    for i in range(0,iter):
     while i>=0:
        d[Student_Roll_number]=[[Student_Name,Student_Age]]
        print('Dict in while',d)
        i+=1
        break

     else:
        print('Iteration over')
#print(Student.__dict__)
print(d)





roll_no=input('Enter roll number=')
Name_of_studet=input('Name of student')
Age_of_student=input('Age of Student')
dict={}
dict[roll_no]=(Name_of_studet,Age_of_student)
print(dict)
'''

'''
Enter roll number=10
Name of studentAshish
Age of Student27
{'10': ('Ashish', '27')}
'''


'''
def generator():
 for i in range(6):
    yield i*i #yeild keyword is as Return.It returns genrator one iteration at a time

g = generator()
for i in g:
    print('Genrator',i)

'''
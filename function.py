def outer():
    print('Outer Function Started')
    def inner():
        print('Inner Function Executed')
    print('Outer function returning Innner Function')
    return inner

f1=outer()
f1()



'''

#WAP to add sum of intered number

def cal(name,*a):
    result=0
    for i in a:
        result +=i
    print('Sum Of Number',result,name)

cal('Ashish',80,90,20)
cal('Amit',98,10)
cal('Yogesh',65,35,45,30)
cal('Sagar',65,648,6214,6546,6548,50)
cal('Akshay',65,65,80)
cal('Krishna')

'''






'''
#WAP to add sum of intered number'''
def cal(*a,name):
    result=0
    for i in a:
     result +=i
    print('Sum Of Number',result,name)

cal(10,80,90,name=20)
cal(98,name=10)
cal(65,35,45,name=30)
cal(65,648,6214,6546,6548,name=50)
cal(65,65,name=80)
cal(name='Ashish')

'''



'''

def cal(a,b):#If number of Arguments incersed then it not possible to change.It takes only two..
    sum=a+b
    return sum


print(cal(10, 20))
'''


def wish(name='Guest',Add='Pune'):pass#Can't add non Default argumemt follow default argument

def wish(name='Guest',Add):pass#Can't add non Default argumemt follow default argument

def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=cal(10,20)
for x in t:
    print(x) 
'''
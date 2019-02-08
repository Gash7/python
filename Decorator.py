#use---Without modyfying existing function,if you want to extended functionality then DECORATOR is used.
#A decorator is a Function which can take other function as input and provide output function with extended fuctionality.
def smartdivision(function):
    def inner(a,b):
        if b==0:
            print('Hello It is not possible')
        else:
            return function(a,b)
    return inner

@smartdivision
def division(a,b):
    return a/b

print(division(10,5))
print(division(10,2))
print(division(10,0))


def decor(func):
    def inner(name):
        if name=='John':
            print('Hello John')
        else:
            func(name)
    return inner


@decor
def wish(name):
    print('Hello',name,'Good Morning')
wish('Ashish')
wish('Amit')
wish('John')
class Vector:

    def __init__(self,Name,Add,State):
        self.name = Name
        self.add = Add
        self.state = State

    def showDetails(self):
        return 'Name of Person:{}\n' \
               'Address of Person:{}\n' \
               'State of Person:{}\n'.format(self.name,self.add,self.state)

p1 = Vector('A','Pune','Maharashtra')
p2 = Vector('B','Mumbai','Maharashtra')
print(p1.__dict__)
print(p1.showDetails())
print(p2.__dict__)
print(p2.showDetails())
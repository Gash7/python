class remoteControl():

    def __init__(self):
        self.channels =['HBO','CNN','IBN','ABP']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

c=remoteControl()
print(next(c))
print(next(c))
print(next(c))
print(next(c))

class CRange():
    current =0
    def __init__(self,last,first=0):
        self.first=first
        self.last=last
    def __iter__(self):
        return self
    def __next__(self):
        if CRange.current<self.last:
            num = CRange.current
            CRange.current +=1
            return num
        raise StopIteration

gen = CRange(50)
for i in gen:
    print(i**2)
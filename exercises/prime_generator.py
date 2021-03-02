class PrimeGenerator:
    def __init__(self,stop):
        self.stop = stop
        self.start = 2


    def __next__(self):
        for x in range(self.start,self.stop):
            for n in range(2,x):
                if x % n == 0:
                    break
                else:
                    self.start = x + 1
                    return x
        raise StopIteration()


primes = PrimeGenerator(20)


while primes!=None:
    print(next(primes))


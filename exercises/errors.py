class Car:
    def __init__(self,make, model):
        self.make = make
        self.model = model
class Garage:
    def __init__(self):
        self.cars=[]
    

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"


    def __len__(self):
        return len(self.cars)
    

    def add_cars(self,car):
        if not isinstance(car,Car):
            raise TypeError(f"Adding {car.__class__.__name__} to 'Car' objects.")
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford','Fiesta')
ford.add_cars(fiesta)


print(len(ford))


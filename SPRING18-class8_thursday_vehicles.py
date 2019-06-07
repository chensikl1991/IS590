"""
IS590PR Thursday Spring 2018

Example of developing a custom class and subclasses with
inheritance, to represent various types of Vehicles.
"""

from collections import Counter


class Vehicle:

    # This is a PROTECTED class variable.
    __number_of_vehicles = Counter()

    def __init__(self, brand, model, year, fuel_type='gasoline'):
        Vehicle.__number_of_vehicles[self.__class__] += 1
        self.brand = brand
        self.model = model
        self.year = year
        self.__fuel_type = fuel_type

    def __del__(self):
        Vehicle.__number_of_vehicles[self.__class__] -= 1


    @classmethod
    def number_of(cls):
        if cls != Vehicle:
            return Vehicle.__number_of_vehicles[cls]
        else:
            return sum(Vehicle.__number_of_vehicles.values())

    @property
    def fuel_type(self):
        return self.__fuel_type

    def move(self, how='drive'):
        pass

    def refuel(self, quantity: float):
        pass


class Car(Vehicle):
    pass


class Boat(Vehicle):
    pass

class Airplane(Vehicle):
    pass


if __name__ == '__main__':

    print(Car.number_of())
    # Car.number_of_cars = 8
    johns_truck = Car('Ford', 'F150', 2018)

    print('fuel type: ', johns_truck.fuel_type)
    johns_truck.__fuel_type = 'hybrid'
    print('fuel type: ', johns_truck.fuel_type)


    print('!!!#cars', johns_truck.number_of())
    johns_car = Car('Subaru', 'Outback', 2015)
    print('#cars', Car.number_of())

    print(johns_truck.fuel_type)

    johns_canoe = Boat('Coleman', '15-foot', 1990)
    print('#cars', Car.number_of())
    print('#boats', Boat.number_of())

    print('#vehicles', Vehicle.number_of())

    johns_sailboat = Boat('Sailing Sloop', '40\'', 2010)   # just wishful thinking...
    print('#cars', Car.number_of())
    print('#boats', Boat.number_of())

    print('#vehicles', Vehicle.number_of())

    jet = Airplane('McDonald-Douglass', 'DC10', 1990)

    jet.refuel(quantity=2000)
    Airplane.refuel(jet, quantity=2000)

    print('# planes', Airplane.number_of())

    del jet
    print('# planes', Airplane.number_of())

    jet.refuel(20)
class Car (object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price>10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        print(self.displayAll())
    def displayAll (self):
        info = 'Price: ' + str(self.price) + "\nSpeed: " + str(self.speed) + "mph\nFuel: " + self.fuel + "\nMileage: " + str(self.mileage) + "mpg\nTax: " + str(self.tax) + "\n"
        return info

car1 = Car (2000, 35, 'Full', 15)
car2 = Car (3000, 50, 'Full', 16)
car3 = Car (5000, 70, 'Full', 18)
car4 = Car (10000, 100, 'Half-way full', 30)
car5 = Car (20000, 150, 'Kind of empty', 24)
car6 = Car (500000, 200, 'Empty', 100)
class Bike(object):

    def __init__ (self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.miles = 0
    def displayInfo (self):
        print "This bike's price is:", self.price
        print "This bike's maximum speed is:", self.maxSpeed
        print "This bike's has been ridden by ", self.miles, "miles"
        return self
    def ride (self):
        print 'Riding!'
        self.miles += 10
        return self
    def reverse (self):
        print 'Reversing!'
        if (self.miles > 0):
            self.miles -= 5
        else:
            print '0 current miles, cannot reverse anymore!'
        return self
    
bike1 = Bike(100, 50)
# bike1.displayInfo()
bike2 = Bike(200, 70)
# bike2.displayInfo()
bike3 = Bike(500, 100)
# bike3.displayInfo()

bike1.ride().ride().ride().reverse().displayInfo()
bike2.reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
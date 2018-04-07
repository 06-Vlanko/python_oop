class Product(object):
    def __init__ (self, item_name, brand, price, weight):
        self.item_name = item_name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.status = 'for sale'
    def sell (self):
        if self.status == 'sold':
            print self.item_name, 'is sold out!'
        else:
            self.status = 'sold'
        return self
    def addTax (self, tax):
        return self.price*(1+tax)
    def returnItem (self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'like new':
            self.status = 'for sale'
        elif reason == 'open box':
            self.status = 'used'
            self.price = self.price*0.8
        else:
            print 'Invalid return code'
        return self
    def displayInfo (self):
        print 'Item Name:', self.item_name
        print 'Brand:', self.brand
        print 'Weight (lb):', self.weight
        print 'Price ($):', self.price
        print 'Current status:', self.status
        print ''
        return self

cheapWine = Product('Wine 123','Patito',150,1.5)
potatoChips = Product('Mega Chips', 'Umbrella', 5, 0.3)
rocket = Product ('Awesome rocket', 'Acme', 3000, 50)

cheapWine.displayInfo().sell().displayInfo().sell().returnItem('defective').displayInfo()
# potatoChips.displayInfo()
# rocket.displayInfo()
class MathDojo (object):
    result = 0.0
    def __init__(self):
        pass
    def add (self, *args):
        for element in args:
            print element
            if type(element) == list or type(element) == tuple:
                for each in element:
                    MathDojo.result += each
            else:
                MathDojo.result += element
        return self
    def subtract (self, *args):
        for element in args:
            if type(element) == list or type(element) == tuple:
                for each in element:
                    MathDojo.result -= each
            else:
                MathDojo.result -= element
        
        return self

thing = MathDojo()
print thing.add([1],(3.4)).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], (1.1,2.3)).result
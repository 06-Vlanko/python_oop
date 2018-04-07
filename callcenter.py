class Call (object):
    def __init__ (self, callId, callerName, callerPhone, timeOfCall, reasonOfCall):
        self.callId = callId
        self.callerName = callerName
        self.callerPhone = callerPhone
        self.timeOfCall = timeOfCall
        self.reasonOfCall = reasonOfCall
    def display (self):
        print 'Call ID:', self.callId
        print "Caller's name:", self.callerName
        print "Caller's phone:", self.callerPhone
        print 'Time of call:', self.timeOfCall
        print 'Reason of call:', self.reasonOfCall
        print ''
        return self

class CallCenter (object):
    def __init__(self):
        self.callList = []
        self.queue = len(self.callList)
    def add (self, newCall):
        self.callList.append(newCall)
        return self
    def remove (self):
        del self.callList[0]
        return self
    def info (self):
        for element in self.callList:
            print 'Name:', element.callerName
            print 'Phone', element.callerPhone
        return self
    def removeByPhone (self, phone):
        for element in self.callList:
            if element.callerPhone == phone:
                del self.callList [self.callList.index(element)]
        return self
    def sortByTime (self):
        self.callList.sort(key =lambda call: call.timeOfCall)
        return self
call1 = Call (1, 'Elena', '123-123', 11.08, 'for funsies')
call2 = Call (2, 'Alexx', '456-456', 11.09, 'seriousss businesss')
call3 = Call (3, 'Pablo', '789-789', 11.10, '3D printing hype')

cs = CallCenter ()
cs.add (call3).add (call1).add (call2).add (call1).info().removeByPhone('123-123').info()
print ''
cs.sortByTime().info()
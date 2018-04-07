#previously used for the random ID generator which is no longer being used, leaving it for self-notes
# import string
# import random

class Patient (object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bedNumber = 0
    #prints the attributes of the object
    def printInfo (self):
        print '--------------------------------'
        print 'ID:', self.id, 'Name:', self.name, 'Bed Number', self.bedNumber
        print 'Allergies:', self.allergies
        return self

#class hospital holds patients
class Hospital (object):
    def __init__(self, name, capacity):
        self.patientList = []
        self.name = name
        self.capacity = capacity
    
    #ID generator, not in use as it was decided patients will provide their own ID to the hospital
    # def idGenerator(self, size = 6, chars = string.ascii_uppercase + string.digits):
    #     return ''.join (random.choice (chars) for _ in range(size))
    
    #admits a patient into the hospital, if it is not full it will add the new patient to the patient list
    #it will assign an available bed# to the new patient using bedAsigner
    def admit (self, patient):
        if len (self.patientList) < self.capacity:
            self.patientList.append (patient)
            print 'Admitted', patient.name + '. Max capacity:', self.capacity,  'Remaining capacity:', self.capacity - len (self.patientList)
            self.bedAsigner (patient)
        else:
            print 'Unable to admit', patient.name, 'because the hospital is full'
        return self
    #checks which beds are being used by the current patients in the hospital and will assign the first bed number available to 'patient'
    # >>>>>>>>>>>>> REMOVE COUNTER CUZ WE CAN USE INDEX+1
    def bedAsigner (self, patient):
        self.counter = 1
        for index in range ( len(self.patientList) ):
            if self.counter == self.patientList[index].bedNumber:
                self.counter += 1
            else:
                patient.bedNumber = self.counter
    #finds a patient in the patientList list and the removes him/her
    def discharge(self, patientId):
        for x in self.patientList:
            if x.id == patientId:
                x.bedNumber = 9999
                del self.patientList [self.patientList.index(x)]
                print '\nDischarged:', x.name
        return self
    #prints the hospital info as well as the info of the current patients in the hospital
    def printPatientList (self):
        self.printHospitalInfo()
        print 'PATIENTS LIST:'
        for element in self.patientList:
            element.printInfo()
        return self
    def printHospitalInfo (self):
        print "\nHOSPITAL'S NAME:", self.name.upper(), '----> MAX CAPACITY:', self.capacity
        return self

patient1 = Patient (101,'Stheve','bad food')
patient2 = Patient (202, 'Pablo','boredom')
patient3 = Patient (303, 'Javier','slow speeds')
patient4 = Patient (404, 'Victor','repetition')

hospital1 = Hospital ('Homey', 3)
hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4).printPatientList()
hospital1.discharge(202)
hospital1.admit(patient4).discharge(101).admit(patient2).printPatientList()

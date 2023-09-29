class School():
    
    def classes(self, Primary, Middle, High):
        self.Primary = Primary
        self.Middle = Middle
        self.High = High

    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):

        return self.name
    
    def get_Level(self):

        return self.level
    
    def get_numberOfStudents(self):

        return self.numberOfStudents
    
    def set_numberOfStudents(self, number):

        self.numberOfStudents = number

    def __repr__(self):

        return (f'A {self.level} school named {self.name} with {self.numberOfStudents} students')
    
class PrimarySchool(School):

    def __init__(self, name, numberOfStudents, pickupPolicy):

        super().__init__(name, 'Primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):

        return self.pickupPolicy
    
    def __repr__(self):

        return super().__repr__() + (f' and a pickup Policy of {self.pickupPolicy}.')
    
school1 = School("Test school", "Middle", 1000)
print(school1)

school2 = PrimarySchool('some stupid children school', 500, 'parents pick up their child, otherwhise the child will become a part of the school lunch.')
print(school2)
    

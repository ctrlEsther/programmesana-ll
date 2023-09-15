class Student():

    def information(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        self.grade = grade

    def get_average(self, score):
        self.get_average = average_score
        return print(average_score)


student = Student()

class Grade():
    minimum_passing = 65

    def score(self, score):
        self.score = score
    
    def passing(self, score):
        if score > 64:
            return print('grade is passing')
        else:
            return print('failed grade')
        
grade = Grade()

roger = student.information('Roger van der Weyden', 'year 10')
sandro = student.information('Sandro Botticelli', 'year 12')
pieter = student.information('Pieter Bruegel', 'year 8')
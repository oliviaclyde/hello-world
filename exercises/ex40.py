#first class example
"""
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
"""

#If you create a class but haven't finished it yet you can put "pass" and Python will ignore it
class Test(object):
    pass


#Writing my own class
class Car:
    def __init__(self, wheels, doors, windows, engine):
        self.wheels = wheels
        self.doors = doors
        self.windows = windows
        self.engine = engine

    def drive(self):
        print("All parts assembled. Ready to go!")
        print(self.wheels)



trip = Car('Goodrich', '4-door', 'automatic windows', 'supercharged' )
trip2 = Car('Ford', '2-door', 'no windows', 'poo' )

trip.drive()
trip2.drive()



"""
#Class vs. Instance of a class
#A class is a blueprint for creating instances
#i.e. Employee class and each employee is an instance of that class
#Instance variables contain data that is unique to each instance

#__init__ method
#Youtube video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&feature=youtu.be
#Create method inside a class
class Employee:
    #create __init__ method (constructor)
    def __init__(self, first, last, pay): #instance is the first argument automactially. Convention calls it "self"
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Olivia', 'Clyde', 60000)


print(emp_1.fullname())
print(Employee.fullname(emp_1))
"""

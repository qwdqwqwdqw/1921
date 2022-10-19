# class Student:
#     print("Hello")
#     def __init__(self):
#         self.height = 165
#         print("ok")
#
# first_student = Student()
# print(first_student)
# print(first_student.height)
# print(first_student.func(arg1, kwar1=1))

# class Student:
#     kolichestvo=0
#     def __init__(self, height):
#         self.height = height
#         Student.kolichestvo+=1
#
# nick = Student(height = 150)
# kate = Student(height = 160)
# print(kate.height)
# print(nick.height)
# print(nick.kolichestvo)
# print(Student.kolichestvo)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def text(self):
#         return f"My name is {self.name}"
# nick = Student(name="Anton")
# print(nick.text())
import random

class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to Study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Self Time")
        self.gladness+=5
        self.progress-=0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cas Out")
            self.alive=False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 0:
            print("Passed externally")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

nick = Student(name = "Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)


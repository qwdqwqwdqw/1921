# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passangers = []
#     def add_passanger(self, *args):
#         for passanger in args:
#             self.passangers.append(passanger)
#     def print_passangers_names(self):
#         if self.passangers!= []:
#             print(f"Names {self.brand} passangers: ")
#             for passanger in self.passangers:
#                 print(passanger.name)
#         else:
#             print(f"There are no passangers in {self.brand}")
#
# Anton = Human("Anton")
# Yarik = Human("Yarik")
# car = Auto("Volswagen")
# car.add_passanger(Anton, Yarik)
# car.print_passangers_names()

import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        set.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >=100:
                self.satiety = 100
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <20:
                manage = "fuel"
            else:
                self.to_repair()
                return
            if manage == "fuel":
                print("I bought fuel")
                self.money -=100
                self.car.fuel += 100
            elif manage == "food":
                print("Bought food")
                self.money -=50
                self.home.food+=50
            elif manage == "delicacies":
                print("Hooray! Delicious!")
                self.gladness+=10
                self.satiety+=2
                self.money-=15

        def chill(self):
            self.gladness+=10
            self.home.mess+=5
        def clean_home(self):
            self.gladness -=5
            self.home.mess=0
        def to_repair(self):
            self.car_strength += 100
            self.home.money -= 50
        def days_indexes(self, day):
            day = f"Todat the {day} of {self.name}`s life"
            print(f"{day:=^50}","\n")
            human_indexes = self.name + "`s indexes"
            print(f"{human_indexes:=^50}","\n" )
            print(f"Money -{self.money}")
            print(f"Satiety - {self.satiety}")
            print(f"gladness - {self.gladness}")
            home_indexes = "Home indexes"
            print(f"{human_indexes:=^50}","\n" )
            print(f"Food - {self.food}")
            print(f"Mess - {self.mess}")
            car_indexes = f"{self.car.brand} car indexes"
            print(f"{human_indexes:=^50}","\n" )
            print(f"Fuel - {self.car.fuel}")
            print(f"Strenght - {self.car.strength}")
        def is_alive(self):
            if self.gladness<0:
                print("Depression")
                return False
            if self.satiety<0:
                print("Dead")
                return False
            if self.money<-500:
                print("Bankrupt")
                return False
        def live(self, day):
            if self.is_alive() == False:
                return False
            if self.home is None:
                print("Settled in the house")
                self.get_home()
            if self.car is None:
                print(f"I bought car {self.car.brend}")
                self.get_car()
            if self.job is None:
                print(f"I have job {self.car.brend}")
                self.get_job()
            self.days_indexes(day)
            dice = random.randint(1,4)
            if self.satiety<20:
                print(f"I ill go eat")
                self.get_eat()
            elif self.money<0:
                print(f"Im poor")
                self.get_eat()
            elif self.car.strenght<15:
                print(f"I need to repair my car")
                self.get_repair()
            elif dice == 1:
                print(f"Lets chill!")
                self.chill()
            elif dice == 2:
                print(f"Start Working")
                self.get_work()
            elif dice == 3:
                print(f"Cleaning time")
                self.clean_home()
            elif dice == 4:
                print(f"Time for threats!")
                self.shopping(manage="delicacies")
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]   

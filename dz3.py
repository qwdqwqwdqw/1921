import random

class Kachok:
    def __init__(self, kachatsa):
        self.kachatsa = kachatsa
        self.zratva = 2

class Gym:
    def __init__(self):
        self.kachatsa = 8
        self.kachok = kachok
    def gym(self):
        print("Opyat kachatsa")
        self.kachok.kalorii -= 50
    def magaz(self):
        print("Nyzna zratva")
        self.kachok.kalorii -= 10
        self.kachok.zratva += 5
        if self.kachok.kalorii <=200:
            print("Nyzno zratb")
            self.kachok.kalorii += 100
            self.kachok.zratva -= 2
    def nadoelo(self):
        print("Schas posmotry fytbol")
        self.kachok.zratva -= 4
    def live(self):
        cube = random.randint(1,2,3)
        if cube == 1:
            self.gym()
        elif cube == 2:
            self.magaz()
        elif cube == 3:
            self.nadoelo()

kachok = Kachok()
gym = Gym()
gym.live()

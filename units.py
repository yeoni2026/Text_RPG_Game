class Player:
    def __init__(self, name, type, hp = 30, power = 4):
        self.name = name
        self.type = type
        self.hp = hp
        self.power = power

    def show_info(self):
        print("이름: " + self.name)
        print("직업: " + self.type)
        print("hp: ", end='')

        for i in range(0, self.hp):
            print("▋", end='')
        print(" (" + str(self.hp)+ ")")
        print("공격력: " + str(self.power))

class Monster:
    def __init__(self, type = "슬라임", hp = 10, power = 3):
        self.type = type
        self.hp = hp
        self.power = power

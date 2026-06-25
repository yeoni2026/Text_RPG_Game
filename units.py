class Player:
    def __init__(self, name, type, hp, attack):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack

    def show_info(self):
        print("이름: " + self.name)
        print("직업: " + self.type)
        print("hp: ", end='')

        for i in range(0, self.hp):
            print("▋", end='')
        print(" (" + str(self.hp)+ ")")
        
        print("공격력: " + str(self.attack))

class Monster:
    def __init__(self, type, hp, attack):
        self.type = type
        self.hp = hp
        self.attack = attack


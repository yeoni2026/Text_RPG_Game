from units import  Monster
import sys

class Battle():
    def __init__(self, player):
        self.player = player
        self.monster = Monster()
    
        print(f"{self.monster.type}을(를) 만났습니다!")
        self.start_battle()

    def start_battle(self):
        while True:
            choice = int(input("1. 공격하기 2. 도망치기 : "))
            match(choice):
                case 1:
                    self.player.attack(self.monster)
                    if self.monster.hp <= 0:
                        print(f"{self.monster.type}을 처지했습니다!")
                        break                   
                    self.monster.attack(self.player)
                    if self.player.hp <= 0:
                        print(f"플레이어가 사망했습니다.. [게임오버]")
                        sys.exit()
                case 2: 
                    print("사냥터에서 도망쳤습니다!")
                    break
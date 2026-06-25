from units import  Monster
import sys


def start_battle(player):
    
    monster = Monster()
    print(f"{monster.type}을(를) 만났습니다!")
    
    while True:
        choice = int(input("1. 공격하기 2. 도망치기 : "))
        match(choice):
            case 1:
                player.attack(monster)
                if monster.hp <= 0:
                    print(f"{monster.type}을 처치했습니다!")
                    break                   
                monster.attack(player)
                if player.hp <= 0:
                    print(f"플레이어가 사망했습니다.. [게임오버]")
                    sys.exit()
            case 2: 
                print("사냥터에서 도망쳤습니다!")
                break
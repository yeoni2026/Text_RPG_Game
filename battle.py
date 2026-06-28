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
                print(f".\n.\n{monster.type}에게 {player.attack}데미지를 입혔습니다!")
                if monster.hp <= 0:
                    print(f".\n.\n{monster.type}을 처치했습니다!")
                    break

                monster.attack(player)   
                print(f".\n.\n{monster.type}이 반격했습니다!\n{monster.attack}데미지를 입었습니다.")
                if player.hp <= 0:
                    print(f"플레이어가 사망했습니다.. [게임오버]")
                    sys.exit()
            case 2: 
                print("사냥터에서 도망쳤습니다!")
                break
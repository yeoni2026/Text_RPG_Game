from service import create_player
from battle import start_battle
print("=== Text RPG 게임 ===")

player = create_player()

while True:
    menu = int(input("1. 사냥터 2. 내 정보 3. 종료 : "))
    match(menu):
        case 1: 
            start_battle(player)
        case 2: 
            player.show_info()
        case 3: 
            print("지금까지 상황을 저장하고 게임을 종료합니다.")
            break    
        case _: print("1~3사이의 숫자를 입력해주세요.")
        

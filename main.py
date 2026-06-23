from units import Player

print("=== Text RPG 게임 ===")
player = Player()
while True:
    menu = int(input("1. 사냥터 가기 2. 캐릭터 정보 3. 종료 : "))
    match(menu):
        case 1: pass
        case 2: 
            player.show_info()
        case 3: 
            print("게임을 종료합니다.")
            break
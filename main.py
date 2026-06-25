from service import create_player

print("=== Text RPG 게임 ===")

player = create_player()

while True:
    menu = int(input("1. 사냥터 가기 2. 캐릭터 정보 3. 종료 : "))
    match(menu):
        case 1: pass
        case 2: 
            player.show_info()
        case 3: 
            print("지금까지 상황을 저장하고 게임을 종료합니다.")
            break
          
        case _: print("1~3사이의 숫자를 입력해주세요.")
        

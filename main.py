from units import Player

print("=== Text RPG 게임 ===")
print("이름을 입력해주세요.")
player_name = input()

player = Player(player_name, "mage", 10, 1) 
player.name = player_name

print("직업을 선택하세요.")
job = int(input("1. 마법사 🧙\n2. 도적 🥷 \n3. 검사 ⚔️\n4. 잡상인 💎\n" ))
match(job):
            case 1: player.type = "마법사"
            case 2: player.type = "도적"
            case 3: player.type = "검사"
            case 4: player.type = "잡상인"
            case _: print("1~4까지의 숫자를 입력해주세요.")

while True:
    menu = int(input("1. 사냥터 가기 2. 캐릭터 정보 3. 종료 : "))
    match(menu):
        case 1: pass
        case 2: 
            player.show_info()
        case 3: 
            print("지금까지 상황을 저장하고 게임을 종료합니다.")
            break
          
        case _: print("1~3까지의 숫자를 입력해주세요.")
        

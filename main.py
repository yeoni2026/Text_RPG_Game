from service import create_player, load_player_data, save_player_data
from battle import start_battle

print("=== Text RPG 게임 ===")

try :
    player = load_player_data()
    print("저장된 데이터를 불러오기에 성공했습니다!")
except :
    print("기존 정보를 불러오는 데 실패했으므로 처음부터 시작합니다.")
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
            save_player_data(player)
            break    
        case _: print("1~3사이의 숫자를 입력해주세요.")
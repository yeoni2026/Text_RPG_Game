from units import Player

def create_player():
    player_name = input("이름을 입력해주세요 : ")

    job_dic = {1 : "마법사", 2 : "도적", 3 : "검사", 4 : "잡상인"}
    job = int(input("1. 마법사 🧙\n2. 도적 🥷 \n3. 검사 ⚔️\n4. 잡상인 💎\n직업을 선택하세요 : "))
    while True:
        if job not in [1, 2, 3, 4]:
            job = int(input(f"1에서 {len(job_dic)}사이의 숫자를 입력해주세요 : "))
            continue
        break
    return Player(player_name, job_dic[job])
    

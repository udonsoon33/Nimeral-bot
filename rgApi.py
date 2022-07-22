import json
import requests
from urllib import parse
import time

api_key = "RGAPI-21edaca7-0814-4426-bb20-37eda678134f"
request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-21edaca7-0814-4426-bb20-37eda678134f"
}


def tier(name):
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})

    if res.status_code == 200:
        # 코드가 200일때
        resobj = json.loads(res.text)
        URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + \
            resobj["id"]
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        rankinfo = json.loads(res.text)
        print("소환사 이름: "+name)
        for i in rankinfo:
            if i["queueType"] == "RANKED_SOLO_5x5":
                # 솔랭과 자랭중 솔랭
                print("솔로랭크:")
                print(f'티어: {i["tier"]} {i["rank"]}')
                print(f'승: {i["wins"]}판, 패: {i["losses"]}판')
            else:
                # 솔랭과 자랭중 자랭
                print("자유랭크:")
                print(f'티어: {i["tier"]} {i["rank"]}')
                print(f'승: {i["wins"]}판, 패: {i["losses"]}판')
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")


if __name__ == "__main__":
    selectnum = input("번호를 입력해주세요: ")

    if selectnum == "1":
        name = input("소환사의 닉네임을 입력해주세요: ")
        tier(name)

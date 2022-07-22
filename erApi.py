from asyncio.windows_events import NULL
import json
from pickle import FALSE
import requests
from urllib import parse
import time

api_key = "TqRQF3aWF79jIKt7xk0sk4brfX0yd7dq72d0SGFp"


def nick(name):
    URL = "https://open-api.bser.io/v1/user/nickname?query="+name
    res = requests.get(URL, headers={"x-api-key": api_key})

    if res.status_code == 200:
        # 코드가 200일때
        resobj = json.loads(res.text)
        return resobj["user"]["userNum"]
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("존재하지 않습니다")
        return NULL


def tier(name, season, pre):
    num = nick(name)
    seas = int(season) * 2 - (1 + int(pre))
    URL = "https://open-api.bser.io/v1/user/stats/" + \
        str(num) + "/" + str(seas)
    res = requests.get(URL, headers={"x-api-key": api_key})

    mmrStr = ""
    matchingTeamMode = []

    if res.status_code == 200:
        # 코드가 200일때
        resobj = json.loads(res.text)
        if(season == 0):
            mmrStr += "일반 게임 MMR\n"
        else:
            if pre == 1:
                mmrStr += "프리시즌 " + str(season) + " MMR\n"
            else:
                mmrStr += "시즌 " + str(season) + " MMR\n"
        if len(resobj["userStats"]) == 0:
            matchingTeamMode = []
        elif len(resobj["userStats"]) == 1:
            if(resobj["userStats"][0]["matchingTeamMode"] == 1):
                matchingTeamMode = [0]
            elif(resobj["userStats"][0]["matchingTeamMode"] == 2):
                matchingTeamMode = [1]
            else:
                matchingTeamMode = [2]
        elif len(resobj["userStats"]) == 2:
            if(resobj["userStats"][0]["matchingTeamMode"] == 1 and
               resobj["userStats"][1]["matchingTeamMode"] == 2):
                matchingTeamMode = [0, 1]
            elif(resobj["userStats"][0]["matchingTeamMode"] == 1 and
                    resobj["userStats"][1]["matchingTeamMode"] == 3):
                matchingTeamMode = [0, 2]
            else:
                matchingTeamMode = [1, 2]
        else:
            matchingTeamMode = [0, 1, 2]

        if len(matchingTeamMode) == 0:
            mmrStr += "랭크게임 플레이횟수 없음"
        else:
            n = 0
            for i in matchingTeamMode:
                if i == 0:
                    mmrStr += "솔로: " + \
                        str(resobj["userStats"][n]["mmr"]) + "\n"
                elif i == 1:
                    mmrStr += "듀오: " + \
                        str(resobj["userStats"][n]["mmr"]) + "\n"
                else:
                    mmrStr += "스쿼드: " + \
                        str(resobj["userStats"][n]["mmr"]) + "\n"
                n += 1
        return mmrStr
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("존재하지 않습니다")
        return NULL


if __name__ == "__main__":
    selectnum = input("번호를 입력해주세요: ")

    if selectnum == "1":
        name = input("닉네임을 입력해주세요: ")
        print(nick(name))
    if selectnum == "2":
        name = input("닉네임을 입력해주세요: ")
        season = input("시즌을 입력해주세요 (일반 게임은 0 입력): ")
        if season != 0:
            pre = input("프리 시즌입니까? (예: 1 / 아니요: 0): ")
        else:
            pre = 0
        print(tier(name, season, pre))

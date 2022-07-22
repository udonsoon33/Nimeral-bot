# discord 라이브러리 사용 선언
import discord
import traceback
import erApi
import pixivUrl
import pixivTag

TOKEN = "OTY5OTY2MTIzOTk3MDc3NTU0.Ym1FWQ.jGJgx8xAiv5QJ1UzouJHOJ7eI3c"


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("내용")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):

        # 현재 채널을 받아옴
        channel = message.channel

        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        # message에 이미지가 있을 경우
        if len(message.attachments) > 0 and message.attachments[0].content_type[0:5] == "image":
            try:
                pixiv_url = pixivUrl.get_url(
                    message.attachments[0].proxy_url)
                pixiv_id = pixivUrl.get_id(pixiv_url)
                pixiv_tag = (str(pixivTag.get_tags(int(pixiv_id))[0].name))
                if(pixiv_tag == "R-18"):
                    # 야한건 안돼!
                    # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
                    embed = discord.Embed(title="야한건 안돼!", color=0x62c1cc)
                    # 메시지 구역에 이미지 넣기
                    embed.set_image(
                        url="https://cdn.discordapp.com/attachments/969967027601149984/971057322803724328/unknown.png")
                    await channel.send(embed=embed)
            except:
                traceback.print_exc()

            return None

        # message.content = message의 내용
        if message.content == "!으헤":
            # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed = discord.Embed(color=0x62c1cc)
            # 메시지 구역에 이미지 넣기
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/969967027601149984/971058923224313866/unknown.png")
            await channel.send(embed=embed)
            return None

        # 이터널 리턴 MMR 조회
        if message.content[0:4] == "!mmr":
            msg = erApi.tier(message.content[5:], 6, 1)
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(TOKEN)

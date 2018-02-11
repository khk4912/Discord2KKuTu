#  도움 주신 분들 
#  Helloyunho / https://github.com/Helloyunho
#  "펀크" / https://github.com/rlacks628628 


# ______ _                       _  _____  _   __ _   __    _____     
# |  _  (_)                     | |/ __  \| | / /| | / /   |_   _|    
# | | | |_ ___  ___ ___  _ __ __| |`' / /'| |/ / | |/ / _   _| |_   _ 
# | | | | / __|/ __/ _ \| '__/ _` |  / /  |    \ |    \| | | | | | | |
# | |/ /| \__ \ (_| (_) | | | (_| |./ /___| |\  \| |\  \ |_| | | |_| |
# |___/ |_|___/\___\___/|_|  \__,_|\_____/\_| \_/\_| \_/\__,_\_/\__,_|
                                                                    
                                                                                                                                                                                             
                                                                                                                         
                                                                                                                         
import websocket, json
from collections import OrderedDict
import asyncio
import multiprocessing
import discord
import threading
import config
class discordbot(discord.Client):
    async def on_ready(self):
        print('\n\n디스코드 로그인 완료\n\n')
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.channel.id == config.channel:
            ws.send('{"type":"talk","value":"' + '[디코] ' + message.author.name + ': ' + message.content + '"}')

async def send_discord(me):
    ch = client.get_channel(config.channelid)
    await ch.send(me)
    return True

class kkutubot(threading.Thread):
    def run(self):
        def on_message(ws, message):
            jsonstring = json.loads(message)
            if jsonstring['type'] == 'chat':
                if not jsonstring['profile']['id'] == config.wsid:
                    print(jsonstring['value'])
                    try:
                        name = jsonstring["profile"]["title"]
                    except:
                        name = jsonstring["profile"]["name"]

                    client.loop.create_task(send_discord('[끄투] ' + name + " : " + jsonstring['value']))

        def on_close(ws):
            print("\n\n 경고! websocket이 종료되었습니다! \n\n")

        socket_url = config.wslink
        # kk = socket_url
        # self.kk = kk.replace('ws://', '')
        # socket_url = socket_url + '/Socket_Here'
        websocket.enableTrace(True)
        global ws
        ws = websocket.WebSocketApp(socket_url, on_message=on_message, on_close=on_close)
        ws.run_forever()
recv = kkutubot(name="get_chat") 
recv.start()
client = discordbot()
client.run(config.token)

import discord
import myconfig
import asyncio
import websockets
import json 

class discordbot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.loop = asyncio.get_event_loop()
        self.mykkutu = self.loop.create_task(self.kkutu_websocket())   

    async def kkutu_websocket(self):
        global websocket # < 좋지않은 예...
        async with websockets.connect(myconfig.ws) as websocket:
            while True:
                message = await websocket.recv()
                jsonstring = json.loads(message)

                if jsonstring['type'] == 'chat':
                    if not jsonstring['profile']['id'] == myconfig.wsid:
                        # print(jsonstring['value'])
                        try:
                            name = jsonstring["profile"]["title"]
                        except:
                            name = jsonstring["profile"]["name"]
                        value = jsonstring['value']
                        value = value.replace("@here","")
                        value = value.replace("@everyone","")
                        print('[끄투] ' + name + ': ' + value )
                        
                        

                        await self.get_channel(myconfig.channelid).send('[끄투] `' + name + '`: ' + value )

    async def on_ready(self):
        print("======")
        print("Discord2KKuTu Discord 로그인 완료.")
        print("======")

    async def on_message(self, message):
        if message.author.bot:
            return

        if not message.channel.id == myconfig.channelid:
            return
        else:
            a = message.attachments
            b = len(a)
            if b > 0:
                for n in a:
                    await websocket.send('{"type":"talk","value":"' + '[디코] ' + message.author.name + ': ' + n.url + '"}')

            await websocket.send('{"type":"talk","value":"' + '[디코] ' + message.author.name + ': ' + message.content + '"}')
        
        

    
client = discordbot()
client.run(myconfig.token)
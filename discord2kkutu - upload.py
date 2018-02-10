# import kkutu2discord
import discord
import json
import websocket
import asyncio
import threading
client = discord.Client()
global socket_url
global text1

text1 = None
socket_url = "socket_here"
def smessage(msg):
    global ws
    ws.send('{"type":"talk","value":"'+msg+'"}')

# async def dsmessage(tgmsg):
#     await client.wait_until_ready()

    # global tgmsg
    # while True:
    #     if not tgmsg is None:
    #         await client.send_message(discord.Channel(id="400592573867229185"), tgmsg)
    #         tgmsg = None
    #         print(tgmsg)
    #     else:
    #         pass
# async def kkutu():
async def send():
    global text1
    while True:
        
        if not text1 == None:
            ch = discord.Object(id="400592573867229185")
            await client.send_message(ch, text1)
            text1 = None
        else:
            pass    
class kkutu(threading.Thread):
    def run(self):
        global ws

        def onmessage(ws,message):
            global text1
        # print(message)
            data = json.loads(message)
            if data["type"] == "chat":
                try:
                    name = data["profile"]["title"]
                except:
                    name = data["profile"]["name"]
                    # sendmsg("400592573867229185","test")

                # print(ws,message)
                if not name == "GUEST8779":
                    print("[끄투] %s : %s" %(name, data["value"]))
                    try:
                        name = data["profile"]["title"]
                    except:
                        name = data["profile"]["name"]
                    text3 = "[끄투] %s : %s" %(name, data["value"])
                    text1 = text3.replace("@everyone","")
                    text1 = text1.replace("@here","")
        def on_close(ws):
            print("경고! websocket이 중지되었습니다!")

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(socket_url, on_message=onmessage,on_close=on_close)
        ws.run_forever()


@client.event
async def on_ready():
    print("\n디스코드 준비 완료!")

@client.event
async def on_message(message):
    global ws
    if message.author.id != "411772883652706304" and message.channel.id == "400592573867229185":
        print("[디코] " +message.author.name + " : " + message.content)

        smessage("[디코] " +message.author.name + " : " + message.content)

recv = kkutu(name="get_chat")
recv.start()
client.loop.create_task(send())
client.run("token")

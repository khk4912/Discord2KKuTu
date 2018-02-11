import random, discord, requests, json, websocket ,asyncio ,threading, bs4
client = discord.Client()
wsurl = "웹소켓 주소"
def send_kkutu(msg):
	global ws 
	ws.send('{"type":"talk","value":"'+msg+'"}')
async def send_discord(msg):
	await client.send_message(discord.Object(id="디코 보낼 채널"), msg)
class kkutu(threading.Thread):
	def run(self):
		global ws
		def onmessage(ws,message):
			li = random.choice([1, 2])
			data = json.loads(message)
			try:
				name = data["profile"]["name"]
			except:
				name = data["profile"]["title"]
			if name == "GUEST7045":
				return
			content = data["value"]
			if li == 1:
				text = "```diff\n+[끄투]"+name+":"+content+"```"
			if li == 2:
				text = "```diff\n-[끄투]"+name+":"+content+"```"
			client.loop.create_task(send_discord(text))
		def on_close(ws):
			print("웹소켓 꺼졌다!\n안해안해안해")
		websocket.enableTrace(True)
		ws = websocket.WebSocketApp(wsurl, on_message=onmessage,on_close=on_close)
		ws.run_forever()
@client.event
async def on_ready():
	print("디코 파트 준비 끝\nALL OF DISOCRD PART IS ON_READY")
@client.event
async def on_message(message):
	global ws
	if not message.channel.id == "디코 받을 채널":
		return
	if message.author.bot:
		return
	send_kkutu("[디코]"+message.author.name+":"+message.content+"")
recv = kkutu(name="get_chat")
recv.start()
client.run("토큰")
	

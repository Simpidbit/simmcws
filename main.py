# Copyright (c) 2020 Simpidbit <gmail@8155530.com>. All Rights Reserved.

# Default listening port: 8080

from send_message import *
import packages
import index
import check

import traceback
import json
import os
import sys
from random import randint
from threading import Thread
from asyncio import sleep
from asyncio import get_event_loop, ensure_future

from websockets import serve as ws_serve

# Defaulted listening port
PORT_DEFAULT = 8080

# Defaulted listening IP
IP_LISTENING_DEFAULT = "127.0.0.1"

# Global valueables
global_var = {}
# To hold some packages that didnot arrive in the world.
global_var["bad_packages"] = []
# To hold command-line back packages.
global_var["commandResults"] = []


# Return the player's id
def getPlayerInfo(string:str) -> str:
	pkt = json.loads(string)
	try:
		name = pkt["body"]["victim"][0]
		return name
	except:
		os.system(f"kill {os.getpid()}")
		return "None"


# When buildings are build, 
# this function can decide if the main process waits.
async def ifWait(pkt:dict, global_var:dict):
	try:
		if "#func" in pkt["message"]:
			await sleep(2)
	except:
		pass
	try:
		if global_var["wait_sympol"]:
			while global_var["wait_sympol"]:
				await sleep(0.1)
	except:
		pass


async def main(client, path):
    await sleep(1)
    await client.send(command("testfor @s"))
    name = getPlayerInfo(await client.recv())

    await client.send(command(actionbar("§b<<< 欢迎使用 >>>")))
    await client.send(command(say("联系作者？ ->  Simpidbit(QQ:2766277616)")))
    await client.send(command(status("等待发出订阅数据包...")))
    await client.send(json.dumps(packages.main["subscribe"]))
    await client.send(command(ok("已经发出订阅数据包！")))
    await client.send(command(say("用户名: " + name)))

    while True:
        pkt = check.getMessageInfo(await client.recv(), name, global_var)
        ensure_future(\
                        index.main(pkt, client, command, global_var)\
                        )
        # If need to block the main process.
        await ifWait(pkt, global_var)
        await sleep(0)


server_port_g = 0
def build_server():
    global server_port_g
    server_port = 0
    try:
        server_port = sys.argv[1]
    except (IndexError):
        server_port = PORT_DEFAULT
    server = ws_serve(main, IP_LISTENING_DEFAULT, server_port)
    server_port_g = server_port
    return server

if __name__ == "__main__":
    os.system("clear")
    global_var["wait_sympol"] = False

    server = build_server()
    print(f"WebSocket服务端已经启动, 请在游戏聊天框内输入命令: /connect 127.0.0.1:{server_port_g} 来连接WebSocket服务端")

    loop = get_event_loop()
    loop.run_until_complete(server)
    loop.run_forever()

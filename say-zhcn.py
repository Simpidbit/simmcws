# Copyright (c) 2020 ghostworker.All Rights Reserved.
#
# This file: main module.
# 

from random import randint
from threading import Thread
import traceback
import json
import os
import sys

from asyncio import sleep
from asyncio import get_event_loop, ensure_future
from websockets import serve as ws_serve

from send_message import *
import packages
import index
import check


# Global valueables
global_var = {}
# To keep some packages that didnot arrive in the world.
global_var["bad_packages"] = []
# To keep command-line back packages.
global_var["commandResults"] = []


def getPlayerInfo(string:str) -> str:
	"""
	Return the player's id who is using this tool
	"""
	pkt = json.loads(string)
	try:
		name = pkt["body"]["victim"][0]
		return name
	except:
		os.system(f"kill {os.getpid()}")
		return "None"


async def ifWait(pkt:dict, global_var:dict):
	"""
	When buildings are build, 
	this function can decide if the main process waits.
	"""
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
    """
    The main function of this application
    """
    print("connected!")

    while True:
        s = input(">>> ")
        await client.send(command(say(s)))
        await client.recv()



def make_server():
    global server_port_g
    server_port = 0
    try:
        server_port = int(sys.argv[1])
    except (IndexError):
        server_port = 9999

    server = ws_serve(main, "127.0.0.1", server_port)
    return (server, server_port)

if __name__ == "__main__":
    os.system("clear")
    global_var["wait_sympol"] = False

    server, server_port = make_server()
    print(f"WebSocket服务端已经启动, 请在游戏聊天框内输入命令: /connect 127.0.0.1:{server_port} 来连接WebSocket服务端")

    loop = get_event_loop()
    loop.run_until_complete(server)
    loop.run_forever()

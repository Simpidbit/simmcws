# Copyright © 2020 ghostworker.All Rights Reserved.
#
# This module:the index of abled things
#

import os
import re

import asyncio

from send_message import *
import please_tell 
import agent
import function
import image
import nbtread
import baike


async def main(pkt, client, command, global_var):
	# 判断是否为玩家信息，有可能是指令回包
	if pkt["type"] == "message":
		message = pkt["message"].split(" ")
		# 用于处理连续的多个空格
		removes = []
		for i in range(len(message)):
			message[i] = message[i].replace(" ","")
			if message[i] == "":
				removes.append(i)

		for each in removes:
			message.pop(each)

		if pkt["type"] == "message":
			cmd = message[0]
			
			# 涉及建筑导入部分
			if re.search(r"^#func",cmd):
				function.build(message, client, global_var)

			elif re.search(r"^#nbt",cmd):
				nbtread.nbtfile(client, message, global_var)

			elif re.search("^#pic",cmd):
				image.pic(message,client,global_var)

			# =========== 其他部分 =================================================

			elif re.search(r"^#ag-create",cmd):
				await client.send(command("agent create"))

			elif re.search(r"^#ag-attack",cmd):
				agent.attack(message,client)

			elif re.search(r"^#ag-tp",cmd):
				# 传 pkt 为了传送方便
				agent.tp(message,client)

			elif re.search(r"^#ag-cmd",cmd):
				agent.cmd(message,client)

			elif re.search(r"^#baike",cmd):
				baike.baike(message,client)

			elif re.search("^#shutdown",cmd):
				pid = os.getpid()
				os.system(f"kill {pid}")

			elif re.search("^#restart",cmd):
				os.system("python restart.py "+str(os.getpid()))

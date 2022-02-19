import asyncio
import json
import time
import traceback
import re

from send_message import *
import cmdarg
import api


def build(message, client, global_var):
	asyncio.ensure_future(_build(message, client, global_var))

async def _build(message, client, global_var):
	args = cmdarg.Cmd(message)
	try:
		open(args.args["-p"],"r").close()
	except:
		await client.send(command(alert("您的文件路径输入有误,无法找到您的文件!")))
		await client.recv()
		await client.recv()
		return

	with open(args.args["-p"],"r") as f:
		lines = f.readlines()
	lines = await api.getPosAndLines(client, global_var, lines)
	await api.sendBuildingPackages(client, lines, global_var, args)

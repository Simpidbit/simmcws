from PIL import Image
from image import blocks as bl
from send_message import *
import asyncio
import traceback
import function
import cmdarg
import api
import cmdarg

def pic(message, client, global_var):
	asyncio.ensure_future(_pic(message, client, global_var))

async def _pic(message, client, global_var):
	args = cmdarg.Cmd(message)

	try:
		args.args["-p"]
	except(KeyError):
		await client.send(command(alert("缺失的参数:-p")))
		return
	try:
		args.args["-t"]
	except(KeyError):
		print("WARNING: -t 参数使用缺省值")
		args.args["-t"] = 1

	try:
		args.args["-s"]
	except(KeyError):
		args.args["-s"] = 1
	args.args["-s"] = int(args.args["-s"])
	
	try:
		img = Image.open(args.args["-p"]).convert("P")
		await client.send(command(status("正在识别图片...")))
	except:
		await client.send(command(alert("未找到文件！")))
		return
	width,height = img.size
	img = img.resize((\
			int(width/args.args["-s"]),\
			int(height/args.args["-s"])\
			))
	width,height = img.size
	
	lines = []
	for h in range(height):
		for w in range(width):
			pixel = img.getpixel((w,h))
			try:
				block = bl.main[pixel]
			except:
				block = "concrete 0"
			lines.append(f"setblock ~{w} ~ ~{h} {block}")
	
	await client.send(command(ok("识别完毕！")))

	await api.getPosAndLines(client, global_var, lines)
	await api.sendBuildingPackages(client, lines, global_var, args)

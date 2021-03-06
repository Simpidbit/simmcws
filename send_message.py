import packages
import json

# 生成指令数据包
def command(cmd,id_ = 0) -> str:
	pk = packages.main['normal']
	pk['body']['commandLine'] = cmd
	pk['header']['requestId'] = "00000000-0000-0000-0000-"+str(id_)
	re = json.dumps(pk)
	return re

# 说话用
def say(string) -> str:
	re = "tellraw @a {\"rawtext\":[{\"text\":\">> §eMessage§f << "+string+" §e\"}]}"
	return re

# 警告用
def alert(string) -> str:
	re = "tellraw @a {\"rawtext\":[{\"text\":\">> §cAlert§f << "+string+" §e\"}]}"
	return re

# 提示用
def ok(string) -> str:
	re = "tellraw @a {\"rawtext\":[{\"text\":\">> §aOK§f << "+string+" §e\"}]}"
	return re

# 状态用
def status(string) -> str:
	re = "tellraw @a {\"rawtext\":[{\"text\":\">> §bStatus§f << "+string+" §e\"}]}"
	return re

# 小标题用
def actionbar(string) -> str:
	re = f"title @a actionbar {string}"
	return re

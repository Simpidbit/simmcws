with open("values.html","r",encoding="utf-8") as f:
	values = f.read()

vlist = values.split("\n")

datas = []
blocks = []
for each in vlist:
	elist = each.split(" ")
	for eeach in elist:
		try:
			datas.append(str(int(eeach)))
		except:
			blocks.append(eeach)

last = list(zip(datas,blocks))
print(last)

dic = {}
for each in last:
	dic[each[0]] = each[1]

with open("blocks_id.py","w",encoding="utf-8") as f:
	f.write(str(dic))

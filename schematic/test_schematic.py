from nbtschematic import SchematicFile
import blocks_id as bi

sf = SchematicFile.load("D:\\Desktop\\files\\leim2.schematic")

"""
width = sf.schema["Schematic"].schema["Width"]
length = sf.schema["Schematic"].schema["Length"]
height = sf.schema["Schematic"].schema["Height"]
"""
width = sf.root["Width"]
height = sf.root["Height"]
length = sf.root["Length"]
print(length,width,height)
input()

with open("test.mcfunction","w",encoding="utf-8") as f:
	for y in range(height):
		for z in range(length):
			for x in range(width):
				if not int(sf.blocks[y,z,x]) == 0:
					block_id = abs(int(sf.blocks[y,z,x]))
					block_data = int(sf.data[y,z,x])
					if not block_id == 0:
						if block_data == 0:
							f.write(f"setblock ~{x}~{y}~{z} {bi.main[str(block_id)]}\n")
							f.write(f"setblock ~{x}~{y}~{z} {bi.main[str(block_id)]} {str(block_data)}\n")

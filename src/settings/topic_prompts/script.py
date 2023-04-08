import os

files = os.listdir('./')

text = ""

for file in files:
	if not file.endswith(".py"):
		with open(file, "r") as f:
			extract = "".join(f.readlines())
			text += file.replace(".txt", "") + ":'"  + extract + "'\n"
			f.close()
	
with open("all_prompts.txt", "w") as f:
	f.write(text)
	f.close()

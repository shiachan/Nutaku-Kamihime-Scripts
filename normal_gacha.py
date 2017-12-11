import requests,json,heading_post,sys,conf,heading,time,sell_fodder_no_loop

def gacha_normal_ten():
	
	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_gacha/normal"
	payload = "{\"gacha_id\":9}"
	res = requests.request("POST", url, data=payload, headers=heading_post.headers)
	data = json.loads(res.text)
	print(data)

def gacha_normal_one():
	
	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_gacha/normal"
	payload = "{\"gacha_id\":8}"
	res = requests.request("POST", url, data=payload, headers=heading_post.headers)
	data = json.loads(res.text)
	print(data)
	
def loop_gacha(roll_type):
	print("Start of loop\n==========")
	if roll_type == 0:
		gacha_normal_ten()
	elif roll_type == 1:
		gacha_normal_one()
	else:
		print("Error gacha type not defined")
		sys.exit()
	time.sleep(1)
	print("gacha_bought\n==========")
	sell_fodder_no_loop.loop_once()

def main_prog():
	print("Hello! Have you set the cookies? If not break this(ctrl+pause on windows python) and set them now!\nNOTE THAT THIS SCRIPT WILL ALSO AUTOSELL ALL N/R/SR ENHANCE WEAPONS AND N/R ENHANCE EIDOLONS! RUN AT OWN RISK")
	try:
		roll_type = int(input("For Gem Gacha x 10 key in 0, Gem Gacha x 1 key in 1, the default is 0: "))
	except: 
		roll_type = 0
	print("How many rolls do you want to do?")
	try:
		roll_count = int(input("You can only roll each 100 times a day, the free roll counts as 1x 1 gem roll the default is 100: "))
	except: 
		roll_count = 100
	if roll_count >= 1 and roll_count <= 100:
		total_loop = int(roll_count)
		current_loop = int(1)
		while total_loop >= current_loop :
			print("Total Number of loops to run: " + str(total_loop))
			print("Current loop being run : " + str(current_loop))
			loop_gacha(roll_type)
			current_loop = current_loop + 1
	else:
		print("Input error with the amount of rolls")


main_prog()
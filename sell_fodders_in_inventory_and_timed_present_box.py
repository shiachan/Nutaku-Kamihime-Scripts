import requests,json,heading_post,sys,heading,time

def sell_weapon_fodders(fodder):
	if fodder == 'nil':
		print("no weapons to sell")
		return "nil"
	else:
		url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons_sale"
		payload = "{\"ids\":["+str(fodder)+"]}"
		res = requests.request("POST", url, data=payload, headers=heading_post.headers)
		data = json.loads(res.text)
		return data
	
def get_weapon_fodder():

	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons"
	querystring = {"json":"{\"selectable_base_filter\":\"sellable\",\"page\":\"1\",\"per_page\":100}"}
	res = requests.request("GET", url, headers=heading.headers, params=querystring)
	data = json.loads(res.text)
	
	data_list = data["data"]
	output = ([d['a_weapon_id'] for d in data_list if d['attack'] == 8 or d['attack'] == 12])
	normal = ([d['a_weapon_id'] for d in data_list if d['rare'] == 'N' and d['bonus'] ==  0])
	output = output + normal
	output = output[:20]
	if not output:
		return "nil"
	else:
		# print(output)
		delimiter = ", "
		str1 = delimiter.join(str(e) for e in output)
		return str1

	
def sell_summon_fodders(fodder):
	if fodder == 'nil':
		print("no summons to sell")
		return "nil"
	else:
		url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_summons_sale"
		payload = "{\"ids\":["+str(fodder)+"]}"
		res = requests.request("POST", url, data=payload, headers=heading_post.headers)
		data = json.loads(res.text)
		return data
	
def get_summon_fodder():

	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_summons"
	querystring = {"json":"{\"selectable_base_filter\":\"sellable\",\"page\":\"1\",\"per_page\":100}"}
	res = requests.request("GET", url, headers=heading.headers, params=querystring)
	data = json.loads(res.text)
	
	data_list = data["data"]
	output = ([d['a_summon_id'] for d in data_list if d['attack'] == 12])
	normal = ([d['a_summon_id'] for d in data_list if d['rare'] == 'N' and d['bonus'] == 0])
	rares  = ([d['a_summon_id'] for d in data_list if d['rare'] == 'R' and d['bonus'] == 0])
	output = normal + rares + output
	output = output[:20]
	if not output:
		return "nil"
	else:
		# print(output)
		delimiter = ", "
		str1 = delimiter.join(str(e) for e in output)
		return str1
	
def receive_timelimit_present():
	
	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_presents_receive"
	payload = "{\"type\":\"timelimit\"}"
	res = requests.request("POST", url, data=payload, headers=heading_post.headers)
	data = json.loads(res.text)
	return data
	
def loop_once():
	received = receive_timelimit_present()
	time.sleep(2)
	w_fodders = get_weapon_fodder()
	s_fodders = get_summon_fodder()
	w_fodders = sell_weapon_fodders(w_fodders)
	s_fodders = sell_summon_fodders(s_fodders)
	print(received)
	print("================================\nEND OF LOOP")

def main_prog():
	print("Hello! Have you set the cookies? If not break this(ctrl+pause on windows python) and set them now!\nNOTE THAT THIS SCRIPT WILL SELL ALL N/R/SR ENHANCE WEAPONS AND N/R/SR ENHANCE EIDOLONS! RUN AT YOUR OWN RISK")
	print("This script lets you sell all those pesky stuff in your time limited present box(Great for getting rid of all those enhance materials you get from (union) raids!) it tries to sell 20 weapons and eidolons each per run \n there is no sanity check so it will keep running even if empty use break to break it")
	print("How many runs do you want to do?")
	try:
		roll_count = int(input("Run count?(default is 1, I've put a max of 100 as a limit, edit it if you like :) ) : "))
	except: 
		roll_count = 1
	if roll_count >= 1 and roll_count <= 100:
		total_loop = int(roll_count)
		current_loop = int(1)
		while total_loop >= current_loop :
			print("Total Number of loops to run: " + str(total_loop))
			print("Current loop being run : " + str(current_loop))
			loop_once()
			current_loop = current_loop + 1
	else:
		print("Input error with the amount of runs")


main_prog()


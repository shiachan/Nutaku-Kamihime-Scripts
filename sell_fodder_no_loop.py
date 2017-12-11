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
	normal = ([d['a_weapon_id'] for d in data_list if d['rare'] == 'N' and d['bonus'] == 0])
	output = output + normal
	output = output[:20]
	
	if not output:
		return "nil"
	else:
		#print(normal)
		#print(output)
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
	output = ([d['a_summon_id'] for d in data_list if d['rare'] == 'R' and d['bonus'] == 0])
	normal = ([d['a_summon_id'] for d in data_list if d['rare'] == 'N' and d['bonus'] == 0])
	output = output + normal
	output = output[:20]

	if not output:
		return "nil"
	else:
		# print(output)
		# print(normal)
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
	w_fodders = get_weapon_fodder()
	s_fodders = get_summon_fodder()

	time.sleep(1)
	w_fodders = sell_weapon_fodders(w_fodders)
	s_fodders = sell_summon_fodders(s_fodders)
	print(w_fodders)
	print(s_fodders)
	print("================================\nEND OF LOOP")


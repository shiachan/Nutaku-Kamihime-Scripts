import requests,json,heading_post,sys,heading,time
	
def get_weapon_fodder():

	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons"
	querystring = {"json":"{\"selectable_base_filter\":\"sellable\",\"page\":\"1\",\"per_page\":100}"}
	res = requests.request("GET", url, headers=heading.headers, params=querystring)
	data = json.loads(res.text)
	
	data_list = data["data"]
	output = ([d['a_weapon_id'] for d in data_list if d['rare'] == "SR" and d['overlimit_count'] == 0 and d['level'] == 1 and d['attack'] >= 13])
	print("You have "+str(len(output))+" SRs")
		
def get_r_fodder():
	
	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons"
	querystring = {"json":"{\"selectable_base_filter\":\"sellable\",\"page\":\"1\",\"per_page\":100}"}
	res = requests.request("GET", url, headers=heading.headers, params=querystring)
	data = json.loads(res.text)
	
	data_list = data["data"]
	output = ([d['a_weapon_id'] for d in data_list if d['rare'] == "R" and d['level'] == 1 and d['attack'] != 8 and d['attack'] != 12])
	print("You have "+str(len(output))+" Rs")

def loop_once():

	w_fodders = get_weapon_fodder()
	r_fodders = get_r_fodder()
	

def main_prog():
	print("Hello! Have you set the cookies? If not break this(ctrl+pause on windows python) and set them now!")
	print("Use this to check how much R and SR fodder you have")
	loop_once()

main_prog()

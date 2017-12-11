import requests,json,heading_post,sys,heading,time
	
def get_weapon_fodder():

	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons"
	querystring = {"json":"{\"selectable_base_filter\":\"sellable\",\"page\":\"1\",\"per_page\":100}"}
	res = requests.request("GET", url, headers=heading.headers, params=querystring)
	data = json.loads(res.text)
	
	data_list = data["data"]
	output = ([d['a_weapon_id'] for d in data_list if d['rare'] == "SR" and d['overlimit_count'] == 0 and d['level'] == 1 and d['attack'] >= 13])
	print("You had "+str(len(output))+" SRs now you have "+str(len(output)-1)+" SRs")
	output = output[0]
	print(output)
	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons/"+str(output)
	res = requests.request("GET", url, headers=heading.headers)
	data = json.loads(res.text)
	slvl_list =  data["skills"][0]['level']
	
	if not output:
		return "nil"
	else:
		print(slvl_list)
		print(output)
		return output
		
def get_r_fodder():
	
	url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons"
	querystring = {"json":"{\"selectable_base_filter\":\"sellable\",\"page\":\"1\",\"per_page\":100}"}
	res = requests.request("GET", url, headers=heading.headers, params=querystring)
	data = json.loads(res.text)
	
	data_list = data["data"]
	output = ([d['a_weapon_id'] for d in data_list if d['rare'] == "R" and d['level'] == 1 and d['attack'] != 8 and d['attack'] != 12])
	print("You had "+str(len(output))+" Rs now you have "+str(len(output)-6)+" Rs")
	output = output[:6]
	print(output)
	return(output)

def enhance_to_slvl4(w_fodder, r_fodders):
	if len(r_fodders) >= 6:
		slvl_2 = str(r_fodders[0])
		slvl_3 = [r_fodders[1],r_fodders[2]]
		delimiter = ", "
		str1 = delimiter.join(str(e) for e in slvl_3)
		slvl_4 = [r_fodders[3],r_fodders[4],r_fodders[5]]
		delimiter = ", "
		str2 = delimiter.join(str(e) for e in slvl_4)
		url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons/"+str(w_fodder)+"/enhance"
		payload = "{\"ids\":["+slvl_2+"]}"
		response = requests.request("POST", url, data=payload, headers=heading_post.headers)
		time.sleep(1)
		url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons/"+str(w_fodder)+"/enhance"
		payload = "{\"ids\":["+str1+"]}"
		response = requests.request("POST", url, data=payload, headers=heading_post.headers)
		time.sleep(1)	
		url = "https://cf.g.kamihimeproject.dmmgames.com/v1/a_weapons/"+str(w_fodder)+"/enhance"
		payload = "{\"ids\":["+str2+"]}"
		response = requests.request("POST", url, data=payload, headers=heading_post.headers)
		time.sleep(1)
	else:
		print("You need 6 R weapons(non-fodder) to do this!")
	
def loop_once():

	w_fodders = get_weapon_fodder()
	r_fodders = get_r_fodder()
	enhance_to_slvl4(w_fodders, r_fodders)
	print("1 down")
	time.sleep(2)
	

def main_prog():
	print("Hello! Have you set the cookies? If not break this(ctrl+pause on windows python) and set them now!\nNOTE THAT THIS SCRIPT WILL TAKE ANY LVL 1 SR(NON-FODDER) AND BRING IT TO SLVL 4 WITH 6 NON FODDER R'S YOU HAVE!\nRUN AT YOUR OWN RISK")
	print("Hate the Enhancing part of the game? This script takes 1 SR slvl 1 weapon and enhances it to slvl 4 with 6 non fodder R's you have.\nThere is no sanity check so it will keep running even if empty use break to break it")
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
			print("================================\nEND OF LOOP")
	else:
		print("Input error with the amount of runs")


main_prog()

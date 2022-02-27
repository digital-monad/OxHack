import deso
import json
import time

#https://github.com/AdityaChaudhary0005/DeSo.py
#name, donation, charity


def read_user_posts(username="DonorKebab"):
	with open("UserPosts.json", "w") as file:
		json.dump(deso.Posts.getUserPosts(username="DonorKebab"), file)
	with open("UserPosts.json", "r") as file:
		userposts = json.load(file)
	#print(userposts)
	post_bodies = []
	for post in userposts['Posts']:
		post_bodies.append(post['Body'])
	return post_bodies
		


def write_post(post_string=''):
	''' SEEDHEX should always be kept private. It has access to your complete wallet. It's kinda like
		seed phrase. This is why writing methods in backend isn't a good practice until we have derived keys.
		You can only automate your own account and can't have user authorisation. It is recommended to use test account while using write methods.

		You can find the seedHex of your account in your browser storage. Just open https://bitclout.com/ > Dev tools > Application > Storage > Local Storage > https://identity.bitclout.com > users > Select the public key with which you want to post > seedHex'''
	SEEDHEX = "7ea760e9f18dfa5dca90facb5a6ad2093813d4930595f3f25faacf5512557ef4"  # your seedHex
	PUBLIC_KEY = "BC1YLjSj1srCBxAieZxVxj3BPUJCsJVefveSgCC9vFEePmnMDgUAYov"  # your PublicKey

	post = deso.Post(SEEDHEX, PUBLIC_KEY)

	#status = post.send("This post was sent using the DeSo python library 😎")
	status = post.send(post_string)
	print(status)  # 200 if post was successfull


def format_post(name='NA',donation=0,charity='NA'):
	formatted_string = 'Donator:'+name+',donation:'+str(donation)+',charity:'+charity
	return formatted_string

def parse_post(post_body=''):
	parse_list = post_body.split(',')
	name = parse_list[0].split("Donator:",1)[1] 
	donation = int(parse_list[1].split("donation:",1)[1])
	charity = parse_list[2].split("charity:",1)[1]
	parsed_list = [name, donation, charity]
	return parsed_list
	
	
	
if __name__ == "__main__":
	#write_post('TESTING AGAIN')
	#print(read_user_posts())
	
	#post_string = format_post(name='TESTGUY',donation=0,charity='N/A')
	#write_post(post_string)
	#time.sleep(10)
	print(read_user_posts())
	print(parse_post(read_user_posts()[0]))
	
	




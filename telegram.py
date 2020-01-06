import requests
import json
from bs4 import BeautifulSoup
import random
import time

def find_proxy():
	print("try to find proxy1")
	proxies_list = []
	res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
	soup = BeautifulSoup(res.text,"lxml")
	for items in soup.select("#proxylisttable tbody tr")[50:random.randint(51,75)]:
		proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
		temp = ('https://' + str(proxy_list))
		proxies={
		'https': temp
		}
		if requests.get(URL + 'getUpdates', proxies=proxies) == 200:
			return proxies
			break
#	proxies_list.append(proxies)
print("try to find proxy")
proxies_list = []
res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(res.text,"lxml")
for items in soup.select("#proxylisttable tbody tr")[50:random.randint(51,75)]:
	proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
	temp = ('https://' + str(proxy_list))
	proxies={
	'https': temp
	}

#token = 'AAG3V-oUt_KvvoKvn56yIAu2AmHn-qzYFy0'
token = '680359542:AAG3V-oUt_KvvoKvn56yIAu2AmHn-qzYFy0'

URL = 'https://api.telegram.org/bot' + token + '/'

# proxies = {
	
# 	'https': 'https://128.0.179.234:41258',
# 	'http': 'http://138.204.23.66.64:53281'
	
# }
print("found proxy:",proxies)
def get_updates():
	url = URL + 'getUpdates'
	r = requests.get(url, proxies=proxies)
	print('result: ', r)
	return r.json()

def get_message():
	data = get_updates()
	print(data['result'][-1])

	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
	message = { 
				'chat_id': chat_id,
				'text': message_text
	}

	return message

def send_message(chat_id, text = 'wait a second please...'):
	print('try to send message')
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	print('sending: ', url)
	requests.get(url, proxies=proxies)


def main():
	while True:
	#	print(get_message())
		answer = get_message()
		chat_id = answer['chat_id']
		text = answer['text']
		send_message(chat_id, answer['text']+"?" )
		if "понял" in text:
			send_message(chat_id, "молодец" )

		print('next step')
		time.sleep(1)

if __name__ == '__main__':
	main()

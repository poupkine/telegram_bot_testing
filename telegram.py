import requests
import json
from bs4 import BeautifulSoup


# res = requests.get('https://free-proxy-list.net/', headers={'User-Agent':'Mozilla/5.0'})
# soup = BeautifulSoup(res.text,"lxml")
# for items in soup.select("#proxylisttable tbody tr"):
# 	proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
# 	temp = ('https://' + str(proxy_list))
# 	proxies={
# 	'https': temp
# 	}
# 	proxies_list.append(proxies)



token = '680359542:AAG3V-oUt_KvvoKv1n56yIAu2AmHn-qzYFy0'

URL = 'https://api.telegram.org/bot' + token + '/'

proxies = {
	
   
	'https': 'https://27.147.136.178:47678',
	'http': 'http://183.88.17.55:8080'
	
}

def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url, proxies=proxies)
	print('result:', r)
	return r.json()

def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
	message = { 
				'chat_id': chat_id,
				'text': message_text
	}

	return message

def send_message(chat_id, text = 'wait a second please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)


def main():
	send_message(13)
	print(get_message())
	answer = get_message()
	chat_id = answer['chat_id']
#	text = 
	send_message(chat_id, "ask!!")

if __name__ == '__main__':
	main()



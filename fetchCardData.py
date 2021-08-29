import requests
import json	
import time

def fetchCardData(print=False):
	# Rate Limits and Good Citizenship for the scryfall api
	time.sleep(0.1)

	url = "https://api.scryfall.com/bulk-data/oracle-cards"

	response1 = requests.get(url)
	bulk_uri = response1.json()['download_uri']
	response2 = requests.get(bulk_uri)
	cards = response2.json()
	if (print):
		for card in cards:
			print(card['name'], '|', card['type_line'])
	return cards

if __name__ == '__main__':
    fetchCardData(print=True)
import requests
import json


def get_exchange_rate():
	response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
	data = response.json()

	return data['rates']['USD'] / data['rates']['EUR']
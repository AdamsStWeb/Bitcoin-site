from django.shortcuts import render

def home(request):
	import requests 
	import json

	
	# Crab Crypto Price 
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,BCH,ETH,XRP,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
	price = json.loads(price_request.content)
	
	# Grab Crypto Newsa
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html',{'api': api, 'price':price})
	
def prices(request):
	
	return render(request, 'prices.html', {})
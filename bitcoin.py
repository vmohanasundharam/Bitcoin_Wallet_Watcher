from bs4 import BeautifulSoup
import requests
import json

class bitcoin(object):
	wallet_address = ""
	html = ""
	tr_rec_list = []
	flag = False
	def __init__(self, wallet_address):
		self.wallet_address = wallet_address
		self.download_wallet()

	def download_wallet(self):
		url =  'https://www.walletexplorer.com/wallet/'+self.wallet_address
		self.html = requests.get(url)
		if self.html.status_code!= 200:
			self.flag = True
		else:
			self.html = BeautifulSoup(self.html.content,"html.parser")
			error = self.html.findAll('p',attrs={"class":"error"})
			flag = True
		
		if len(error) > 0:
			url =  'https://www.walletexplorer.com/address/'+self.wallet_address
			self.html = requests.get(url)
			
			if self.html.status_code!= 200:
				self.flag = True
			else:
				self.html = BeautifulSoup(self.html.content,"html.parser")
				error = self.html.findAll('p',attrs={"class":"error"})
				self.flag = True
				if len(error) > 0:
					self.flag = True
				else:
					self.wallet_address =  self.html.findAll('a')[1].attrs['href'].replace("/wallet/","")
					url =  'https://www.walletexplorer.com/wallet/'+self.wallet_address
					print url
					self.html = requests.get(url)
					if self.html.status_code!= 200:
						self.flag = True
					else:
						self.html = BeautifulSoup(self.html.content,"html.parser")
						error = self.html.findAll('p',attrs={"class":"error"})
						if len(error) > 0 :
							self.flag = False
		else:
			self.flag = True


	def wallet_balance(self):
		if self.flag != False:
			balance = self.html.findAll('td',attrs={"class":"txid"})
			balance = balance[0].previous_element
			return balance


	def transfers_to_wallet(self):
		if self.flag != False:
			recived_rows = self.html.findAll('tr',attrs={"class":"received"})
			nodes_recived = []
			if len(recived_rows) > 0:
				for row in recived_rows:
					node = []
					date = row.find('td',attrs={"class":"date"}).text
					node.append(date)
					transfer_amount = row.find('td',attrs={"class":"amount diff"}).text
					transfer_amount = transfer_amount.replace("+","")
					node.append(transfer_amount)
					sender_wallet_id = row.find_all(href=True)[0]['href'].replace("/wallet/","")
					node.append(sender_wallet_id)
					nodes_recived.append(node)
			return nodes_recived
		else:
			return 0

	def transfers_from_wallet(self):
		if self.flag != False:
			sent_rows = self.html.findAll('tr',attrs={"class":"sent"})
			nodes_sent = []
			if len(sent_rows) > 0:
				for row in sent_rows:
					node = []
					time = row.find('td',attrs={"class":"date"}).text
					sent_table = row.find('table',attrs={"class":"empty"})
					table_rows = sent_table.findAll('tr')
					iterater = len(table_rows)-2
					while iterater >= 0:
						node = []
						transfer_amount =  table_rows[iterater].find('td',attrs={"class":"amount diff"}).text
						transfer_amount = transfer_amount.replace("-","")
						wallet_address =  table_rows[iterater].find_all(href=True)[0]['href'].replace("/wallet/","")
						node.append(time)
						node.append(transfer_amount)
						node.append(wallet_address)
						iterater -= 1
						nodes_sent.append(node)
			return nodes_sent
		else:
			return 0

def get_object(arg):
	obj = bitcoin(arg)
	return obj
	
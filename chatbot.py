# -*- coding: utf-8 -*-
import sys

import telegram
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox

tran1 = None #insert "traintime"
tran2 = None #insert "north"、"mid"、 "south"、"east" from which to go
tran3 = None #insert "north"、"mid"、 "south"、"east" to which
tran4 = None #insert the area to go
trainfrom = None
trainto = None
partfrom = None
partto = None

app = Flask(__name__)
bot = telegram.Bot(token='354914266:AAHNeiSma3dDA94TehenEFUPDP9LiHcUAEE')

def _set_webhook():
	status = bot.set_webhook('https://125dc476.ngrok.io/hook')
	if not status:
		print('Webhook set failed')
		sys.exit(1)

@app.route('/hook', methods=['POST'])
def webhook_handler():
	if request.method == "POST":
		update = telegram.Update.de_json(request.get_json(force=True), bot)

		text = update.message.text
		global tran1
		global tran2
		global tran3
		global tran4
		global trainfrom
		global trainto
#		update.message.reply_text(text)
		if 'traintime' in text:
			tran1 = 1
			update.message.reply_text("What part do you go from,\'north\'、\'mid\'、\'south\'、\'east\'?")
		elif tran1 == 1:
			if 'north' in text:
				partfrom = 'FromStationList1'
			if 'mid' in text:
				partfrom = 'FromStationList2'
			if 'south' in text:
				partfrom = 'FromStationList3'
			if 'east' in text:
				partfrom = 'FromStationList4'
#update.message.reply_text(partfrom)
			update.message.reply_text("What part do you go to,\'north\'、\'mid\'、\'south\'、\'east\'?")
			tran2 = 1
			tran1 = 2
		elif tran2 == 1:
			if 'north' in text:
				partto = 'FromStationList1'
			if 'mid' in text:
				partto = 'FromStationList2'
			if 'south' in text:
				partto = 'FromStationList3'
			if 'east' in text:
				partto = 'FromStationList4'
#update.message.reply_text(partto)
			update.message.reply_text("What name of area do you go from?")
			tran3 = 1
			tran2 = 2
			tran1 = 3
		elif tran3 == 1:
			trainfrom = text
#update.message.reply_text(trainfrom)
			update.message.reply_text("What name of area do you go to?")
			tran4 = 1
			tran3 = 2
			tran2 = 3
			tran1 = 4
		elif tran4 == 1:
			trainto = text
			update.message.reply_text(trainfrom)
#update.message.reply_text(trainto)
			timesearch()
		elif 'exit' in text:
			tran1 = 0
			tran2 = 0
			tran3 = 0
			tran4 = 0
			trainfrom = None
			trainto = None
			partfrom = None
			partto = None
		else:
			update.message.reply_text("I don't know what you mean,please tell me again or reply 'exit' for other talk topic.")
	return 'ok'
def timesearch():
	global trainfrom
	global trainto
	driver = webdriver.Firefox()
	driver.get("http://twtraffic.tra.gov.tw/twrail/EasySearch.aspx")
			
	selectfrom = Select(driver.find_element_by_name('FromStationList1'))
	selectfrom.select_by_visible_text(trainfrom)

	selectto = Select(driver.find_element_by_name('ToStationList1'))
	selectto.select_by_visible_text(trainto)

	button = driver.find_element_by_id("Button2")
	button.click()



if __name__ == "__main__":
	_set_webhook()
	app.run()

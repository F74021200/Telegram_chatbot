# -*- coding: utf-8 -*-
import sys

import telegram
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox

tran1 = None

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

#		update.message.reply_text(text)
		if 'traintime' in text:
			tran1 = 1
		elif 'check' in text:
			timesearch()
		else:
			update.message.reply_text("What do you test?")
	return 'ok'
def timesearch():
	driver = webdriver.Firefox()
	driver.get("http://twtraffic.tra.gov.tw/twrail/EasySearch.aspx")
			
	selectfrom = Select(driver.find_element_by_name('FromStationList1'))
	selectfrom.select_by_visible_text(u"福隆")

	selectto = Select(driver.find_element_by_name('ToStationList1'))
	selectto.select_by_visible_text(u"雙溪")

	button = driver.find_element_by_id("Button2")
	button.click()



if __name__ == "__main__":
	_set_webhook()
	app.run()

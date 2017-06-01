Comprehensive Document
======================
##	1.Description:
####	Now, the bot has only one chain of states, or one topic can talk with.When users insert 'traintime',the bot will ask user to insert the part of area users go from,and then after users insert the part to go from,the bot asks users to insert the part os area to go to.After inserting the part to go to,bot ask for the name to go from,and then ask the name to go to.Finally,the bot will open an window for the routine of train today.

##	2.Bot:
####	F74021200

##	3.Driver:
####	From [Selenium document](http://selenium-python.readthedocs.io/installation.html),"Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.", and the bot uses Firefox,therefor needs [geckodriver](https://github.com/mozilla/geckodriver/releases)

##	4.FSM:
<img src="https://github.com/F74021200/Telegram_chatbot/blob/master/my_state_diagram.png">

##	5.Implementation Example:
*	insert "traintime"
*	insert "north"
*	insert "north"
*	insert "福隆"
*	insert "雙溪"
*	window opend

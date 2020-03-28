import os
import sys

import configparser
import json

def load_config():
	if not os.path.exists("config.ini"):
		print("The config file is missing!  Check to see that it is in the current working directory.")
		sys.exit()

	ini = configparser.ConfigParser()
	ini.read("config.ini")

	sect = ini.sections()

	if "BotVariables" not in ini.sections():
		print("There seems to be something wrong with config.ini.  Is the [BotVariables] section present?")
		sys.exit()

	try:
		tk       = ini.get("BotVariables", "Bot-Token")
		channels = ini.get("BotVariables", "Listen-Channels")
		users    = ini.get("BotVariables", "Listen-Users")
		roles    = ini.get("BotVariables", "Listen-Roles")
		prefix   = ini.get("BotVariables", "Bot-Prefix")
	except configparser.NoOptionError:
		print("Some variables are missing from the config.ini.  Double check the file, then try again.")
		sys.exit()

	return tk, channels, users, roles, prefix

def load_json():
	if not os.path.exists("data.json"):
		master = {	"consoles" : {},
				"users" : {}	}
		return master

	with open("data.json", "r") as data:
		master = json.load(data)
		data.close()

	return master

def save_json(master):
	with open("data.json", "w") as data:
		json.dump(master, data)
		data.close()

	print("data.json was updated.")
	return
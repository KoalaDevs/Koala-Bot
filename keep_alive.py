#***************************************************************************#
#                                                                           #
# MCDramaBot - A Discord Bot That Causes Drama                              #
# https://github.com/CrankySupertoon/MCDramaBot                             #
# Copyright (C) 22020 CrankySupertoon. All rights reserved.                 #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I am not dead."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
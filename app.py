import json

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/api/stats")
def jsoned_stats():
	with open("jsons/stats.json", "r") as f:
		l = json.load(f)
		
	return jsonify(l)
	
@app.route("/")
def index():
	return "Hiiii"
	
if __name__ == '__main__':
	app.run()
from flask import Flask, render_template, jsonify, request, session
from models.position import Position,distance
from models.hunts import Hunt,hunts_list
#import git


app = Flask(__name__)



@app.route('/update_server', methods=['POST'])
def webhook():
	if request.method == 'POST':
		#repo = git.Repo('/home/Chicco94')
		#origin = repo.remotes.origin
		#origin.pull('main')
		return 'Updated PythonAnywhere successfully', 200
	else:
		return 'Wrong event type', 400



@app.route('/')
def index():
	session.clear()
	session['targetIndex'] = 0
	return render_template('index.html', tappa_attuale=-1)



@app.route('/start')
def start():
	return render_template('start.html', tappa_attuale=-1, hunts_list=hunts_list)



@app.route('/next-position', methods=['POST','GET','REDIRECT'])
def next_position():
	# Accessing the data sent with POST request
	session['targetIndex'] = session['targetIndex'] + 1
	response = {'targetIndex':session['targetIndex']}
	if (session['targetIndex'] >= len(hunts_list[session['targetHunt']].tappe)):
		response['ended'] = True
	return jsonify(response)



@app.route('/tappa_raggiunta')
def tappa_raggiunta():
	return render_template('tappa_raggiunta.html', posizione=hunts_list[session['targetHunt']].tappe[session['targetIndex']], tappa_attuale=session['targetIndex']+1, tot_tappe=len(hunts_list[session['targetHunt']].tappe))



@app.route('/set-selected-hunt', methods=['POST'])
def set_selected_hunt():
	# Accessing the data sent with POST request
	data = request.json
	session['targetHunt'] = data['id']
	response = True
	return jsonify(response)



@app.route('/check-position', methods=['POST'])
def check_position():
	# Accessing the data sent with POST request
	data = request.json
	distance_calculated = distance(hunts_list[session['targetHunt']].tappe[session['targetIndex']],Position(data['latitude'],data['longitude']))
	response = {}
	response['distance'] = distance_calculated
	if(distance_calculated<20):
		response['reached'] = True
		response['message'] = 'Congratulazioni hai raggiunto la posizione corretta!'
	else:
		response['reached'] = False
		response['message'] = f"Sei troppo lontano. Ti mancano ancora {distance_calculated} metri"
	return jsonify(response)



@app.route('/tappa')
def tappa():
	return render_template('tappa.html', posizione=hunts_list[session['targetHunt']].tappe[session['targetIndex']], tappa_attuale=session['targetIndex'], tot_tappe=len(hunts_list[session['targetHunt']].tappe))



@app.route('/fine')
def fine():
	return render_template('fine.html', tappa_attuale=-1)



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()
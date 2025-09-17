from flask import Flask, render_template, jsonify, request, session
from models.position import Position,distance
#import git


targetPositions = [
    Position(
		45.4382407, 
		12.3359719, 
		"Indizio 1",
		"Testo 1"
	),
    Position(
		45.4382407, 
		12.3359719, 
		"Indizio 2",
		"Test 2"
	)
]

app = Flask(__name__)
app.secret_key = 'super secret key'

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
	return render_template('start.html', tappa_attuale=-1)

@app.route('/next-position', methods=['POST','GET','REDIRECT'])
def next_position():
	# Accessing the data sent with POST request
	session['targetIndex'] = session['targetIndex'] + 1
	response = {'targetIndex':session['targetIndex']}
	if (session['targetIndex'] >= len(targetPositions)):
		response['ended'] = True
	return jsonify(response)



@app.route('/tappa_raggiunta')
def tappa_raggiunta():
	return render_template('tappa_raggiunta.html', posizione=targetPositions[session['targetIndex']], tappa_attuale=session['targetIndex']+1, tot_tappe=len(targetPositions))


@app.route('/check-position', methods=['POST'])
def check_position():
	# Accessing the data sent with POST request
	data = request.json
	distance_calculated = distance(targetPositions[session['targetIndex']],Position(data['latitude'],data['longitude']))
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
	return render_template('tappa.html', posizione=targetPositions[session['targetIndex']], tappa_attuale=session['targetIndex'], tot_tappe=len(targetPositions))


@app.route('/fine')
def fine():
	return render_template('fine.html', tappa_attuale=-1)


if __name__ == '__main__':
    app.run()
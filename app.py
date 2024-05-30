from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from models.position import Position,distance
import git

app = Flask(__name__)
app.secret_key = "3d6f45a5fc12445dbac2f59c3b6c7cb1"
app.config['SESSION_TYPE'] = 'filesystem'

targetPositions = [
	Position(44.060644, 12.565954, "Inizia la tua avventura nella piazza principale di Rimini, dove c'è una fontana adornata da una statua. Cerca sotto il suo sguardo vigile per il primo indizio!" ,"Ho cercato un minimo di storia...ma non ho trovato niente!!"),
	Position(44.056981, 12.571071, "Il passato romano di Rimini si riflette in questo maestoso arco. Guarda da vicino le sue decorazioni per trovare la prossima direzione da prendere" ,"testo di prova2" ),
	#Position(44.067290, 12.581946, "Dirigiti verso il luccichio del sole sull'acqua e troverai la prossima tappa, dove il suono delle onde si mescola con il richiamo dei gabbiani" ,"testo di prova3"),
	#Position(44.077141, 12.575021, "Da qui puoi avere una vista mozzafiato sulla città e sul mare. Osserva attentamente il panorama e troverai l'indizio che ti guiderà al prossimo traguardo della tua avventura" ,"testo di prova"),
	#Position(44.081782, 12.576638, "Dirigiti lungo il porto di Rimini, dove la storia e la cultura si mescolano con l'atmosfera marinaresca. Cerca tra le imbarcazioni e gli edifici colorati per trovar del marinaio la sposa" ,"testo di prova"),
	#Position(44.059817, 12.564048, "La fortezza medievale ti proteggerà dal caldo sole estivo mentre ti svela il segreto della prossima tappa. Guarda attentamente le mura per trovare la prossima tappa del tuo viaggio" ,"testo di prova"),
	#Position(44.059952, 12.569947, "La bellezza gotica di questo edificio ti svelerà il prossimo passo. C'è un dettaglio nascosto che ti guiderà alla tua destinazione successiva" ,"testo di prova"),
	#Position(44.060221, 12.575327, "Immergiti nell'antica grandezza dell'antica Roma, dove una volta echeggiavano i suoni dei combattimenti gladiatori" ,"testo di prova"),
	#Position(44.059247, 12.568537, "Nel cuore del centro storico, troverai una piazza che racconta storie di coraggio. Cerca tra i suoi monumenti per il tesoro che cerchi" ,"testo di prova"),
	#Position(44.062064, 12.567580, "Esplora le antiche mura del medico più famoso di Rimini, dove i segreti della medicina romana sono stati conservati" ,"testo di prova"),
	#Position(44.063674, 12.563827, "Via verso il maestoso Ponte, un simbolo dell'antica ingegneria romana che si erge fiero sul fiume Marecchia" ,"testo di prova"),
	#Position(44.064979, 12.565711, "Attraversa il fiume Marecchia e immergiti nell'atmosfera unica di questo borgo. Tra i colorati murales e le stradine acciottolate, troverai l'ultimo indizio!" ,"testo di prova"),
	Position(44.064965, 12.561880, "Ora via dove la pancia incontra il mare...si va a mangiare!!","testo di prova"),
]



app = Flask(__name__)
@app.route('/update_server', methods=['POST'])
def webhook():
	if request.method == 'POST':
		repo = git.Repo('/home/Chicco94')
		origin = repo.remotes.origin
		origin.pull('main')
		return 'Updated PythonAnywhere successfully', 200
	else:
		return 'Wrong event type', 400


@app.route('/')
def index():
	session.clear()
	session['targetIndex'] = 0
	return render_template('index.html')
	

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
	print("rendering")
	return render_template('tappa_raggiunta.html', posizione=targetPositions[session['targetIndex']])


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
	return render_template('tappa.html', posizione=targetPositions[session['targetIndex']])


@app.route('/fine')
def fine():
	return render_template('fine.html')


if __name__ == '__main__':
	app.run()
from flask import Flask, render_template, jsonify, request, session
from models.position import Position,distance
import git


targetPositions = [
    Position(43.5074191, 16.4416724, "Sotto il sole o con la pioggia, ogni mattina ti accoglie una piazza. Frutta e verdura qui puoi trovare, al cuore della città ti devi avvicinare.","Il mercato della verdura di Pazar è una delle parti più vivaci e autentiche di Spalato. Si trova proprio vicino al Palazzo di Diocleziano, unendo storia e quotidianità in un unico luogo. Qui, da secoli, gli abitanti della città acquistano frutta e verdura fresca, direttamente dai contadini locali. Questo mercato è il posto ideale per immergersi nella cultura locale e assaporare la vera essenza della città, tra i colori sgargianti dei prodotti e le voci animate dei venditori."),
    Position(43.5081085, 16.4412302, "Quattro sono le vie per entrare nel regno antico, Una splende al sole come un tesoro mistico. Non è d oro né di bronzo il suo nome, ma di un metallo che brilla al lume. Da qui il palazzo accoglie chi giunge, nelle mura che storia e leggenda unisce. Qual è questa porta che devi trovare, per proseguire il viaggio e non farti fermare?","La Porta d'Argento, o Porta Argentea, è una delle quattro porte principali del Palazzo di Diocleziano. Originariamente, tutte le porte avevano nomi legati ai metalli preziosi, riflettendo la grandezza e l'importanza del palazzo stesso. La Porta d'Argento era l'ingresso principale per coloro che venivano da est. Durante il Medioevo, la porta fu murata per proteggere la città, ma fu successivamente riaperta e oggi accoglie migliaia di visitatori. Da qui si può accedere direttamente alla Cattedrale di San Doimo, un altro gioiello della città di Spalato."),
    Position(43.5077513, 16.4404660, "Un tempo mausoleo di un imperatore potente, ora dimora di un santo, devoto e presente. Con la sua torre che sfiora il cielo, domina la città come un gioiello. Tra le sue mura risuona il passato, in ogni pietra, un mistero celato. Qual è questo luogo di fede e storia, dove il sacro e l antico si fondono in gloria?","La Cattedrale di San Doimo, o Cattedrale di San Domnius, è uno degli edifici sacri più antichi del mondo ancora in uso. Originariamente costruita come mausoleo per l'imperatore romano Diocleziano nel IV secolo, fu successivamente convertita in cattedrale nel VII secolo, dedicata a San Doimo, il santo patrono di Spalato. La sua torre campanaria è uno dei simboli più riconoscibili della città, e dalla sua cima si gode di una vista spettacolare su Spalato e il mare Adriatico. La fusione di elementi pagani e cristiani fa della cattedrale un esempio unico di continuità storica e culturale."),
    Position(43.5081301, 16.4400909, "Vicino al palazzo, un luogo circolare, che un tempo ospitava il potere imperiale. Un soffitto alto, aperto al cielo, da qui il sovrano osservava il suo impero. Il suono risuona nelle sue mura antiche, e il cuore di Spalato qui vive e palpita. Dove ti trovi, se alzi lo sguardo, vedi un cerchio di pietra, eterno e saldo?","Il Vestibolo è una grande sala circolare che fungeva da ingresso monumentale agli appartamenti imperiali del Palazzo di Diocleziano. Caratterizzato da un'imponente cupola, oggi aperta al cielo, il Vestibolo era il luogo in cui gli ospiti venivano accolti in maniera grandiosa prima di accedere agli alloggi dell'imperatore. L'acustica perfetta di questo spazio è sorprendente: spesso vi si esibiscono gruppi vocali dal vivo, offrendo ai visitatori un'esperienza acustica unica. Questo luogo è un esempio straordinario della grandiosità dell'architettura romana e della sua capacità di combinare funzione e bellezza."),
    Position(43.5094556, 16.4394830, "In un mondo di draghi, regine e re, dove il ferro e il fuoco decideranno chi c'è. Nelle mura di Spalato troverai, un regno di fantasia che il mondo incantò ormai. Qual è il luogo che cerchi, dimmi se sai, dove Westeros e Spalato si incontrano, vai!","Il Museo di Trono di Spade a Spalato è una meta imperdibile per i fan della celebre serie televisiva. Spalato è stata una delle location principali delle riprese della serie, e il museo celebra questa connessione unica. Al suo interno, i visitatori possono vedere riproduzioni fedeli del Trono di Spade, costumi, armi e oggetti di scena utilizzati durante le riprese. Il museo offre anche uno sguardo dietro le quinte della produzione, mostrando come le strade storiche di Spalato sono state trasformate in set cinematografici per dar vita ai luoghi iconici di Westeros."),
    Position(43.5109170, 16.4376662, "Tra luci e ombre, risuona la voce, di chi racconta storie con arte e con cuore. Non è un palazzo né un antico portone, ma qui la cultura è la vera padrona. Un sipario si alza, e il mondo appare, in un gioco di emozioni da ammirare. Qual è questo luogo dove la città si raduna, per vivere sogni alla luce di una luna?", "Il Teatro Nazionale di Spalato, inaugurato nel 1893, è uno dei teatri più antichi e importanti della Croazia. Questo magnifico edificio in stile neorinascimentale è il centro della vita culturale della città e ha ospitato spettacoli di opera, balletto, teatro e concerti per oltre un secolo. Durante la sua lunga storia, il teatro è stato un punto di riferimento per l'arte e la cultura croata, promuovendo il talento locale e internazionale. La sua facciata imponente e l'interno riccamente decorato offrono ai visitatori un'esperienza culturale raffinata, in un ambiente che unisce tradizione e bellezza architettonica."),
    Position(43.5087524, 16.4362362, "Un angolo d'Italia in una città dal cuore slavo, con archi e colonne in un quadro perfetto e raro. Aperta al mare e al cielo infinito, qui la storia incontra il presente, in un abbraccio deciso. Con portici eleganti che raccontano del passato, questa piazza ti attende, non hai forse indovinato?","Piazza Repubblica, conosciuta localmente come Prokurative, è uno degli spazi urbani più suggestivi di Spalato. Costruita a fine XIX secolo con un forte richiamo all'architettura veneziana, la piazza è circondata su tre lati da eleganti portici in stile neorinascimentale. Aperta sul lato occidentale verso il mare, la piazza è un luogo vivace dove si tengono concerti, festival ed eventi culturali durante tutto l'anno. La sua atmosfera raffinata e l'architettura distintiva la rendono un luogo perfetto per passeggiare e godersi la vista sulla Riva e sul porto di Spalato."),
    Position(43.5080759, 16.4364092, "Acque azzurre lambiscono la riva, dove il sole saluta mentre il giorno si avvia. Un cammino tra palme, caffè e sorrisi, qui la città vive i suoi momenti divisi. Passeggiando ascolti il dolce suono, del mare che racconta storie di ogni uomo. Dove ti trovi se il mare è il tuo compagno, e la brezza ti guida in questo luogo sovrano?","Il lungomare di Spalato, noto come Riva, è il cuore pulsante della vita cittadina. Completamente ristrutturato negli ultimi anni, questo elegante viale è il luogo dove gli abitanti di Spalato e i visitatori si incontrano per passeggiare, socializzare e rilassarsi di fronte al mare. Fiancheggiato da palme e affacciato sul porto, il lungomare offre una vista spettacolare sulle isole vicine e sul Palazzo di Diocleziano. La Riva è anche il luogo principale per eventi pubblici, celebrazioni e festival, rendendola uno degli spazi più amati e frequentati della città."),
    Position(43.5008704, 16.4431281, "Solitario si erge, guardiano del mare, con la sua luce che naviganti deve guidare. Anche nelle notti più scure e profonde, è lui che veglia e le rotte risponde. Un punto di riferimento per chi è lontano, e una meta finale per chi è a mano. Qual è questo luogo, alto e luminoso, che indica la fine del viaggio, misterioso?","Il faro di Spalato, situato in una delle posizioni più panoramiche della costa, è un simbolo di sicurezza e guida per i marinai che si avvicinano alla città. Questo faro, benché non tra i più grandi, ha un’importanza storica per la città, segnando il confine tra terra e mare. Costruito nel XIX secolo, il faro è una testimonianza dell importanza marittima di Spalato, un luogo dove la storia e la natura si incontrano. Dalla sua base si può godere di una vista spettacolare sul mare Adriatico, particolarmente suggestiva al tramonto, quando la luce del faro si accende per guidare i naviganti.")
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
	return render_template('index.html', tappa_attuale=-1)


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
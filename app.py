from flask import Flask, render_template, jsonify, request, session
from models.position import Position,distance
import git


targetPositions = [
    Position(
        45.4382407, 
        12.3359719, 
        "Sopra un fiume che sembra di seta, un ponte di marmo maestoso si erge con meta. Le botteghe ti invitano a fare un giro, mentre il mercato sottostante offre un chiaro respiro. Dove vai se il Gran Canale devi attraversare, e il ponte più famoso ti vuole abbracciare?",
        "Il Ponte di Rialto è il più antico dei quattro ponti che attraversano il Canal Grande e fu completato nel 1591. Originariamente costruito in legno, il ponte crollò più volte prima di essere ricostruito in pietra. È stato progettato dall'architetto Antonio da Ponte, che vinse una competizione contro alcuni dei più grandi architetti dell'epoca, tra cui Michelangelo. Oggi, il Ponte di Rialto è uno dei simboli più riconoscibili di Venezia e ospita negozi che vendono gioielli, souvenir e altri prodotti artigianali."
    ),
    Position(
		45.4348790, 
		12.3345567, 
		"Nascosta tra i palazzi, una spirale ascende, dove gradini a chiocciola la vista estende. Un segreto architettonico, unico nel suo stile, ti porta in alto, con un giro gentile. Dove devi andare se vuoi salire, su una scala che sembra quasi un gioiello da ammirare?",
		"La Scala Contarini del Bovolo è una scala a chiocciola esterna che fa parte del Palazzo Contarini. Costruita alla fine del XV secolo, la scala è un raro esempio di architettura rinascimentale a Venezia e deve il suo nome \"Bovolo\" (che in veneziano significa \"chiocciola\") alla sua struttura elicoidale. La scala offre una vista panoramica mozzafiato sui tetti di Venezia, e il suo design unico la rende una delle gemme nascoste della città."
	),
    Position(
		45.4321378, 
		12.3292795, 
		"Di legno è fatto, ma forte resiste, su un canale che l’arte attraversa e persiste. Da qui vedi chiese e palazzi splendenti, e il Bacino ti chiama con acque lucenti. Qual è questo ponte, che all’arte ti avvicina, tra Gallerie famose e la laguna vicina",
		"Il Ponte dell'Accademia è uno dei quattro ponti che attraversano il Canal Grande, e l'unico costruito in legno. Inaugurato nel 1933, il ponte è stato originariamente progettato come una struttura temporanea, ma è diventato un simbolo amato della città. Dal ponte si può godere di una delle viste più spettacolari di Venezia, che include la Basilica di Santa Maria della Salute e il Bacino di San Marco. È anche un punto di accesso per le Gallerie dell'Accademia, uno dei musei d'arte più importanti di Venezia."
	),
    Position(
		45.4341549, 
		12.3384483, 
		"Dove il leone con ali si posa, e il campanile saluta ogni cosa. Una basilica dorata racconta storie lontane, mentre i piccioni festeggiano in ampie campagne. Qual è questa piazza, la più grande e grandiosa, che tutti conoscono come il cuore di una città famosa?",
		"Piazza San Marco è l'unica piazza di Venezia, tutte le altre sono chiamate \"campi\". Considerata una delle piazze più belle del mondo, è stata descritta da Napoleone come \"il salotto d\'Europa\". La piazza è circondata da edifici storici, tra cui la Basilica di San Marco, con i suoi mosaici dorati, e il Campanile di San Marco, che offre una vista panoramica sulla città. La piazza è anche famosa per i suoi caffè storici, come il Caffè Florian, uno dei più antichi d\'Europa, aperto nel 1720."
	),
    Position(
		45.4335038, 
		12.3403416, 
		"Dove i dogi governavano con potere e saggezza, un palazzo maestoso che ha visto ogni ricchezza. Tra colonne di marmo e sale dorate, le decisioni della Repubblica furono celebrate. Dove devi andare se il potere vuoi trovare, in un palazzo che la storia non può dimenticare?",
		"Il Palazzo Ducale è stato il centro del potere politico veneziano per secoli. Sede del Doge e del governo della Repubblica di Venezia, il palazzo è un capolavoro dell'architettura gotica veneziana. All'interno, si trovano sale riccamente decorate, come la Sala del Maggior Consiglio, dove si tenevano le riunioni del governo. Il palazzo è anche collegato alle Prigioni Nuove attraverso il famoso Ponte dei Sospiri, e ha una storia ricca di intrighi politici e artistici."
	),
    Position(
		45.4336499, 
		12.3409718, 
		"Un ponte chiuso, di pietra bianca, dove il prigioniero un ultimo sguardo lancia. Verso il canale si dirige il suo sguardo, con un sospiro lascia un ricordo amaro. Qual è questo ponte, che il destino lega, tra un palazzo di giustizia e una prigione cupa e ceca?",
		"Il Ponte dei Sospiri collega il Palazzo Ducale alle Prigioni Nuove ed è stato costruito all'inizio del XVII secolo. Il ponte prende il nome dai sospiri dei prigionieri che, attraversandolo, vedevano per l'ultima volta la luce del giorno e il Canal Grande prima di essere rinchiusi. Nonostante la sua storia triste, il ponte è diventato uno dei luoghi più romantici di Venezia, con una leggenda che dice che le coppie che si baciano sotto di esso al tramonto saranno unite per sempre."
	),
    Position(
		45.4340214, 
		12.3438845, 
		"Una passeggiata che affaccia sul mare, dove gondole e barche puoi ammirare. Da qui si vede la laguna estesa, e i venti salati raccontano ogni impresa. Qual è questo luogo, dove gli schiavi del mare venivano un tempo, per commercio e per mare?",
		"La Riva degli Schiavoni è una delle passeggiate più famose di Venezia, situata lungo il bacino di San Marco. Il nome deriva dagli \"Schiavoni\", i mercanti provenienti dalla Dalmazia (l'odierna Croazia) che commerciavano con Venezia e che abitavano nella zona. Questa passeggiata offre una vista spettacolare sulla laguna e sull'Isola di San Giorgio Maggiore. La Riva è stata un punto di incontro per secoli ed è costellata di palazzi storici, tra cui l'Hotel Danieli, uno degli alberghi più lussuosi di Venezia, che ha ospitato celebrità e reali di tutto il mondo."
	),
    Position(
		45.4348253, 
		12.3497775, 
		"Nella città dove i leoni son tanti, ne trovi uno antico, tra i più intriganti. Non viene da qui, ma da un’isola lontana, dove un tempo regnava una storia arcana. Portato a Venezia per il suo valore, sta a guardia di un museo, con tutto il suo splendore. Dove ti trovi, se questo leone cercare vuoi, tra marmi e miti, una storia scoprirai?",
		"Il Leone di Delos è una scultura antica che risale all'epoca greca, originaria dell'isola di Delos, uno dei siti archeologici più importanti del Mediterraneo. Il leone fu portato a Venezia nel XVII secolo e oggi si trova nei pressi dell'Arsenale, esposto all'interno del Museo Storico Navale. Questo leone, come molti altri in città, simboleggia la forza e la protezione, ma ha anche una storia che lo lega alla cultura e alla mitologia greca. Un pezzo di Grecia nel cuore di Venezia, che testimonia i legami culturali e storici che attraversano il Mediterraneo."
	),
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
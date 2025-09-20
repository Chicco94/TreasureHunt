from dataclasses import dataclass
from models.position import Position

@dataclass
class Hunt():
    id: int
    name:str
    description:str
    tappe:list[Position]

    def __str__(self):
        return f'Hunt(id={self.id}, name={self.name}, description={self.description})'
    
hunts_list = [
    Hunt(
        0,
        "Legnaro",
        "Caccia al tesoro a Legnaro, tra scienza, natura e storia.",
        [
            Position(45.354261, 11.963485,
				"Tra piatti deliziosi e un'accoglienza raffinata, trova il luogo dove l'acqua sembra impazzita. Un ristorante rinomato, il primo passo è qui: scopri il suo nome, inizia la tua caccia così!" ,
				"Ho cercato un minimo di storia...ma non ho trovato niente!!"
			),
            Position(45.352544, 11.950971,
				"Prosegui ora il tuo cammino, tra scienza e innovazione, trova il luogo dove l'universo è in esplorazione. Ricerca e particelle, la fisica qui regna sovrana, un istituto prestigioso, questa è la tua nuova tana!" ,
				"L'INFN è stato fondato nel 1951 ed è uno dei principali istituti di ricerca in Italia dedicati allo studio della fisica nucleare, subnucleare e delle particelle. L'obiettivo principale dell'INFN è esplorare i costituenti fondamentali della materia e le leggi che regolano l'universo."
            ),
            Position(45.345806, 11.958850,
				"Tra campi e coltivazioni, dove la scienza incontra la natura, cerca il luogo di studio e ricerca, una vera avventura. Qui crescono le piante e le idee a dismisura, Agripolis è il nome, questa è la tua prossima fermatura." ,
				"Agripolis è un campus universitario che ospita facoltà di agraria e veterinaria. È un centro di ricerca e formazione dove si studiano tecnologie agricole innovative e si promuove la sostenibilità ambientale."
			),
            Position(45.342959, 11.962612,
				"Un luogo di culto e di pace ti attende ora, con una torre che si erge alta, verso l'aurora. Le sue mura antiche raccontano storie senza età, trova il prossimo indizio e vai oltre con felicità.",
				"La Chiesa di San Biagio è un punto di riferimento storico e spirituale per la comunità di Legnaro. Costruita in epoca medievale, la chiesa presenta elementi architettonici e artistici di grande valore, tra cui affreschi e statue antiche."
			),
            Position(45.342535, 11.960570,
				"Immergiti nella natura, dove gli alberi sussurrano segreti antichi e la fauna è viva e prospera. Trova il sentiero giusto e segui il respiro del bosco,  il prossimo indizio è tra le fronde, ben nascosto." ,
				"Bosco Vivo è un'area naturale protetta dove è possibile esplorare la flora e la fauna locali. È un luogo ideale per passeggiate, birdwatching e per godere della tranquillità della natura."
			),
            Position(45.345850, 11.938429,
				"Attraversa l'acqua su un ponte stretto e lungo, qui natura e ingegno si incontrano in un'unica canzone. Cerca il tuo indizio lungo la passerella sospesa, il prossimo passo è alla tua attesa." ,
				"La passerella di Roncajette era un ponte pedonale che attraversava il fiume Bacchiglione. Offre una vista panoramica sul fiume e sui dintorni, ed è un esempio di ingegneria che si integra armoniosamente con l'ambiente naturale."
			),
            Position(45.321663, 11.941840,
				"Segui il corso d'acqua che scorre placido e sereno, dove il Bacchiglione incontra un ruscello meno ampio ma ameno. Cammina lungo le sue rive, tra natura e frescura, fino a trovare un piccolo <b>Fiumicello</b>, la tua prossima avventura." ,
				"Era da tanto che dovevamo fare un giro in bici e seguire il fiume mi sembrava un'idea carina :)"
			),
            Position(45.323556, 11.964892,
				"Là dove le giovani volpi si aprono al sapere, un luogo di crescita, educazione e pensiero. Tra banchi e aule, trova l'indizio nascosto, il tuo viaggio è ben disposto." ,
				"Lo so che non c'entra nulla, ma dovevo obbligarti a percorrere questa strada e non sapevo dove fare tappa :)"
			),
            Position(45.337477, 11.966914,
				"Ricorda quel momento speciale, tra risate e luce amica, in una via dove il tempo si ferma e la memoria si radica. Là abbiamo scattato una foto, catturando un ricordo caro, trova la strada di quel giorno felice, è il tuo prossimo faro." ,
				"Io non saprò fare indovinelli, ma chatGPT ci è andato davvero romantico su questa tappa XD"
			),
            Position(45.342997, 11.964686,
				"Un palazzo elegante, con una storia da raccontare, tra archi e sale, eleganza senza uguale. Cerca tra i dettagli, osserva con attenzione, segui questa direzione." ,
				"Palazzo Gemma è un elegante edificio storico situato nel centro di Legnaro. Conosciuto per la sua architettura distintiva e la sua storia affascinante, il palazzo ospita spesso eventi culturali e mostre."
			),
            Position(45.344197, 11.966608,
				"Per un dolce riposo, cerca un luogo di piacere, dove gelati e sorrisi si mescolano al piacere, con gusti colorati e sapori deliziosi." ,
				"Come ogni caccia che si rispetti...bisogna integrare le energie spese :)"
            ),
        ]
    ),
    Hunt(
        1,
        "Spalato",
        "Caccia al tesoro a Spalato, tra storia antica e bellezze naturali.",
        [
            Position(43.5074191, 16.4416724,
				"Sotto il sole o con la pioggia, ogni mattina ti accoglie una piazza. Frutta e verdura qui puoi trovare, al cuore della città ti devi avvicinare.",
                "Il mercato della verdura di Pazar è una delle parti più vivaci e autentiche di Spalato. Si trova proprio vicino al Palazzo di Diocleziano, unendo storia e quotidianità in un unico luogo. Qui, da secoli, gli abitanti della città acquistano frutta e verdura fresca, direttamente dai contadini locali. Questo mercato è il posto ideale per immergersi nella cultura locale e assaporare la vera essenza della città, tra i colori sgargianti dei prodotti e le voci animate dei venditori."
			),
            Position(43.5081085, 16.4412302,
				"Quattro sono le vie per entrare nel regno antico, Una splende al sole come un tesoro mistico. Non è d oro né di bronzo il suo nome, ma di un metallo che brilla al lume. Da qui il palazzo accoglie chi giunge, nelle mura che storia e leggenda unisce. Qual è questa porta che devi trovare, per proseguire il viaggio e non farti fermare?",
                "La Porta d'Argento, o Porta Argentea, è una delle quattro porte principali del Palazzo di Diocleziano. Originariamente, tutte le porte avevano nomi legati ai metalli preziosi, riflettendo la grandezza e l'importanza del palazzo stesso. La Porta d'Argento era l'ingresso principale per coloro che venivano da est. Durante il Medioevo, la porta fu murata per proteggere la città, ma fu successivamente riaperta e oggi accoglie migliaia di visitatori. Da qui si può accedere direttamente alla Cattedrale di San Doimo, un altro gioiello della città di Spalato."
			),
            Position(43.5077513, 16.4404660,
				"Un tempo mausoleo di un imperatore potente, ora dimora di un santo, devoto e presente. Con la sua torre che sfiora il cielo, domina la città come un gioiello. Tra le sue mura risuona il passato, in ogni pietra, un mistero celato. Qual è questo luogo di fede e storia, dove il sacro e l antico si fondono in gloria?",
                "La Cattedrale di San Doimo, o Cattedrale di San Domnius, è uno degli edifici sacri più antichi del mondo ancora in uso. Originariamente costruita come mausoleo per l'imperatore romano Diocleziano nel IV secolo, fu successivamente convertita in cattedrale nel VII secolo, dedicata a San Doimo, il santo patrono di Spalato. La sua torre campanaria è uno dei simboli più riconoscibili della città, e dalla sua cima si gode di una vista spettacolare su Spalato e il mare Adriatico. La fusione di elementi pagani e cristiani fa della cattedrale un esempio unico di continuità storica e culturale."
			),
            Position(43.5081301, 16.4400909,
				"Vicino al palazzo, un luogo circolare, che un tempo ospitava il potere imperiale. Un soffitto alto, aperto al cielo, da qui il sovrano osservava il suo impero. Il suono risuona nelle sue mura antiche, e il cuore di Spalato qui vive e palpita. Dove ti trovi, se alzi lo sguardo, vedi un cerchio di pietra, eterno e saldo?",
                "Il Vestibolo è una grande sala circolare che fungeva da ingresso monumentale agli appartamenti imperiali del Palazzo di Diocleziano. Caratterizzato da un'imponente cupola, oggi aperta al cielo, il Vestibolo era il luogo in cui gli ospiti venivano accolti in maniera grandiosa prima di accedere agli alloggi dell'imperatore. L'acustica perfetta di questo spazio è sorprendente: spesso vi si esibiscono gruppi vocali dal vivo, offrendo ai visitatori un'esperienza acustica unica. Questo luogo è un esempio straordinario della grandiosità dell'architettura romana e della sua capacità di combinare funzione e bellezza."
			),
            Position(43.5094556, 16.4394830,
				"In un mondo di draghi, regine e re, dove il ferro e il fuoco decideranno chi c'è. Nelle mura di Spalato troverai, un regno di fantasia che il mondo incantò ormai. Qual è il luogo che cerchi, dimmi se sai, dove Westeros e Spalato si incontrano, vai!",
                "Il Museo di Trono di Spade a Spalato è una meta imperdibile per i fan della celebre serie televisiva. Spalato è stata una delle location principali delle riprese della serie, e il museo celebra questa connessione unica. Al suo interno, i visitatori possono vedere riproduzioni fedeli del Trono di Spade, costumi, armi e oggetti di scena utilizzati durante le riprese. Il museo offre anche uno sguardo dietro le quinte della produzione, mostrando come le strade storiche di Spalato sono state trasformate in set cinematografici per dar vita ai luoghi iconici di Westeros."
			),
            Position(43.5109170, 16.4376662,
				"Tra luci e ombre, risuona la voce, di chi racconta storie con arte e con cuore. Non è un palazzo né un antico portone, ma qui la cultura è la vera padrona. Un sipario si alza, e il mondo appare, in un gioco di emozioni da ammirare. Qual è questo luogo dove la città si raduna, per vivere sogni alla luce di una luna?",
                "Il Teatro Nazionale di Spalato, inaugurato nel 1893, è uno dei teatri più antichi e importanti della Croazia. Questo magnifico edificio in stile neorinascimentale è il centro della vita culturale della città e ha ospitato spettacoli di opera, balletto, teatro e concerti per oltre un secolo. Durante la sua lunga storia, il teatro è stato un punto di riferimento per l'arte e la cultura croata, promuovendo il talento locale e internazionale. La sua facciata imponente e l'interno riccamente decorato offrono ai visitatori un'esperienza culturale raffinata, in un ambiente che unisce tradizione e bellezza architettonica."
			),
            Position(43.5087524, 16.4362362,
				"Un angolo d'Italia in una città dal cuore slavo, con archi e colonne in un quadro perfetto e raro. Aperta al mare e al cielo infinito, qui la storia incontra il presente, in un abbraccio deciso. Con portici eleganti che raccontano del passato, questa piazza ti attende, non hai forse indovinato?",
                "Piazza Repubblica, conosciuta localmente come Prokurative, è uno degli spazi urbani più suggestivi di Spalato. Costruita a fine XIX secolo con un forte richiamo all'architettura veneziana, la piazza è circondata su tre lati da eleganti portici in stile neorinascimentale. Aperta sul lato occidentale verso il mare, la piazza è un luogo vivace dove si tengono concerti, festival ed eventi culturali durante tutto l'anno. La sua atmosfera raffinata e l'architettura distintiva la rendono un luogo perfetto per passeggiare e godersi la vista sulla Riva e sul porto di Spalato."
			),
            Position(43.5080759, 16.4364092,
				"Acque azzurre lambiscono la riva, dove il sole saluta mentre il giorno si avvia. Un cammino tra palme, caffè e sorrisi, qui la città vive i suoi momenti divisi. Passeggiando ascolti il dolce suono, del mare che racconta storie di ogni uomo. Dove ti trovi se il mare è il tuo compagno, e la brezza ti guida in questo luogo sovrano?",
                "Il lungomare di Spalato, noto come Riva, è il cuore pulsante della vita cittadina. Completamente ristrutturato negli ultimi anni, questo elegante viale è il luogo dove gli abitanti di Spalato e i visitatori si incontrano per passeggiare, socializzare e rilassarsi di fronte al mare. Fiancheggiato da palme e affacciato sul porto, il lungomare offre una vista spettacolare sulle isole vicine e sul Palazzo di Diocleziano. La Riva è anche il luogo principale per eventi pubblici, celebrazioni e festival, rendendola uno degli spazi più amati e frequentati della città."
			),
            Position(43.5008704, 16.4431281,
				"Solitario si erge, guardiano del mare, con la sua luce che naviganti deve guidare. Anche nelle notti più scure e profonde, è lui che veglia e le rotte risponde. Un punto di riferimento per chi è lontano, e una meta finale per chi è a mano. Qual è questo luogo, alto e luminoso, che indica la fine del viaggio, misterioso?",
                "Il faro di Spalato, situato in una delle posizioni più panoramiche della costa, è un simbolo di sicurezza e guida per i marinai che si avvicinano alla città. Questo faro, benché non tra i più grandi, ha un’importanza storica per la città, segnando il confine tra terra e mare. Costruito nel XIX secolo, il faro è una testimonianza dell importanza marittima di Spalato, un luogo dove la storia e la natura si incontrano. Dalla sua base si può godere di una vista spettacolare sul mare Adriatico, particolarmente suggestiva al tramonto, quando la luce del faro si accende per guidare i naviganti."
            ),
        ]
    ),
    Hunt(
        2,
        "Rimini",
        "Caccia al tesoro a Rimini, tra storia antica e divertimento moderno.",
        [
            Position(44.060644, 12.565954,
				"Inizia la tua avventura nella piazza principale di Rimini, dove c'è una fontana adornata da una statua. Cerca sotto il suo sguardo vigile per il primo indizio!" ,
				"testo di prova1"
			),
            Position(44.056981, 12.571071,
				"Il passato romano di Rimini si riflette in questo maestoso arco. Guarda da vicino le sue decorazioni per trovare la prossima direzione da prendere" ,
				"testo di prova2" ),
            Position(44.067290, 12.581946,
				"Dirigiti verso il luccichio del sole sull'acqua e troverai la prossima tappa, dove il suono delle onde si mescola con il richiamo dei gabbiani" ,
				"testo di prova3"
			),
            Position(44.077141, 12.575021,
				"Da qui puoi avere una vista mozzafiato sulla città e sul mare. Osserva attentamente il panorama e troverai l'indizio che ti guiderà al prossimo traguardo della tua avventura" ,
				"testo di prova"
			),
            Position(44.081782, 12.576638,
				"Dirigiti lungo il porto di Rimini, dove la storia e la cultura si mescolano con l'atmosfera marinaresca. Cerca tra le imbarcazioni e gli edifici colorati per trovar del marinaio la sposa" ,
				"testo di prova"
			),
            Position(44.059817, 12.564048,
				"La fortezza medievale ti proteggerà dal caldo sole estivo mentre ti svela il segreto della prossima tappa. Guarda attentamente le mura per trovare la prossima tappa del tuo viaggio" ,
				"testo di prova"
			),
            Position(44.059952, 12.569947,
				"La bellezza gotica di questo edificio ti svelerà il prossimo passo. C'è un dettaglio nascosto che ti guiderà alla tua destinazione successiva" ,
				"testo di prova"
			),
            Position(44.060221, 12.575327,
				"Immergiti nell'antica grandezza dell'antica Roma, dove una volta echeggiavano i suoni dei combattimenti gladiatori" ,
				"testo di prova"
			),
            Position(44.059247, 12.568537,
				"Nel cuore del centro storico, troverai una piazza che racconta storie di coraggio. Cerca tra i suoi monumenti per il tesoro che cerchi" ,
				"testo di prova"
			),
            Position(44.062064, 12.567580,
				"Esplora le antiche mura del medico più famoso di Rimini, dove i segreti della medicina romana sono stati conservati" ,
				"testo di prova"
			),
            Position(44.063674, 12.563827,
				"Via verso il maestoso Ponte, un simbolo dell'antica ingegneria romana che si erge fiero sul fiume Marecchia" ,
				"testo di prova"
			),
            Position(44.064979, 12.565711,
				"Attraversa il fiume Marecchia e immergiti nell'atmosfera unica di questo borgo. Tra i colorati murales e le stradine acciottolate, troverai l'ultimo indizio!" ,
				"testo di prova"
			),
            Position(44.064965, 12.561880,
				"Ora via dove la pancia incontra il mare...si va a mangiare!!",
				"testo di prova"
            ),
        ]
    ),
    Hunt(
        3,
        "Venezia",
        "Caccia al tesoro a Venezia, tra canali, ponti e storia.",
        [
            Position(45.4382407, 12.3359719,
				"Sopra un fiume che sembra di seta, un ponte di marmo maestoso si erge con meta. Le botteghe ti invitano a fare un giro, mentre il mercato sottostante offre un chiaro respiro. Dove vai se il Gran Canale devi attraversare, e il ponte più famoso ti vuole abbracciare?" ,
				"Il Ponte di Rialto è il più antico dei quattro ponti che attraversano il Canal Grande e fu completato nel 1591. Originariamente costruito in legno, il ponte crollò più volte prima di essere ricostruito in pietra. È stato progettato dall'architetto Antonio da Ponte, che vinse una competizione contro alcuni dei più grandi architetti dell'epoca, tra cui Michelangelo. Oggi, il Ponte di Rialto è uno dei simboli più riconoscibili di Venezia e ospita negozi che vendono gioielli, souvenir e altri prodotti artigianali."
			),
            Position(45.4348790, 12.3345567,
				"Nascosta tra i palazzi, una spirale ascende, dove gradini a chiocciola la vista estende. Un segreto architettonico, unico nel suo stile, ti porta in alto, con un giro gentile. Dove devi andare se vuoi salire, su una scala che sembra quasi un gioiello da ammirare?" ,
				"La Scala Contarini del Bovolo è una scala a chiocciola esterna che fa parte del Palazzo Contarini. Costruita alla fine del XV secolo, la scala è un raro esempio di architettura rinascimentale a Venezia e deve il suo nome \"Bovolo\" (che in veneziano significa \"chiocciola\") alla sua struttura elicoidale. La scala offre una vista panoramica mozzafiato sui tetti di Venezia, e il suo design unico la rende una delle gemme nascoste della città." ),
            Position(45.4321378, 12.3292795,
				"Di legno è fatto, ma forte resiste, su un canale che l’arte attraversa e persiste. Da qui vedi chiese e palazzi splendenti, e il Bacino ti chiama con acque lucenti. Qual è questo ponte, che all’arte ti avvicina, tra Gallerie famose e la laguna vicina" ,
				"Il Ponte dell'Accademia è uno dei quattro ponti che attraversano il Canal Grande, e l'unico costruito in legno. Inaugurato nel 1933, il ponte è stato originariamente progettato come una struttura temporanea, ma è diventato un simbolo amato della città. Dal ponte si può godere di una delle viste più spettacolari di Venezia, che include la Basilica di Santa Maria della Salute e il Bacino di San Marco. È anche un punto di accesso per le Gallerie dell'Accademia, uno dei musei d'arte più importanti di Venezia."
			),
            Position(45.4341549, 12.3384483,
				"Dove il leone con ali si posa, e il campanile saluta ogni cosa. Una basilica dorata racconta storie lontane, mentre i piccioni festeggiano in ampie campagne. Qual è questa piazza, la più grande e grandiosa, che tutti conoscono come il cuore di una città famosa?" ,
				"Piazza San Marco è l'unica piazza di Venezia, tutte le altre sono chiamate \"campi\". Considerata una delle piazze più belle del mondo, è stata descritta da Napoleone come \"il salotto d\'Europa\". La piazza è circondata da edifici storici, tra cui la Basilica di San Marco, con i suoi mosaici dorati, e il Campanile di San Marco, che offre una vista panoramica sulla città. La piazza è anche famosa per i suoi caffè storici, come il Caffè Florian, uno dei più antichi d\'Europa, aperto nel 1720."
			),
            Position(45.4335038, 12.3403416,
				"Dove i dogi governavano con potere e saggezza, un palazzo maestoso che ha visto ogni ricchezza. Tra colonne di marmo e sale dorate, le decisioni della Repubblica furono celebrate. Dove devi andare se il potere vuoi trovare, in un palazzo che la storia non può dimenticare?" ,
				"Il Palazzo Ducale è stato il centro del potere politico veneziano per secoli. Sede del Doge e del governo della Repubblica di Venezia, il palazzo è un capolavoro dell'architettura gotica veneziana. All'interno, si trovano sale riccamente decorate, come la Sala del Maggior Consiglio, dove si tenevano le riunioni del governo. Il palazzo è anche collegato alle Prigioni Nuove attraverso il famoso Ponte dei Sospiri, e ha una storia ricca di intrighi politici e artistici."
			),
            Position(45.4336499, 12.3409718,
				"Un ponte chiuso, di pietra bianca, dove il prigioniero un ultimo sguardo lancia. Verso il canale si dirige il suo sguardo, con un sospiro lascia un ricordo amaro. Qual è questo ponte, che il destino lega, tra un palazzo di giustizia e una prigione cupa e ceca?" ,
				"Il Ponte dei Sospiri collega il Palazzo Ducale alle Prigioni Nuove ed è stato costruito all'inizio del XVII secolo. Il ponte prende il nome dai sospiri dei prigionieri che, attraversandolo, vedevano per l'ultima volta la luce del giorno e il Canal Grande prima di essere rinchiusi. Nonostante la sua storia triste, il ponte è diventato uno dei luoghi più romantici di Venezia, con una leggenda che dice che le coppie che si baciano sotto di esso al tramonto saranno unite per sempre."
			),
            Position(45.4340214, 12.3438845,
				"Una passeggiata che affaccia sul mare, dove gondole e barche puoi ammirare. Da qui si vede la laguna estesa, e i venti salati raccontano ogni impresa. Qual è questo luogo, dove gli schiavi del mare venivano un tempo, per commercio e per mare?" ,
				"La Riva degli Schiavoni è una delle passeggiate più famose di Venezia, situata lungo il bacino di San Marco. Il nome deriva dagli \"Schiavoni\", i mercanti provenienti dalla Dalmazia (l'odierna Croazia) che commerciavano con Venezia e che abitavano nella zona. Questa passeggiata offre una vista spettacolare sulla laguna e sull'Isola di San Giorgio Maggiore. La Riva è stata un punto di incontro per secoli ed è costellata di palazzi storici, tra cui l'Hotel Danieli, uno degli alberghi più lussuosi di Venezia, che ha ospitato celebrità e reali di tutto il mondo."
			),
            Position(45.4348253, 12.3497775,
				"Nella città dove i leoni son tanti, ne trovi uno antico, tra i più intriganti. Non viene da qui, ma da un’isola lontana, dove un tempo regnava una storia arcana. Portato a Venezia per il suo valore, sta a guardia di un museo, con tutto il suo splendore. Dove ti trovi, se questo leone cercare vuoi, tra marmi e miti, una storia scoprirai?" ,
				"Il Leone di Delos è una scultura antica che risale all'epoca greca, originaria dell'isola di Delos, uno dei siti archeologici più importanti del Mediterraneo. Il leone fu portato a Venezia nel XVII secolo e oggi si trova nei pressi dell'Arsenale, esposto all'interno del Museo Storico Navale. Questo leone, come molti altri in città, simboleggia la forza e la protezione, ma ha anche una storia che lo lega alla cultura e alla mitologia greca. Un pezzo di Grecia nel cuore di Venezia, che testimonia i legami culturali e storici che attraversano il Mediterraneo."
			),
        ]
    ),
    Hunt(
        4,
        "Lisbona",
        "Caccia al tesoro a Lisbona, tra miradouros, quartieri pittoreschi e simboli marittimi.",
        [
            # Cattedrale di Lisbona (Sé de Lisboa)
            Position(
                38.709845206654535, -9.133338956668137,
                "Un’antica cattedrale con torri gemelle custodisce secoli di fede e storia.",
                "La Sé de Lisboa, costruita nel 1147, è la chiesa più antica della città. Fu eretta subito dopo la riconquista cristiana dai Mori, in stile romanico, con influenze gotiche e barocche dovute a successive ristrutturazioni. Sopravvisse a diversi terremoti, che ne modificarono l’aspetto. Al suo interno si conservano reliquie e un chiostro che rivela resti romani e visigoti. È dedicata a Sant’Antonio, patrono di Lisbona, che qui fu battezzato. Le sue torri gemelle e la facciata severa la rendono uno dei simboli spirituali della capitale portoghese."
            ),
            # Quartiere dell’Alfama
            Position(
                38.7124771, -9.1298928,
                "Perditi nei vicoli che salgono e scendono come onde: scale di pietra, panni stesi al vento e voci che cantano storie antiche. Da quassù, un castello sorveglia ogni passo.",
                "L’Alfama è il quartiere più antico e pittoresco di Lisbona, sopravvissuto quasi intatto al terremoto del 1755. Le sue stradine tortuose e le case colorate raccontano l’anima autentica della città. Qui nacque e si sviluppò il fado, la musica tradizionale portoghese, dichiarata patrimonio UNESCO. L’atmosfera è unica: panni stesi alle finestre, azulejos decorativi e piccole taverne accoglienti. Dal quartiere si aprono splendidi miradouros sul Tago. È un luogo che conserva il cuore popolare e nostalgico della capitale."
            ),
            # Castello di São Jorge
            Position(
                38.7123645, -9.1329061,
                "Tra mura di pietra e torri che sfidano il tempo, i corvi custodiscono leggende di re e battaglie. Trova il punto più alto: da qui la città si svela come un tesoro sotto i tuoi occhi.",
				"Il Castello di São Jorge sorge su una collina che domina Lisbona, ed è uno dei monumenti più antichi della città. Le sue origini risalgono ai Visigoti e ai Mori, ma divenne fortezza reale dopo la conquista cristiana del 1147. Dal castello si gode una vista panoramica straordinaria sul Tago e sui quartieri sottostanti. Fu residenza reale fino al XVI secolo, quando i sovrani si trasferirono verso la zona fluviale. Oggi i suoi bastioni e torri raccontano la storia militare della città. È una tappa imprescindibile per comprendere le radici di Lisbona."
            ),
            # Praça do Comércio
            Position(
                38.7072535, -9.1357750,
                "Davanti al grande fiume, dove un tempo sorgeva il palazzo reale, si apre uno spazio immenso. Cavalieri di bronzo vegliano al centro: trova l’arco che custodisce l’ingresso alla città.",
				"La Praça do Comércio è una delle piazze più maestose d’Europa, simbolo della rinascita di Lisbona dopo il terremoto del 1755. Un tempo ospitava il Palazzo Reale Ribeira, distrutto dal sisma. Al centro sorge la statua equestre di re José I, realizzata dallo scultore Machado de Castro. L’imponente Arco da Rua Augusta segna l’accesso al centro storico. La piazza si apre direttamente sul fiume, evocando l’antico ruolo marittimo della città. Oggi è un luogo di ritrovo, di eventi e un biglietto da visita per chi arriva via mare."
            ),
            # Rua Augusta e Arco
            Position(38.7108610, -9.1376612,
				"Cammina lungo il tappeto di pietra bianca e nera: botteghe e profumi ti guidano verso una porta trionfale che sembra aprire il cielo. Solo chi osa attraversarla scoprirà la città segreta oltre le mura.",
				"La Rua Augusta è la via pedonale più vivace della Baixa. L’arco, completato nell’Ottocento, celebra la ricostruzione della città e porta scolpite figure allegoriche che rappresentano il Genio e la Gloria."
			),
            # Elevador de Santa Justa
            Position(
                38.7121815, -9.1394466,
                "Un gigante di ferro, con ingranaggi che sembrano usciti da un sogno di Jules Verne, sale verso il cielo. Chi osa prenderlo vedrà Lisbona dall’alto come un avventuriero in mongolfiera.",
				"L’Elevador de Santa Justa, inaugurato nel 1902, fu progettato da Raoul Mesnier de Ponsard, allievo di Gustave Eiffel. La sua struttura neogotica in ferro battuto è un capolavoro dell’ingegneria urbana di inizio Novecento. Collega la Baixa al Chiado, due quartieri centrali separati da un dislivello. Dalla cima si ammira una delle viste più belle di Lisbona, con la piazza Rossio e il fiume Tago. Originariamente funzionava a vapore, mentre oggi è elettrico. È non solo un mezzo di trasporto, ma anche un’icona turistica e architettonica della città."
            ),
            # Chiado
            Position(38.7105162, -9.1419973,
				"Tra librerie antiche e caffè profumati, un poeta di bronzo siede paziente. Avvicinati, magari ti sussurrerà un verso di fado o una storia di viaggiatori perduti.",
				"Il Chiado è il quartiere letterario e bohémien di Lisbona. Qui si trova la statua di Fernando Pessoa, davanti al celebre Café A Brasileira, uno dei luoghi di ritrovo degli intellettuali del ’900."
			),
            # Igreja de São Roque
            Position(38.7135151, -9.1434950,
				"In una facciata sobria si nasconde un segreto d’oro: altari che brillano come scrigni e storie di santi venuti da lontano. La vera ricchezza è celata all’interno.",
				"La chiesa di São Roque è una delle più antiche gesuite del mondo. All’interno custodisce cappelle riccamente decorate, tra cui la Cappella di San Giovanni Battista, un tempo considerata la più costosa del mondo."
			),
            # Miradouro de São Pedro de Alcântara
            Position(
                38.71497146310214, -9.144113597275993,
                "Da una terrazza giardino, Lisbona si apre davanti a te con castelli e tetti che brillano al sole.",
                "Il Miradouro de São Pedro de Alcântara è uno dei punti panoramici più famosi della città. Situato nel quartiere Bairro Alto, offre una vista spettacolare sul Castello di São Jorge e sul centro storico. La terrazza è ornata da statue e azulejos che raffigurano le principali attrazioni di Lisbona. È un luogo perfetto al tramonto, quando i colori caldi tingono i tetti e il Tago. Fu costruito nel XIX secolo come giardino pubblico, ed è ancora oggi uno spazio di relax per abitanti e visitatori. Qui si respira l’essenza romantica della città."
            ),
            # Praça do Rossio
            Position(38.7138741, -9.1390472,
				"Qui il selciato disegna onde sotto i tuoi piedi, come se il mare fosse intrappolato nella pietra. Trova il re che veglia sulla piazza e ascolta l’eco delle rivolte e dei festeggiamenti.",
				"Il Rossio è da secoli il cuore pulsante di Lisbona: teatro di mercati, feste e persino esecuzioni pubbliche. Oggi è famoso per i suoi caffè storici e la pavimentazione ondulata in stile portoghese"
			),
            # Praça dos Restauradores
            Position(38.7158360, -9.1410909,
				"Segui la via che scende verso la piazza dei restauratori: qui un obelisco svetta per ricordare battaglie vinte. Ma il vero premio non è di pietra… è dolce, caldo e profuma di crema: assaggialo e avrai conquistato Lisbona.",
				"Praça dos Restauradores celebra la rivolta del 1640 che riportò l’indipendenza al Portogallo dopo sessant’anni di dominio spagnolo. Oggi è anche un ottimo punto dove fermarsi in una delle pasticcerie vicine per gustare i famosi pastéis de nata, il tesoro più dolce della città."
			),
        ]
    ),
    Hunt(
        5,
        "Málaga",
        "Caccia al tesoro a Málaga, tra castelli moreschi, arte e mercati vivaci.",
        [
            # Castillo de Gibralfaro
            Position(
                36.7234153, -4.4114134,
                "Dall’alto di una collina veglia una fortezza antica, con mura che hanno visto secoli di battaglie e tramonti sul mare.",
                "Il Castillo de Gibralfaro fu costruito nel XIV secolo per difendere l’Alcazaba e la città sottostante. La sua posizione elevata offriva un punto di osservazione privilegiato sulla costa mediterranea. È celebre per l’assedio del 1487, quando i Re Cattolici conquistarono Málaga dopo mesi di resistenza. Oggi le sue mura ben conservate permettono di camminare lungo il perimetro con viste spettacolari. All’interno ospita un piccolo museo militare che racconta la storia della fortezza. È uno dei simboli storici più imponenti della città."
            ),
            # Alcazaba
            Position(
                36.7214830, -4.4159353,
                "Scendi tra mura e giardini profumati di aranci, entrerai in una fortezza che un tempo difendeva la città. Ogni cortile è un labirinto, ogni porta un enigma moresco.",
				"L’Alcazaba di Málaga è una delle fortezze musulmane meglio conservate in Spagna, costruita nell’XI secolo dalla dinastia hammudita. Era residenza dei governatori musulmani e al contempo struttura difensiva. I suoi giardini, cortili e decorazioni moresche rivelano l’influenza artistica dell’epoca. Collegata al castello di Gibralfaro da un passaggio fortificato, formava un sistema di difesa unico. Fu abbandonata per secoli e solo nel XX secolo iniziò il restauro. Oggi rappresenta una delle attrazioni più visitate della città."
            ),
            # Teatro Romano
            Position(
                36.7212080, -4.4172349,
                "Accanto all’Alcazaba si celano gradinate antiche, testimoni di spettacoli e voci di un impero lontano.",
                "Il Teatro Romano di Málaga risale al I secolo d.C., costruito durante l’impero di Augusto. Rimase in uso fino al III secolo, per poi cadere nell’oblio. Nei secoli successivi molte sue pietre furono riutilizzate per l’Alcazaba. Fu riscoperto solo nel 1951, nascosto sotto edifici moderni. Oggi, dopo lunghi restauri, ospita eventi culturali e spettacoli. È un prezioso esempio della presenza romana in Andalusia e si integra armoniosamente con i monumenti moreschi circostanti."
            ),
            # Plaza de la Merced
            Position(
                36.7233770, -4.4175685,
                "In una piazza vivace si erge un obelisco che veglia al centro dedicato alla libertà e la memoria di un grande artista.",
                "La Plaza de la Merced è una delle piazze più emblematiche di Málaga, punto d’incontro e cuore sociale della città. Al centro si trova l’obelisco in onore del generale Torrijos, eroe liberale del XIX secolo. Qui nacque Pablo Picasso, e la sua casa-museo si affaccia proprio sulla piazza. È un luogo vivace, animato da bar e caffè che ne fanno uno dei punti di ritrovo preferiti dagli abitanti. Durante le feste cittadine si trasforma in un palcoscenico di musica e tradizione. È una tappa che unisce storia, arte e vita quotidiana."
            ),
            # Museo Pablo Picasso
            Position(
                36.7217488, -4.4184291,
                "In una città che ha dato i natali a un genio, le tele parlano di occhi cubisti e colori che si trasformano. Trova il palazzo che custodisce i sogni del gran pittore.",
				"Il Museo Picasso di Málaga, inaugurato nel 2003, ospita oltre 200 opere del celebre artista nato qui nel 1881. Dipinti, sculture, ceramiche e disegni raccontano la sua carriera e la sua straordinaria capacità innovativa. L’edificio è un palazzo rinascimentale ristrutturato, che unisce storia e modernità. È una delle istituzioni culturali più visitate della città. Il museo ha contribuito a rilanciare Málaga come capitale dell’arte contemporanea. Visitandolo si comprende meglio l’evoluzione di Picasso e il suo legame con la città natale."
            ),
            # Cattedrale di Málaga (“La Manquita”)
            Position(
                36.7200911, -4.4200044,
                "Guarda in alto: una torre svetta fiera, l’altra… manca. Il popolo le ha dato un soprannome affettuoso: cerca la chiesa incompleta e ascolta il silenzio delle sue navate.",
				"La Cattedrale di Málaga, soprannominata “La Manquita” (la monca), deve il suo nome alla torre sud mai completata. Costruita tra il XVI e il XVIII secolo, fonde elementi gotici, rinascimentali e barocchi. La sua facciata riccamente decorata e l’interno luminoso ne fanno un capolavoro architettonico. Al suo interno si trovano magnifici cori lignei e opere d’arte rinascimentali. È uno dei simboli religiosi più importanti della città. Nonostante l’incompletezza, la sua imponenza la rende unica e affascinante."
            ),
            # Calle Larios
            Position(
                36.7184674, -4.4214777,
                "Cammina tra vetrine e profumi, su un tappeto di marmo lucido che brilla al tramonto. Questa via elegante è il cuore pulsante dello shopping… ma attento: potresti perderti tra le sue luci.",
				"Calle Marqués de Larios è la via più famosa di Málaga, inaugurata nel 1891. È nota per le sue eleganti architetture ottocentesche e per essere il cuore dello shopping cittadino. Durante tutto l’anno ospita eventi culturali, sfilate e celebrazioni. A Natale si illumina con spettacolari giochi di luci che attraggono visitatori da tutta la Spagna. È pedonale, rendendola perfetta per passeggiare tra negozi e caffè. Rappresenta il volto moderno e cosmopolita di Málaga, in dialogo con la sua storia."
            ),
            # Plaza de la Constitución
            Position(
                36.7211223, -4.4219976,
                "Al cuore della città, dove da secoli si decide il destino di Málaga, una fontana sorride al sole. Da qui partono tutte le strade: trovala e ti avvicinerai al tesoro finale.",
				"La Plaza de la Constitución è da secoli il centro politico e sociale di Málaga. In epoca medievale ospitava il municipio e il mercato cittadino. Oggi è circondata da edifici storici e da caffè che la rendono sempre viva. Durante la Settimana Santa è uno dei luoghi principali delle processioni. È anche il punto di partenza della celebre Feria de Málaga, la festa estiva più importante della città. La sua centralità ne fa un crocevia culturale e identitario per gli abitanti."
            ),
            # Mercado Central de Atarazanas – Tesoro finale
            Position(
                36.7182360, -4.4239058,
                "Segui i profumi del mare e delle spezie: una grande vetrata colorata ti guida verso un mondo di colori e sapori. Qui troverai il tesoro più gustoso della città.",
				"Il Mercado Central de Atarazanas si trova in un edificio del XIX secolo costruito sul sito di un antico arsenale arabo. La sua facciata conserva ancora l’arco originale moresco, testimonianza del passato musulmano di Málaga. All’interno ospita decine di bancarelle con prodotti freschi: pesce, frutta, spezie e tapas. È un luogo animato, frequentato da abitanti e turisti. La vetrata colorata raffigurante scene della città è uno dei suoi tratti distintivi. Visitandolo si vive la Málaga più autentica e conviviale."
            ),
        ]
    ),
    Hunt(
        6,
        "Alicante",
        "Caccia al tesoro ad Alicante, tra castelli, spiagge e tapas.",
        [
            # Explanada de España
            Position(
                38.343224815602774, -0.4831886528356794,
                "Un tappeto di onde di marmo bianco, rosso e nero ti accompagna tra palme che ondeggiano al vento. Segui il viale fino a scoprire il mare.",
                "L’Explanada de España è una passeggiata iconica di Alicante, lunga oltre 500 metri e decorata con più di sei milioni di tessere di marmo. Il disegno ondulato ricorda le onde del mare e la rende unica nel suo genere. Fiancheggiata da palme, è il luogo ideale per passeggiare al tramonto. Qui si svolgono concerti, mercatini e incontri quotidiani. È un punto di ritrovo per abitanti e turisti. La sua eleganza mediterranea incarna lo spirito marittimo della città."
            ),
            # Ayuntamiento de Alicante
            Position(
                38.34514337283181, -0.4812205534657148,
                "Davanti a te si erge un palazzo solenne, con due torri che vegliano sulla città. Ma il vero segreto è all’ingresso: cerca il punto zero da cui nasce l’altitudine spagnola.",
                "L’Ayuntamiento de Alicante è il municipio cittadino, costruito nel XVII secolo in stile barocco. La sua facciata è arricchita da torri gemelle e decorazioni elaborate. All’interno si trova la famosa “cota cero”, il punto zero da cui si misurano le altitudini in Spagna. È un edificio che unisce bellezza architettonica e funzione pubblica. Nel corso dei secoli ha ospitato eventi solenni e politici importanti. È uno dei simboli del potere civile e della storia amministrativa di Alicante."
            ),
            # Basilica de Santa María
            Position(
                38.34605783193618, -0.47952710934089887,
                "Una chiesa sorta dalle ceneri di una moschea, con torri che sembrano guardiani di pietra. Osserva la sua porta barocca e lascia che ti racconti secoli di fede.",
                "La Basilica de Santa María è la chiesa più antica di Alicante, costruita sui resti di una moschea araba nel XIV secolo. In stile gotico-valenzano, conserva elementi barocchi aggiunti nei secoli. La sua facciata è dominata da due torri asimmetriche che la rendono particolare. All’interno custodisce opere d’arte e un imponente altare maggiore rococò. È un luogo simbolico che racconta la trasformazione religiosa e culturale della città. Ancora oggi ospita importanti celebrazioni liturgiche."
            ),
            # Museo de Arte Contemporáneo (MACA)
            Position(
                38.34623630461506, -0.47968808316869777,
                "In un antico granaio si nascondono colori, linee e visioni moderne. Entra e scoprirai i sogni astratti di artisti che hanno cambiato la storia dell’arte.",
                "Il MACA raccoglie opere di Miró, Dalí e Picasso, oltre a importanti collezioni di arte contemporanea spagnola. L’edificio barocco che lo ospita risale al XVII secolo."
            ),
            # Barrio de Santa Cruz
            Position(
                38.347796346146424, -0.4826606997265488,
                "Case bianche, fiori colorati e scale strette: questo quartiere è un labirinto che profuma di mare e tradizione. Perditi tra i suoi vicoli e sentirai il cuore antico di Alicante.",
                "Il Barrio de Santa Cruz è il cuore storico di Alicante, un quartiere pittoresco che conserva l’anima autentica della città. Le sue case bianche con balconi fioriti e piastrelle colorate ricordano i villaggi andalusi. Le stradine in salita offrono scorci spettacolari verso il castello e il mare. È il luogo dove tradizione e quotidianità si fondono: feste popolari, musica e processioni animano le sue vie. Qui si respira l’essenza mediterranea, fatta di convivialità e colori. Passeggiarvi è come fare un salto indietro nel tempo."
            ),
            # Castillo de Santa Bárbara
            Position(
                38.34868168606967, -0.47697036121888875,
                "Dall’alto di una montagna che sembra un volto addormentato, una fortezza sorveglia il mare e la città. Scala le sue mura e scoprirai panorami che parlano di battaglie antiche.",
                "Il Castillo de Santa Bárbara domina Alicante dal Monte Benacantil, a 166 metri di altezza. Fu costruito dai Mori nel IX secolo e ampliato nei secoli successivi. La sua posizione strategica permetteva di controllare tutta la baia e difendere la città dalle invasioni. Durante la dominazione cristiana divenne una delle fortezze più importanti del Mediterraneo. Oggi offre panorami spettacolari sulla costa e ospita mostre ed eventi culturali. È un simbolo di Alicante e uno dei luoghi più visitati della città."
            ),
            # Placa de Bous d’Alacant
            Position(
                38.352224317798246, -0.4847408188825469,
                "Cerca il cerchio perfetto di pietra: un’arena dove un tempo il ruggito del pubblico accompagnava corride e spettacoli. Oggi è un luogo di cultura e memoria.",
                "La Plaza de Bous d’Alacant, inaugurata nel 1848, è una delle arene più grandi della Comunità Valenciana. Ha ospitato corride, concerti ed eventi di massa. La sua architettura circolare può accogliere migliaia di spettatori, rendendola un punto di riferimento per la città. Nei secoli ha visto cambiare le mode e le tradizioni popolari. Oggi continua a essere un luogo vivo di manifestazioni culturali. La sua imponenza testimonia la lunga tradizione della tauromachia e dello spettacolo in Spagna."
            ),
            # Castell de Sant Ferran
            Position(
                38.35096913106977, -0.49109106139458775,
                "Non tutti guardano questa fortezza, ma le sue mura hanno difeso la città in tempi difficili. Cerca il castello dimenticato che sorveglia Alicante dall’interno.",
                "Il Castell de Sant Ferran fu costruito nel XIX secolo come rinforzo difensivo durante la Guerra d’Indipendenza spagnola. A differenza del Castillo de Santa Bárbara, non ebbe mai un ruolo militare rilevante. La sua struttura, oggi parzialmente in rovina, è circondata da un grande parco urbano. È un luogo perfetto per passeggiate tranquille e per ammirare Alicante da una prospettiva diversa. Poco conosciuto dai turisti, rappresenta un angolo silenzioso e suggestivo della città. È un monumento che ricorda i cambiamenti storici di Alicante."
            ),
            # Mercado Central de Alicante – Tesoro finale
            Position(
                38.34854993921596, -0.4863498678162601,
                "Entra dove i colori esplodono e i profumi si mescolano: frutta, spezie, pesce e dolci ti guidano verso il tesoro più goloso. Qui, tra le bancarelle, ti aspetta la ricompensa.",
                "Il Mercado Central de Alicante, inaugurato nel 1921, è un edificio in stile modernista ricco di vetrate e decorazioni. All’interno ospita oltre 200 bancarelle di prodotti freschi: pesce, carne, frutta e specialità locali. È un luogo vibrante, cuore pulsante della vita quotidiana cittadina. Sopravvissuto a bombardamenti durante la Guerra Civile, conserva una memoria storica importante. Oggi è amato tanto dagli abitanti quanto dai turisti. È la conclusione ideale di una caccia al tesoro tra sapori e tradizioni."
            ),
        ]
    ),
    Hunt(
        7,
        "Siviglia",
        "Caccia al tesoro a Siviglia, tra palazzi moreschi, piazze vivaci e tradizioni andaluse.",
        [
            # Torre del Oro
            Position(
                37.3824815054664, -5.996172410691331,
                "Vicino al fiume s’innalza una torre che un tempo brillava come l’oro. Custodiva segreti e ricchezze: riuscirai a svelarli guardando le sue mura?",
                "La Torre del Oro fu costruita nel XIII secolo dai Mori come parte delle mura difensive lungo il Guadalquivir. Il suo nome deriva dai riflessi dorati delle piastrelle che la rivestivano. Per secoli controllò l’accesso al porto, cuore dei commerci con le Americhe. Usata come prigione e deposito di polvere da sparo, ha attraversato guerre e restauri. Oggi ospita un museo navale e dalla sua cima si gode una vista unica sulla città."
            ),
            # Parque de María Luisa
            Position(
                37.3735784872386, -5.987907389415148,
                "Entra nel giardino dei sogni: tra alberi secolari, fontane e padiglioni esotici. Segui il canto degli uccelli e troverai la strada.",
                "Il Parque de María Luisa è il polmone verde di Siviglia, donato alla città nel 1893 dalla duchessa di Montpensier. Progettato in stile romantico, è ricco di viali ombreggiati, laghetti e padiglioni scenografici. Durante l’Esposizione Iberoamericana del 1929 ospitò padiglioni oggi trasformati in musei. Qui convivono flora mediterranea ed esotica, con pappagalli che si mescolano agli aranci. È uno dei luoghi più amati dai sivigliani per passeggiare e trovare sollievo dalla calura estiva."
            ),
            # Museo de Artes y Costumbres Populares de Sevilla
            Position(
                37.37190099734513, -5.987678707790162,
                "In un elegante padiglione scoprirai la vita quotidiana di un tempo: abiti, ceramiche e tradizioni che raccontano l’anima andalusa.",
                "Ospitato nel padiglione mudejar dell’Esposizione del 1929, il Museo delle Arti e Tradizioni Popolari custodisce testimonianze uniche della vita andalusa. Collezioni di ceramiche di Triana, strumenti musicali, tessuti e artigianato mostrano la ricchezza della cultura popolare. L’edificio stesso è un gioiello architettonico che fonde elementi arabi e rinascimentali. È un viaggio nel quotidiano, dalle feste ai mestieri. Qui si respira l’anima autentica di Siviglia, lontana dai grandi monumenti."
            ),
            # Plaza de España
            Position(
                37.377391994584464, -5.986142563659162,
                "Un abbraccio di mattoni e maioliche, ponti e canali ti circondano. Solo chi percorre l’intero semicerchio troverà la via.",
                "La Plaza de España fu costruita per l’Esposizione Iberoamericana del 1929 ed è considerata uno dei luoghi più spettacolari di Siviglia. Progettata dall’architetto Aníbal González, fonde stili rinascimentali, barocchi e moreschi. Ogni provincia spagnola è rappresentata da splendidi azulejos decorativi lungo il colonnato. Il canale interno permette giri in barca, aggiungendo fascino al luogo. La piazza è apparsa in diversi film, tra cui Star Wars e Lawrence d’Arabia. È un simbolo della grandezza spagnola del Novecento."
            ),
            # Archivo de Indias
            Position(
                37.384520696278564, -5.9935123809832636,
                "Custode silenzioso di rotte e segreti, qui sono conservate le memorie del Nuovo Mondo.",
                "L’Archivo General de Indias conserva milioni di documenti sulla storia della colonizzazione spagnola nelle Americhe e nelle Filippine. Fondato nel XVI secolo per centralizzare le carte dell’impero, oggi è patrimonio UNESCO. Qui si trovano lettere di Colombo, mappe, registri e resoconti dei conquistadores. L’edificio, in stile rinascimentale, fu progettato da Juan de Herrera. Visitandolo si tocca con mano l’epoca delle grandi esplorazioni. È una miniera di tesori per storici e viaggiatori curiosi."
            ),
            # Real Alcázar
            Position(
                37.38511776267362, -5.991877239494301,
                "Un palazzo dalle mille vite, dove re cristiani e sovrani moreschi lasciarono tracce d’eternità.",
                "Il Real Alcázar di Siviglia è uno dei complessi monumentali più importanti di Spagna, riconosciuto come patrimonio UNESCO. Originariamente costruito come fortezza araba, fu trasformato in palazzo reale dai sovrani cristiani. Lo stile mudejar domina, con decorazioni geometriche, stucchi finissimi e giardini profumati di aranci. È ancora oggi residenza ufficiale della famiglia reale spagnola a Siviglia. Alcune scene di Game of Thrones sono state girate nei suoi cortili. Ogni angolo racconta secoli di storia e cultura."
            ),
            # Cattedrale di Siviglia e Giralda
            Position(
                37.38514662926833, -5.992989501696389,
                "Una torre che fu minareto ora sfida il cielo. Qui fede e storia si intrecciano nei secoli.",
                "La Cattedrale di Siviglia è una delle più grandi chiese gotiche al mondo, costruita nel XV secolo sul sito della moschea maggiore. All’interno si trova la tomba di Cristoforo Colombo e un imponente altare maggiore. La Giralda, torre campanaria, era in origine un minareto almohade del XII secolo. Il suo profilo domina la città ed è accessibile tramite rampe, pensate per salire a cavallo. Dal suo punto più alto si gode una vista mozzafiato. È un simbolo della potenza religiosa e culturale di Siviglia."
            ),
            # Barrio de Santa Cruz
            Position(
                37.386238870365936, -5.990045489094412,
                "Addentrati in vicoli stretti dove il tempo sembra fermarsi. Tra aranci in fiore e balconi colorati, ascolta i sussurri delle antiche leggende.",
                "Il Barrio de Santa Cruz è il quartiere più pittoresco di Siviglia, un labirinto di viuzze eredità del passato ebraico della città. Case imbiancate a calce, piazzette con aranci e balconi fioriti creano un’atmosfera romantica. Qui nacquero leggende e racconti popolari che ancora affascinano i visitatori. Fu il quartiere ebraico fino alla cacciata del 1492. Passeggiando si scoprono scorci segreti e silenzi lontani dal caos. È uno dei luoghi più autentici per vivere l’anima andalusa."
            ),
            # Metropol Parasol (Las Setas)
            Position(
                37.39283724091993, -5.991940012228259,
                "Un enorme fungo di legno che sembra venire dal futuro: saprai trovarti sotto le sue ombre?",
                "Il Metropol Parasol, soprannominato “Las Setas” (i funghi), è una struttura contemporanea inaugurata nel 2011. Realizzata in legno e cemento, è una delle più grandi costruzioni lignee del mondo. La sua forma futuristica ha ridisegnato Plaza de la Encarnación, creando un contrasto con l’antico centro storico. Ospita un mercato al piano terra, un museo archeologico nel sottosuolo e una passerella panoramica sul tetto. È un esempio di come Siviglia unisca tradizione e modernità. Di sera si illumina regalando scenografie spettacolari."
            ),
            # Monumento a San Fernando
            Position(
                37.38860646350063, -5.995488071655011,
                "Al centro di una piazza variopinta si erge il cavaliere che conquistò Siviglia. Solo chi riconoscerà il re-santo troverà la prossima traccia.",
                "Il Monumento a San Fernando si trova nella Plaza Nueva e commemora il re che riconquistò Siviglia ai Mori nel 1248. La statua equestre mostra il sovrano con spada e croce, simboli del suo potere religioso e militare. Fu inaugurata nel 1924 ed è circondata da edifici storici e caffè. San Fernando è patrono della città e la sua figura è ancora oggi venerata. La piazza è un punto d’incontro vivace e centrale, cuore della vita cittadina. Qui storia e quotidianità si fondono armoniosamente."
            ),
            # Plaza de Toros de la Maestranza
            Position(
                37.38537079635972, -5.998813052731079,
                "Un cerchio bianco e oro ti attende: luogo di passioni, sfide e applausi. Qui il tempo scorre al ritmo della tradizione.",
                "La Plaza de Toros de la Maestranza è una delle arene più antiche e prestigiose di Spagna. Costruita nel XVIII secolo, è famosa per la sua pianta ellittica e la facciata barocca bianca e gialla. Qui si svolgono ancora oggi corride durante la Feria de Abril. Ospita anche un museo che racconta la storia della tauromachia e dei toreri leggendari. L’arena può accogliere migliaia di spettatori ed è considerata la “cattedrale” della corrida. È un simbolo controverso ma radicato della cultura spagnola."
            ),
            # Mercado de Triana – Tesoro finale
            Position(
                37.38553943787021, -6.003180343155216,
                "Oltre il ponte, in un quartiere di marinai e ceramisti, scoprirai il mercato dei colori. Qui ti attende il tesoro più goloso: tapas e sapori autentici.",
                "Il Mercado de Triana sorge sulle rovine del Castello di San Jorge, antica sede dell’Inquisizione. Oggi è uno dei mercati più vivaci di Siviglia, ricco di bancarelle di pesce fresco, tapas e prodotti locali. Ogni mattina si anima di voci e colori, punto di ritrovo per abitanti e turisti. La struttura moderna si integra con resti storici visibili ancora oggi. Qui si respira la vera anima del quartiere di Triana, culla del flamenco e dell’artigianato ceramico. È la conclusione perfetta di un viaggio tra storia e gusto."
            ),
        ]
    )
]
            
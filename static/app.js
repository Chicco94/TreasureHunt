
var targetPositions = [
    { latitude: 45.354261, longitude: 11.963485, hintMessage:"Tra piatti deliziosi e un'accoglienza raffinata, trova il luogo dove l'acqua sembra impazzita. Un ristorante rinomato, il primo passo è qui: scopri il suo nome, inizia la tua caccia così!" , info:"Ho cercato un minimo di storia...ma non ho trovato niente!!"},
    { latitude: 45.352544, longitude: 11.950971, hintMessage:"Prosegui ora il tuo cammino, tra scienza e innovazione, trova il luogo dove l'universo è in esplorazione. Ricerca e particelle, la fisica qui regna sovrana, un istituto prestigioso, questa è la tua nuova tana!" , info:"L'INFN è stato fondato nel 1951 ed è uno dei principali istituti di ricerca in Italia dedicati allo studio della fisica nucleare, subnucleare e delle particelle. L'obiettivo principale dell'INFN è esplorare i costituenti fondamentali della materia e le leggi che regolano l'universo." },
    { latitude: 45.345806, longitude: 11.958850, hintMessage:"Tra campi e coltivazioni, dove la scienza incontra la natura, cerca il luogo di studio e ricerca, una vera avventura. Qui crescono le piante e le idee a dismisura, Agripolis è il nome, questa è la tua prossima fermatura." , info:"Agripolis è un campus universitario che ospita facoltà di agraria e veterinaria. È un centro di ricerca e formazione dove si studiano tecnologie agricole innovative e si promuove la sostenibilità ambientale." },
    { latitude: 45.342959, longitude: 11.962612, hintMessage:"Un luogo di culto e di pace ti attende ora, con una torre che si erge alta, verso l'aurora. Le sue mura antiche raccontano storie senza età, trova il prossimo indizio e vai oltre con felicità.", info:"La Chiesa di San Biagio è un punto di riferimento storico e spirituale per la comunità di Legnaro. Costruita in epoca medievale, la chiesa presenta elementi architettonici e artistici di grande valore, tra cui affreschi e statue antiche." },
    { latitude: 45.342535, longitude: 11.960570, hintMessage:"Immergiti nella natura, dove gli alberi sussurrano segreti antichi e la fauna è viva e prospera. Trova il sentiero giusto e segui il respiro del bosco,  il prossimo indizio è tra le fronde, ben nascosto." , info:"Bosco Vivo è un'area naturale protetta dove è possibile esplorare la flora e la fauna locali. È un luogo ideale per passeggiate, birdwatching e per godere della tranquillità della natura." },
    { latitude: 45.345850, longitude: 11.938429, hintMessage:"Attraversa l'acqua su un ponte stretto e lungo, qui natura e ingegno si incontrano in un'unica canzone. Cerca il tuo indizio lungo la passerella sospesa, il prossimo passo è alla tua attesa." , info:"La passerella di Roncajette era un ponte pedonale che attraversava il fiume Bacchiglione. Offre una vista panoramica sul fiume e sui dintorni, ed è un esempio di ingegneria che si integra armoniosamente con l'ambiente naturale." },
    { latitude: 45.321663, longitude: 11.941840, hintMessage:"Segui il corso d'acqua che scorre placido e sereno, dove il Bacchiglione incontra un ruscello meno ampio ma ameno. Cammina lungo le sue rive, tra natura e frescura, fino a trovare un piccolo <b>Fiumicello</b>, la tua prossima avventura." , info:"Era da tanto che dovevamo fare un giro in bici e seguire il fiume mi sembrava un'idea carina :)" },
    { latitude: 45.323556, longitude: 11.964892, hintMessage:"Là dove le giovani volpi si aprono al sapere, un luogo di crescita, educazione e pensiero. Tra banchi e aule, trova l'indizio nascosto, il tuo viaggio è ben disposto." , info:"Lo so che non c'entra nulla, ma dovevo obbligarti a percorrere questa strada e non sapevo dove fare tappa :)" },
    { latitude: 45.337477, longitude: 11.966914, hintMessage:"Ricorda quel momento speciale, tra risate e luce amica, in una via dove il tempo si ferma e la memoria si radica. Là abbiamo scattato una foto, catturando un ricordo caro, trova la strada di quel giorno felice, è il tuo prossimo faro." , info:"Io non saprò fare indovinelli, ma chatGPT ci è andato davvero romantico su questa tappa XD" },
    { latitude: 45.342997, longitude: 11.964686, hintMessage:"Un palazzo elegante, con una storia da raccontare, tra archi e sale, eleganza senza uguale. Cerca tra i dettagli, osserva con attenzione, segui questa direzione." , info:"Palazzo Gemma è un elegante edificio storico situato nel centro di Legnaro. Conosciuto per la sua architettura distintiva e la sua storia affascinante, il palazzo ospita spesso eventi culturali e mostre." },
    { latitude: 45.344197, longitude: 11.966608, hintMessage:"Per un dolce riposo, cerca un luogo di piacere, dove gelati e sorrisi si mescolano al piacere, con gusti colorati e sapori deliziosi." , info:"Come ogni caccia che si rispetti...bisogna integrare le energie spese :)" }
];


var targetIndex = 0; // Indice della posizione di destinazione attuale
function start() {
    document.getElementById("getLocationButton").style.display = "block";
    document.getElementById("hintMessage").style.display = "block";
    document.getElementById("startButton").style.display = "none";
    document.getElementById("hintMessage").innerHTML = targetPositions[targetIndex].hintMessage;
}


function nextLocation() {
    targetIndex++;
    if(targetIndex >= targetPositions.length){ // Caccia al tesoro conclusa
        document.getElementById("getLocationButton").style.display = "none";
        document.getElementById("nextStepButton").style.display = "none";
        document.getElementById("distanceMessage").style.display = "none";
        document.getElementById("hintMessage").style.display = "none";
        document.getElementById("okMessage").style.display = "none";
        document.getElementById("endMessage").style.display = "block";
        document.getElementById("infoButton").style.display = "none";
    } else { // Caccia al tesoro in corso
        document.getElementById("getLocationButton").style.display = "block";
        document.getElementById("hintMessage").style.display = "block";
        document.getElementById("distanceMessage").style.display = "none";
        document.getElementById("okMessage").style.display = "none";
        document.getElementById("nextStepButton").style.display = "none";
        document.getElementById("infoButton").style.display = "none";
        document.getElementById("hintMessage").innerHTML = targetPositions[targetIndex].hintMessage;
    }
}


var attemps = 0;
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(checkPosition);
    } else {
        alert("Geolocation is not supported by this browser");
    }
}


function skipToNextLocation(){
    var result = confirm("Vuoi saltare la tappa?");
    if (result) {
        attemps = 0;
        document.getElementById("okMessage").innerHTML = "Tappa non correttamente raggiunta";
        document.getElementById("getLocationButton").style.display = "none";
        document.getElementById("hintMessage").style.display = "none";
        document.getElementById("nextStepButton").style.display = "none";
        document.getElementById("distanceMessage").style.display = "none";
        document.getElementById("okMessage").style.display = "block";
        document.getElementById("nextStepButton").style.display = "block";
        document.getElementById("skipToNextStepButton").style.display = "none";
        document.getElementById("infoButton").style.display = "block";
    }
}

function info(){
    alert(targetPositions[targetIndex].info)
}


function checkPosition(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var target = targetPositions[targetIndex];
    var targetRadius = 20; // Raggio in metri
    // Calcola la distanza tra la posizione corrente e la posizione di destinazione
    var distance = calculateDistance(latitude, longitude, target.latitude, target.longitude);
    // Se la distanza è inferiore al raggio, passa alla prossima posizione di destinazione
    if (distance < targetRadius) {
        attemps = 0;
        document.getElementById("okMessage").innerHTML = "Congratulazioni hai raggiunto la posizione corretta!";
        document.getElementById("getLocationButton").style.display = "none";
        document.getElementById("hintMessage").style.display = "none";
        document.getElementById("nextStepButton").style.display = "none";
        document.getElementById("distanceMessage").style.display = "none";
        document.getElementById("okMessage").style.display = "block";
        document.getElementById("nextStepButton").style.display = "block";
        document.getElementById("skipToNextStepButton").style.display = "none";
        document.getElementById("infoButton").style.display = "block";
    } else {
        attemps += 1;
        if (attemps >= 1){
            document.getElementById("skipToNextStepButton").style.display = "block";
        } 
        document.getElementById("distanceMessage").innerHTML = "Sei troppo lontano. Ti mancano ancora "+distance+" metri";
        document.getElementById("distanceMessage").style.display = "block";
        
    }
}


// Calcola la distanza tra due coordinate geografiche utilizzando la formula di Haversine
function calculateDistance(lat1, lon1, lat2, lon2) {
    var R = 6371; // Raggio medio della Terra in km
    var dLat = deg2rad(lat2 - lat1);
    var dLon = deg2rad(lon2 - lon1);
    var a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var d = R * c; // Distanza in km
    var distanceMeters = d * 1000; // Converti in metri
    return Math.round(distanceMeters);
}


// Converte gradi in radianti
function deg2rad(deg) {
    return deg * (Math.PI / 180);
}
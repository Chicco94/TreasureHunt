var targetPositions = [
    { latitude: 44.060644, longitude: 12.565954, hintMessage:"Inizia la tua avventura nella piazza principale di Rimini, dove c'è una fontana adornata da una statua. Cerca sotto il suo sguardo vigile per il primo indizio!" , info:"testo di prova1"},
    { latitude: 44.056981, longitude: 12.571071, hintMessage:"Il passato romano di Rimini si riflette in questo maestoso arco. Guarda da vicino le sue decorazioni per trovare la prossima direzione da prendere" , info:"testo di prova2" },
    { latitude: 44.067290, longitude: 12.581946, hintMessage:"Dirigiti verso il luccichio del sole sull'acqua e troverai la prossima tappa, dove il suono delle onde si mescola con il richiamo dei gabbiani" , info:"testo di prova3"},
    { latitude: 44.077141, longitude: 12.575021, hintMessage:"Da qui puoi avere una vista mozzafiato sulla città e sul mare. Osserva attentamente il panorama e troverai l'indizio che ti guiderà al prossimo traguardo della tua avventura" , info:"testo di prova"},
    { latitude: 44.081782, longitude: 12.576638, hintMessage:"Dirigiti lungo il porto di Rimini, dove la storia e la cultura si mescolano con l'atmosfera marinaresca. Cerca tra le imbarcazioni e gli edifici colorati per trovar del marinaio la sposa" , info:"testo di prova"},
    { latitude: 44.059817, longitude: 12.564048, hintMessage:"La fortezza medievale ti proteggerà dal caldo sole estivo mentre ti svela il segreto della prossima tappa. Guarda attentamente le mura per trovare la prossima tappa del tuo viaggio" , info:"testo di prova"},
    { latitude: 44.059952, longitude: 12.569947, hintMessage:"La bellezza gotica di questo edificio ti svelerà il prossimo passo. C'è un dettaglio nascosto che ti guiderà alla tua destinazione successiva" , info:"testo di prova"},
    { latitude: 44.060221, longitude: 12.575327, hintMessage:"Immergiti nell'antica grandezza dell'antica Roma, dove una volta echeggiavano i suoni dei combattimenti gladiatori" , info:"testo di prova"},
    { latitude: 44.059247, longitude: 12.568537, hintMessage:"Nel cuore del centro storico, troverai una piazza che racconta storie di coraggio. Cerca tra i suoi monumenti per il tesoro che cerchi" , info:"testo di prova"},
    { latitude: 44.062064, longitude: 12.567580, hintMessage:"Esplora le antiche mura del medico più famoso di Rimini, dove i segreti della medicina romana sono stati conservati" , info:"testo di prova"},
    { latitude: 44.063674, longitude: 12.563827, hintMessage:"Via verso il maestoso Ponte, un simbolo dell'antica ingegneria romana che si erge fiero sul fiume Marecchia" , info:"testo di prova"},
    { latitude: 44.064979, longitude: 12.565711, hintMessage:"Attraversa il fiume Marecchia e immergiti nell'atmosfera unica di questo borgo. Tra i colorati murales e le stradine acciottolate, troverai l'ultimo indizio!" , info:"testo di prova"},
    { latitude: 44.064965, longitude: 12.561880, hintMessage:"Ora via dove la pancia incontra il mare...si va a mangiare!!", info:"testo di prova" }
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
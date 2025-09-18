function getLocation() {
	console.log("Getting location...");
    if (navigator.geolocation) {
		console.log("Geolocation is supported by this browser.");
		// Mostra la clessidra o barra di caricamento
		//document.getElementById("loadingSpinner").style.display = "block";

		navigator.geolocation.getCurrentPosition(
			function(position) {
				// Nasconde la clessidra o barra di caricamento
				//document.getElementById("loadingSpinner").style.display = "none";
				checkPosition(position);
			},
			function(error) {
				//document.getElementById("loadingSpinner").style.display = "none";
				console.error(error);
				alert("Errore nel recupero della posizione. Assicurati di aver abilitato la condivisione della posizione.");
				document.getElementById("skipToNextStepButton").style.display = "block";
			}
		);
    } else {
        alert("Geolocation is not supported by this browser");
    }
}



function checkPosition(position) {
	console.log("Checking position...");
	fetch('/check-position', {
	  method: 'POST',
	  headers: {
		'Content-Type': 'application/json',
	  },
	  body: JSON.stringify({latitude: position.coords.latitude, longitude: position.coords.longitude})
	})
	.then(response => response.json())
	.then(data => {
			distance = data.distance_calculated;
			reached = data.reached;
			if (!reached){
				document.getElementById("distanceMessage").innerHTML = data.message;
				document.getElementById("distanceMessage").style.display = "block";
				document.getElementById("skipToNextStepButton").style.display = "block";
			} else {
				document.getElementById("distanceMessage").style.display = "none";
				alert(data.message);
				nextLocation();
			}
		}
	);
}



function setSelectedHunt(selected_hunt_id) {
	fetch('/set-selected-hunt', {
	  method: 'POST',
	  headers: {
		'Content-Type': 'application/json',
	  },
	  body: JSON.stringify({id: selected_hunt_id})
	})
	.then(response => response.json())
}



function sleep(time) {
	return new Promise(resolve => setTimeout(resolve, time));
}



function skipToNextLocation(){
    var result = window.confirm("Vuoi saltare la tappa?");
    if (result) {
        window.location.href = "tappa_raggiunta";
    }
}



function nextLocation() {
	fetch('/next-position', {
	  method: 'POST',
	  headers: {
		'Content-Type': 'application/json',
	  },
	  body: JSON.stringify({})
	})
	.then(response => response.json())
	.then(data => {
            if (data.ended){
                window.location.href = "fine";
            } else {
                window.location.href = "tappa";
            }
		}
	);
}
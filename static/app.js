function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(checkPosition);
    } else {
        alert("Geolocation is not supported by this browser");
    }
}

function checkPosition(position) {
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
			document.getElementById("distanceMessage").innerHTML = data.message;
			document.getElementById("distanceMessage").style.display = "block";
			if (!reached){
				document.getElementById("skipToNextStepButton").style.display = "block";
			}
		}
	);
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
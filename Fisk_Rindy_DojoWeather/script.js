
var popup = document.querySelector(".cookiePopup");


function loading_report() {
    alert("Loading weather report...")
}

function accept() {
    popup.remove();
}

function celsiusToFahrenheit(temp) {
    return Math.round(9 / 5 * temp + 32);
}

function fahrenheitToCelsius(temp) {
    return Math.round(5 / 9 * (temp - 32));
}

function temp_select (element) {
    console.log(element.value);
    for(var i=1; i<9; i++) {
        var tempSpan = document.querySelector("#temp" + i); 
        var tempChange = parseInt(tempSpan.innerText);
        if(element.value == "°C") {
            tempSpan.innerText = fahrenheitToCelsius(tempChange);
        } else{
            tempSpan.innerText = celsiusToFahrenheit(tempChange);
        }
    }
}


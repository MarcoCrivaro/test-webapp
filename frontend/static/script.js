function turnOn(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/api/turnOn", true);
    xhttp.send();
}
function turnOff(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/api/turnOff", true);
    xhttp.send();
}
function toggle(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/api/toggle", true);
    xhttp.send();
}
function onPageLoadGetDashboardAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);

            document.getElementById("avg_temperature").innerHTML = dataObj.temperature_sensor;
            document.getElementById("avg_pressure").innerHTML = dataObj.pressure_sensor;
            document.getElementById("avg_co2").innerHTML = dataObj.CO2_sensor;
            document.getElementById("avg_tvoc").innerHTML = dataObj.TVOC_Sensor;
            document.getElementById("avg_humidity").innerHTML = dataObj.humidity_sensor;
        }
    }
    xhttp.open("GET","api/dashboard", true);
    xhttp.send();
}

onPageLoadGetDashboardAPI();

function onLogoutClick() {
    window.location.href = "{% url 'logout_page' %}";
}

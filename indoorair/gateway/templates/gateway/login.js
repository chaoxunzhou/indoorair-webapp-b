function onLoginClick() {
    const password = document.getElementById("password").value;
    const username = document.getElementById("username").value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
            // Get the string data that the server sent us.
            const resultString = this.responseText;

            // Create an object which converts the string to an object using JSON parsing.
            var resultObject = JSON.parse(resultString);

            // Please note, "was_logged_in" is a key set by the server.
            if (resultObject.was_logged_in === false) {
                alert(resultObject.reason);
            } else {
                window.location.href = "/dashboard";
            }
        }
    }

    xhttp.open("POST", "{% url 'login_api' %}", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send("username="+username+"&password="+password);
}

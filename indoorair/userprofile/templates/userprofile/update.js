function generateViewFromObject(dataObj) {
    if (dataObj.was_found === false) {
        alert("Sorry we could not find that instrument!");
        onBackClick();
    } else {
        var firstNameInputElement = document.getElementById("first_name");
        firstNameInputElement.value = dataObj.first_name;
        var lastNameInputElement = document.getElementById("last_name");
        lastNameInputElement.value = dataObj.last_name;
        var emailInputElement = document.getElementById("email");
        emailInputElement.value = dataObj.email;
        var usernameInputElement = document.getElementById("username");
        usernameInputElement.value = dataObj.username;
    }
}

function onPageLoadRunGetProfileFromAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);
            generateViewFromObject(dataObj);
        }
    }
    const detailURL = "/api/profile";
    console.log(detailURL);
    xhttp.open("GET", detailURL, true);
    xhttp.send();
}

onPageLoadRunGetProfileFromAPI();


function onBackClick() {
    window.location.href = "{% url 'profile_retrieve_page' %}";
}

function onSubmitClick() {
    window.location.href = "";
}

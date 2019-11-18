function generateViewFromObject() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const dataString = this.responseText;
        const dataObj = JSON.parse(dataString);
            document.getElementById("first_name").value = dataObj.first_name
            document.getElementById("last_name").value = dataObj.last_name
            document.getElementById("email").value = dataObj.email
            document.getElementById("username").value = dataObj.username
        }else{
          alert("Sorry we could not find that instrument!");
          onBackClick();
      }
      const detailURL = "/api/profile";
      console.log(detailURL);
      xhttp.open("GET", detailURL, true);
      xhttp.send();
}


generateViewFromObject();


function onBackClick() {
    window.location.href = "{% url 'profile_retrieve_page' %}";
}

function onSubmitClick() {
    window.location.href = "";
}

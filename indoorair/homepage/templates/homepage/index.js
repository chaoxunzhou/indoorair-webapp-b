
  function onLoginClick(){
    window.location.href = "/login";
  }
  function onRegisterClick(){
    window.location.href = "/register";
  }

  function onContactClick(){
    window.location.href = "{% url 'contact' %}";
  }

  function onVersionClick() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const dataString = this.responseText
        const dataObj = JSON.parse(dataString)
        document.getElementById('getVersion').innerHTML = dataObj.version;
      }
    };
    xhttp.open('GET', "/api/version", true);
    xhttp.send();
}

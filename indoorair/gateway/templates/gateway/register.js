function onRegisterClick(){
  const firstName = document.getElementById('first_name').value;
  const lastName = document.getElementById('last_name').value;
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

var xhttp = new XMLHttpRequest()
  xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200){
      const resultString = this.responseText;
      var resultObject = JSON.parse(resultString)
      if(resultObject.was_registered === false){
        alert(resultObject.reason);
      }else{
      window.location.href = "{% url 'register_ok_page' %}";
      }
    }
};
xhttp.open('POST', 'api/register', true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("first_name="+firstName+"&last_name="+lastName+"&password="+password+"&username="+username+"&email="+email);
}

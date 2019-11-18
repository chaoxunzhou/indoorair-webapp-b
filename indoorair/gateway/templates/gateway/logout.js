function onPageLoadRunPostLogoutFromApi(){

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
      const loginObject = JSON.parse(this.responseText);
      if(loginObject.was_successful === ture){
        window.location.href = "{% url 'login_page' %}";
      }else{
        alert(loginObject.reason)
      }
    }
  }
  xhttp.open("POST","api/logout", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  const string = "username=" + username+"&password=" +password
  xhttp.send(string)
}


onPageLoadRunPostLogoutFromApi()

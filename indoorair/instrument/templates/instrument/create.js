function onCreateClick(){
    const createInsrtument = document.getElementById('create_instrument').value;

    var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        document.getElementById("create").innerHTML = this.responseText;
       }
     };
  xhttp.open('POST', '/instrument/create/api', true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("create_instrument="+createInsrtument);
  }

console.log("page loaded...");

//friend requests
var request_count = document.querySelector("#requests");

//friends list
var connection_count = document.querySelector("#connections");

//changes the profile name
var username = document.querySelector("#username");


  // Re connection Requsts - Accept

function accept(id) {
    var element = document.querySelector(id);
    element.remove();
    request_count.innerText--;
    connection_count.innerText++;
}


  //Re connection Requests - Ignore

function ignore(id) {
    var element = document.querySelector(id);
    element.remove();
    request_count.innerText--;
}

//name change function

function edit() {
    username.innerText = "Rindy Loo & Tigger Too!!";
}
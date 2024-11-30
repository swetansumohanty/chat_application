const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ac/'
    + id
    + '/'
);

socket.onopen = function(event){
    console.log("connection open ...");
    console.log(id);
    console.log(message_username);
}

socket.onmessage = function(event){
    console.log('message from server',event);
    console.log('message from server',event.data);
    const data = JSON.parse(event.data)
    console.log(data,typeof(data))
    console.log(data.message)
    console.log(data.username)
    document.querySelector("#chat-body").value += ('['+
        data.username +']:'+ data.message+'\n'
        )
}

socket.onclose = function(event){
    console.log("connection lost ...");
}

socket.onerror = function(event){
    console.log("ERROR OCCURED");
}


document.getElementById("chat-message-submit").onclick = 
function(event){
    const messgeInputDom = document.getElementById("input-message")
    const message = messgeInputDom.value
    socket.send(JSON.stringify({
        "message":message,
        "username":message_username
    }))
    messgeInputDom.value = ''
}
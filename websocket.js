const socket = new WebSocket('ws://localhost:8765');

// Connection opened event handler
socket.addEventListener('open', function (event) {
    console.log('WebSocket connected');
    
    // Send a message to the server
    socket.send('Hello Server!');
});

// Message from server event handler
socket.addEventListener('message', function (event) {
    console.log('Message from server:', event.data);
});

// Error event handler
socket.addEventListener('error', function (event) {
    console.error('WebSocket error:', event);
});

// Close event handler
socket.addEventListener('close', function (event) {
    console.log('WebSocket closed');
});

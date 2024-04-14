document.addEventListener('DOMContentLoaded', function() {
    const inputBox = document.getElementById('userInput');
    const chatbox = document.getElementById('chatbox');

    document.getElementById('userInput').addEventListener('keypress', function(event) {
        if (event.keyCode === 13) {  // Enter key code
            event.preventDefault();  // Prevent form submission
            if (this.value.trim() !== '') {  // Check for non-empty input
                sendMessage();
            }
        }
    });

    function sendMessage() {
        const message = inputBox.value;
        inputBox.value = '';  // Clear the input box

        // Append user message with distinct styling
        const userMessage = document.createElement('div');
        userMessage.textContent = 'User: ' + message;
        userMessage.style.color = 'blue'; // Change color for user messages
        userMessage.style.margin = '5px 0'; // Add margin
        chatbox.appendChild(userMessage);

        fetch('/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({message: message})
        }).then(response => response.json())
          .then(data => {
              // Append bot response with distinct styling
              const botMessage = document.createElement('div');
              botMessage.textContent = 'Bot: ' + data.message;
              botMessage.style.color = 'green'; // Change color for bot messages
              botMessage.style.margin = '5px 0'; // Add margin
              chatbox.appendChild(botMessage);

              // Autoscroll to the latest message
              chatbox.scrollTop = chatbox.scrollHeight;
          }).catch(error => console.error('Error:', error));
    }
});

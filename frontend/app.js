document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const typingIndicator = document.getElementById('typing-indicator');

    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'system-message'}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        // Very basic markdown handling for bold and line breaks
        let formattedContent = content
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
            
        contentDiv.innerHTML = formattedContent;
        messageDiv.appendChild(contentDiv);
        
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function sendQueryToAPI(query) {
        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: query })
            });

            if (!response.ok) {
                throw new Error(`API error: ${response.status}`);
            }

            const data = await response.json();
            
            // The RAG agent usually returns a dict with 'result' or just the text
            // Let's handle different possible return structures
            let answerText = "Sorry, I couldn't understand the response.";
            if (typeof data === 'string') {
                answerText = data;
            } else if (data.result) {
                answerText = data.result;
            } else if (data.answer) {
                answerText = data.answer;
            } else if (typeof data === 'object') {
                // If it's a dict but doesn't have result/answer
                answerText = JSON.stringify(data);
            }
            
            return answerText;
            
        } catch (error) {
            console.error('Error fetching data:', error);
            return `Error communicating with BookBrain: ${error.message}`;
        }
    }

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const query = userInput.value.trim();
        if (!query) return;

        // Add user message
        addMessage(query, true);
        
        // Clear input and show typing indicator
        userInput.value = '';
        typingIndicator.style.display = 'flex';
        scrollToBottom();

        // Disable input while waiting
        userInput.disabled = true;
        
        // Fetch response
        const responseText = await sendQueryToAPI(query);
        
        // Hide typing indicator and enable input
        typingIndicator.style.display = 'none';
        userInput.disabled = false;
        userInput.focus();
        
        // Add bot message
        addMessage(responseText, false);
    });
});

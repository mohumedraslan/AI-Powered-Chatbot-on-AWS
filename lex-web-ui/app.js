// AWS Lex configuration
AWS.config.region = 'us-east-1';
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
  IdentityPoolId: 'us-east-1:d10f332b-8132-4292-a419-7c82b6aec22a',
});

const lexruntimev2 = new AWS.LexRuntimeV2();

const botId = 'UFU0FKTC4D';
const botAliasId = 'TSTALIASID';
const localeId = 'en_US';
const sessionId = Date.now().toString();

function addMessage(text, sender) {
  const chat = document.getElementById('chat');
  const bubble = document.createElement('div');
  bubble.className = `bubble ${sender}`;
  bubble.textContent = text;
  chat.appendChild(bubble);
  chat.scrollTop = chat.scrollHeight;
}

function sendMessage() {
  const input = document.getElementById('message');
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, 'user');
  input.value = '';

  const params = {
    botId,
    botAliasId,
    localeId,
    sessionId,
    text: message
  };

  lexruntimev2.recognizeText(params, (err, data) => {
    if (err) {
      console.error(err);
      addMessage("Error: " + err.message, 'bot');
    } else {
      const messages = data.messages || [];
      messages.forEach(m => addMessage(m.content, 'bot'));
    }
  });
}

// Enable sending with Enter key
window.onload = function () {
  const input = document.getElementById('message');
  input.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      sendMessage();
    }
  });
};

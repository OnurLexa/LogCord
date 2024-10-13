// LOGCORD AMA JAVASCRIPT VERSIYONU


const fetch = require('node-fetch');

const webhookURL = 'WEBHOOK_BURAYA';

function sendLogMessage(message) {
	const payload = {
		content: message,
		username: 'Logger', // gönderici adıdır, istedeginiz gibi değiştirebilirsiniz
	};

	fetch (webhookURL, {
		method: 'POST',,
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(payload),
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('webhook gönderiminde sorun olustu.');
		}
		console.log('mesaj gönderildi', message),
	})
	.catch(error => {
		console.error('hata:', error);
	});
}


// 2. KISIM

const https = require('https');

const webhookUrl = 'WEBHOOK_BURAYA';
const webhookOptions = {
  method: ' POST',
  headers: {
    'Content-Type': 'application/json'
  }
};

function sendWebhookMessage(message) {
  const payload = JSON.stringify({ content: message });
  const req = https.request(webhookUrl, webhookOptions, (res) => {
    let data = '';
    res.on('data', (chunk) => {
      data += chunk;
    });
    res.on('end', () => {
      console.log(`Sent message to Discord Webhook: ${message}`);
    });
  });
  req.write(payload);
  req.end();
}

sendWebhookMessage('ONUR LEXA!');

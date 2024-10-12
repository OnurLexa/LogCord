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

sendLogMessage('bu bir test log mesajıdır.');

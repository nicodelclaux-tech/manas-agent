const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        handleSIGINT: false
    }
});

client.on('qr', (qr) => {
    console.log('SCAN THIS QR CODE WITH WHATSAPP:');
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Manas Agent Bridge is ready!');
});

client.on('message', async msg => {
    if (msg.hasMedia) {
        console.log('Received media from:', msg.from);
    }
});

client.initialize();

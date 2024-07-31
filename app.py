from flask import Flask, render_template, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Ambil kredensial Twilio dari variabel lingkungan
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/')
def index():
    balance = client.api.v2010.accounts(TWILIO_ACCOUNT_SID).fetch().balance
    return render_template('index.html', balance=balance)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    target_number = request.form['target_number']
    message_body = request.form['message_body']
    
    result = {'status': 'GAGAL', 'info': 'GAGAL'}
    if target_number.startswith('62') and len(target_number) == 12:
        try:
            message = client.messages.create(
                body=message_body,
                from_='+1234567890',  # Ganti dengan nomor Twilio Anda
                to=target_number
            )
            result = {'status': 'BERHASIL', 'info': 'BERHASIL'}
        except Exception as e:
            result['info'] = 'GAGAL'
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

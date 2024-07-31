from flask import Flask, request, render_template
from twilio.rest import Client
import os

app = Flask(__name__)

# Ambil kredensial Twilio dari variabel lingkungan
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/')
def index():
    balance = client.api.v2010.accounts(TWILIO_ACCOUNT_SID).fetch().balance
    return render_template('index.html', balance=balance)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    numbers = request.form['numbers'].split(',')
    message_body = request.form['message']
    results = []

    for number in numbers:
        number = number.strip()
        try:
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=number
            )
            results.append({'number': number, 'status': 'VALID', 'info': 'BERHASIL'})
        except Exception as e:
            results.append({'number': number, 'status': 'TIDAK VALID', 'info': 'GAGAL'})

    return render_template('index.html', balance=client.api.v2010.accounts(TWILIO_ACCOUNT_SID).fetch().balance, results=results)

if __name__ == '__main__':
    app.run(debug=True)

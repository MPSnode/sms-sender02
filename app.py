from flask import Flask, render_template, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    account_sid = request.json.get('account_sid')
    auth_token = request.json.get('auth_token')
    client = Client(account_sid, auth_token)
    
    try:
        balance = client.api.v2010.accounts(account_sid).balance.fetch()
        info = {
            "balance": balance.balance,
            "currency": balance.currency,
            "account_sid": account_sid,
            "auth_token": auth_token
        }
        return jsonify(info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/send_sms', methods=['POST'])
def send_sms():
    account_sid = request.json.get('account_sid')
    auth_token = request.json.get('auth_token')
    to_numbers = request.json.get('to_numbers')
    message_body = request.json.get('message_body')
    
    client = Client(account_sid, auth_token)
    results = []
    
    for number in to_numbers:
        try:
            message = client.messages.create(
                to=number,
                from_="Your Twilio Number",  # Replace with your Twilio number
                body=message_body
            )
            results.append({
                "number": number,
                "status": "VALID",
                "message": "BERHASIL"
            })
        except Exception as e:
            results.append({
                "number": number,
                "status": "TIDAK VALID",
                "message": "GAGAL"
            })
    
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const account_sid = document.getElementById('account_sid').value;
    const auth_token = document.getElementById('auth_token').value;
    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ account_sid, auth_token })
    }).then(response => response.json()).then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('info-section').style.display = 'block';
            document.getElementById('balance').textContent = data.balance;
            document.getElementById('currency').textContent = data.currency;
            document.getElementById('account_sid').value = data.account_sid;
            document.getElementById('auth_token').value = data.auth_token;
        }
    });
});

document.getElementById('sms-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const account_sid = document.getElementById('account_sid').value;
    const auth_token = document.getElementById('auth_token').value;
    const message_body = document.getElementById('message_body').value;
    const to_numbers = document.getElementById('to_numbers').value.split(',');

    fetch('/send_sms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ account_sid, auth_token, message_body, to_numbers })
    }).then(response => response.json()).then(data => {
        const output = document.getElementById('output');
        output.innerHTML = '';
        data.forEach(result => {
            const div = document.createElement('div');
            div.className = result.status === 'VALID' ? 'success' : 'error';
            div.textContent = `Nomor: ${result.number} - ${result.status} - ${result.message}`;
            output.appendChild(div);
        });
    });
});
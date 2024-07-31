document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('smsForm');
    const resultsContainer = document.getElementById('results');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        // Clear previous results
        resultsContainer.innerHTML = '';

        const numbers = document.getElementById('numbers').value.split(',').map(num => num.trim());
        const message = document.getElementById('message').value;

        numbers.forEach(number => {
            // Simulate sending SMS and getting result
            const resultItem = document.createElement('li');
            if (isValidNumber(number)) {
                resultItem.className = 'VALID';
                resultItem.innerHTML = `Nomor Target: ${number} - VALID<br>Info: BERHASIL`;
            } else {
                resultItem.className = 'TIDAK VALID';
                resultItem.innerHTML = `Nomor Target: ${number} - TIDAK VALID<br>Info: GAGAL`;
            }
            resultsContainer.appendChild(resultItem);
        });
    });

    function isValidNumber(number) {
        // Simple validation logic, you can adjust it
        return /^(\+62|0)8[1-9][0-9]{7,11}$/.test(number);
    }
});

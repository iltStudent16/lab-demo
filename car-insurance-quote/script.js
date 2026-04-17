document.getElementById('quoteForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const age = document.getElementById('age').value;
    const car_model = document.getElementById('car_model').value;
    const driving_history = document.getElementById('driving_history').value;
    const response = await fetch('/api/quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ age: Number(age), car_model, driving_history })
    });
    const data = await response.json();
    document.getElementById('result').textContent = 'Your quote: $' + data.quote;
});

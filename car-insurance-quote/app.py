from flask import Flask, request, jsonify
from quote_logic import calculate_quote

app = Flask(__name__)

@app.route('/api/quote', methods=['POST'])
def get_quote():
    data = request.json
    age = data.get('age')
    car_model = data.get('car_model')
    driving_history = data.get('driving_history')
    quote = calculate_quote(age, car_model, driving_history)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)

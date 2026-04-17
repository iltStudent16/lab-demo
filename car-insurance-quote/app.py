from flask import Flask, request, jsonify, send_from_directory
from quote_logic import calculate_quote

import os

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Serve static files (js, css, etc.)
    if os.path.exists(path):
        return send_from_directory('.', path)
    return 'Not Found', 404

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

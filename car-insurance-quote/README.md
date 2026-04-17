
# Car Insurance Quote

A simple web application built with Flask that calculates car insurance quotes based on user input.

## Features
- User-friendly web form for quote requests
- Real-time quote calculation via REST API
- Clean, responsive frontend

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Setup
1. Clone the repository and navigate to the project directory:
   ```sh
   git clone <repo-url>
   cd car-insurance-quote
   ```
2. (Optional but recommended) Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. Fill out the form and submit to get your insurance quote.

## API
- **POST** `/api/quote` — Accepts JSON with `age`, `car_model`, and `driving_history` fields. Returns a JSON object with the calculated quote.

## Project Structure
- `app.py` — Flask backend
- `index.html` — Main frontend page
- `script.js` — Handles form submission and API calls
- `style.css` — Styles for the frontend
- `quote_logic.py` — Quote calculation logic

## License
MIT

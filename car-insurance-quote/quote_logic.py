def calculate_quote(age, car_model, driving_history):
    base = 500
    if age < 25:
        base += 200
    if car_model.lower() in ['sports', 'luxury']:
        base += 300
    if driving_history.lower() == 'bad':
        base += 400
    elif driving_history.lower() == 'average':
        base += 100
    return base

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    
    # User Information
    user_id = 'rahul_kumar_21122002'
    email = 'rahulkumar2112k@gmail.com'
    roll_number = '22BCS50181'
    
    # Validate Input
    if 'data' not in data or not isinstance(data['data'], list):
        return jsonify({'is_success': False, 'message': 'Invalid input'}), 400

    # Separate Numbers and Alphabets
    numbers = [item for item in data['data'] if item.isdigit()]
    alphabets = [item for item in data['data'] if item.isalpha()]
    
    # Highest Alphabet Calculation
    highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []

    # API Response
    response = {
        'is_success': True,
        'user_id': user_id,
        'email': email,
        'roll_number': roll_number,
        'numbers': numbers,
        'alphabets': alphabets,
        'highest_alphabet': highest_alphabet
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({'operation_code': 1})

if __name__ == '__main__':
    app.run(debug=True)

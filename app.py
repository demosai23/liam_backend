from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '').strip().lower()

    responses = {
        'hi': 'hello!',
        'hello': 'hi there!',
        'how are you': 'I’m just a bot, but I’m doing fine!',
        'what is your name': 'I’m your friendly Flask bot.',
        'bye': 'Goodbye! Have a great day!',
    }

    # Default fallback if input is unknown
    default_response = "I'm not sure how to respond to that yet."

    # Look for exact match in known responses
    response = responses.get(user_input, default_response)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

    



 
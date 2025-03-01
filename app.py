from flask import Flask, request, jsonify
from flask_cors import CORS
from langchained import get_groq_response

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['Post'])

def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "The 'message' field is required."}), 400
    
    response = get_groq_response(user_input)
    return jsonify({"response": response})



if __name__ == '__main__':
    app.run(port=5000)
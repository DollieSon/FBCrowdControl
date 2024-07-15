from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app,resources={r"/data": {"origins": "https://www.facebook.com"}})
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(f"Received data: {data}")
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(debug=True,port=5210)
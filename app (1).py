from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # تفعيل CORS لجميع الطلبات

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "server_url": "https://loginbp.ggpolarbear.com",
        "latest_release_version": "OB53"
    })

@app.route('/api', methods=['GET'])
def api_endpoint():
    return jsonify({
        "server_url": "https://loginbp.ggpolarbear.com",
        "latest_release_version": "OB53"
    })

# لدعم مسار /api/index
@app.route('/api/index', methods=['GET'])
def api_index():
    return jsonify({
        "server_url": "https://loginbp.ggpolarbear.com",
        "latest_release_version": "OB53"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
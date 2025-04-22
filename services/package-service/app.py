from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

@app.route('/package/<id>')
def get_package(id):
    return jsonify({
        "package_id": id,
        "status": "In Transit",
        "eta": "2 hours"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "message": "Minimalist ML model deployment",
    }), 200

app.run()

@app.route("/models", methods=["GET"])
def get_models():
    return jsonify({
        "models": ["Model 1", "Model 2"]
    }), 200
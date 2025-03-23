from flask import Flask, request, jsonify
from blockchain import Blockchain
from ai_model import AIModel

app = Flask(__name__)
blockchain = Blockchain()
ai = AIModel()

@app.route("/predict", methods=["POST"])
def predict_and_store():
    data = request.json
    if "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    
    # Get AI prediction
    prediction = ai.predict(data["text"])
    
    # Add to blockchain
    block = blockchain.add_block(prediction)
    
    return jsonify({
        "message": "Prediction stored",
        "block_index": block.index,
        "data": block.data,
        "hash": block.hash
    })

@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = [{"index": b.index, "data": b.data, "hash": b.hash} for b in blockchain.chain]
    return jsonify({"chain": chain_data, "valid": blockchain.is_chain_valid()})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
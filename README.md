# AI Blockchain Project
A simple project combining AI and blockchain. Uses a pre-trained sentiment model to make predictions and stores them in a basic blockchain.

## Setup
1. Install Python 3.9+
2. Clone this repo
3. Create and activate a virtual env: `python -m venv venv` then `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install deps: `pip install -r requirements.txt`
5. Run: `python app.py`

## Usage
- POST to `/predict` with JSON like `{"text": "This is awesome!"}`
- GET `/chain` to see the blockchain


## Example
### Example-1
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"This is awesome!"}' http://localhost:5000/predict
{
  "block_index": 2, 
  "data": "Prediction: POSITIVE (confidence: 1.00)", 
  "hash": "afeebf7d3e26a9ebe629b46ad02f906f5774f91704867dbe90e9f9aea089a630", 
  "message": "Prediction stored"
}
```
### Example-2
```
curl http://localhost:5000/chain
{
  "chain": [
    {
      "data": "Genesis Block", 
      "hash": "e92f41ef0874c4e2f82d78b6cab921bb5fee1601c38ab4dbcfd21c8189b7d44f", 
      "index": 0
    }, 
    {
      "data": "Prediction: POSITIVE (confidence: 1.00)", 
      "hash": "a06a865b1dc9befd784f79be7832da727537c73d3ac02658765a0b4156abfa49", 
      "index": 1
    }, 
    {
      "data": "Prediction: POSITIVE (confidence: 1.00)", 
      "hash": "afeebf7d3e26a9ebe629b46ad02f906f5774f91704867dbe90e9f9aea089a630", 
      "index": 2
    }
  ], 
  "valid": true
}
```
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

curl -X POST -H "Content-Type: application/json" -d '{"text":"This is badddd!"}' http://localhost:5000/predict
{
  "block_index": 4, 
  "data": "Prediction: NEGATIVE (confidence: 1.00)", 
  "hash": "43b34c2ebf103fa6e5d58748d1831f4f0e84559a17e4585b81cd771c7305e258", 
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
      "hash": "5711534b2cf297d77e8e27dd719ffa75ae047e17ecfdc88c7fb008fe93d122dc", 
      "index": 0
    }, 
    {
      "data": "Prediction: POSITIVE (confidence: 1.00)", 
      "hash": "4a54362cd739768539af636eb306d980f3e6f03188a2e41f8b37b5ff55537a4b", 
      "index": 1
    }, 
    {
      "data": "Prediction: POSITIVE (confidence: 1.00)", 
      "hash": "e25f36bb028680f09303c6f1e7c1514fb5e9030734783ee0054f991c7a56558f", 
      "index": 2
    }, 
    {
      "data": "Prediction: NEGATIVE (confidence: 1.00)", 
      "hash": "81ce4798ef8cfd806024a798b081626daae5ff7e747ac6b1cd0e319800899aec", 
      "index": 3
    }
  ], 
  "valid": true
}
```
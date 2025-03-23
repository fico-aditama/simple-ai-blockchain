from transformers import pipeline

class AIModel:
    def __init__(self):
        # Load a pre-trained sentiment analysis model
        self.model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def predict(self, text):
        # Return prediction as a string
        result = self.model(text)[0]
        return f"Prediction: {result['label']} (confidence: {result['score']:.2f})"

# Test it
if __name__ == "__main__":
    ai = AIModel()
    print(ai.predict("I love this project!"))
    print(ai.predict("This is terrible."))
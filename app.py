from flask import Flask, request, render_template
import pickle

# Load the model and vectorizer
with open('model/spam_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # index.html contains the form for input

# Route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input text from the form
        input_text = request.form['email']
        
        # Transform the input text using the vectorizer
        input_vector = vectorizer.transform([input_text])
        
        # Make the prediction
        prediction = model.predict(input_vector)
        
        # Determine the output
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        
    except Exception as e:
        result = "Error processing the input. Please try again."

    # Pass the result back to the HTML template
    return render_template('index.html', prediction_text=f'This message is: {result}')

if __name__ == "__main__":
    app.run(debug=True)
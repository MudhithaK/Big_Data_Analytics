from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    viewer_rate = float(request.form['viewer_rate'])
    
    # Dummy example prediction  
    prediction = viewer_rate * 10000  

    return f"Predicted Views: {prediction}"

if __name__ == '__main__':
    app.run(debug=True)

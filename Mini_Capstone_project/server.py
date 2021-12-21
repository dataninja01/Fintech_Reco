import numpy as np
import joblib
from flask import Flask, request, render_template, jsonify

# instantiate Flask app
app = Flask(__name__)

# load model w metadata
model = joblib.load("models/pipe_clf_checkpoint.joblib")
model_clf = model['pipeline']

# route post requests
@app.route('/')
def my_form():
    return render_template('form.html')

@app.route("/", methods = ["POST"])
def predict_sentiment():
    # pass requests to model
    data = request.get_json(force=True)
    preds = model_clf.predict(data['input'])
    
    # predict class values vs labels
    if data['predict classes'] == "True":
        predictions = [model['class labels'][key] for key in preds]
    else:
        predictions = preds
    
    # store responses
    response = []
    for x, pred in zip(data['input'], predictions):
        response.append("Text: "+str(x)+" | class: "+str(pred))
    
    return render_template(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

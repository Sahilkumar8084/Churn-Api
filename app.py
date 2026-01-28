from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__) #app object banata hai ye


bundle = joblib.load('gb1.pkl')
model = bundle['model']
scaler = bundle['scaler']
Threshold = 0.45
model_columns=bundle['columns']


@app.route('/')
def welcome():
    return ("Welcome to the page of the API")

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    data = request.get_json()
    #Case 1 of conversion of json data to the dataframe
    # usign the df = pd.Json_normalize(data)
    #Case2: of the conversionof the df = pd.DataFrame([data])
    #so for now using these method for now
    
    df = pd.DataFrame([data])
    
    df_scaled = scaler.transform(df)
    
    prediction=model.predict(df_scaled)
    pred_probab = model.predict_proba(df_scaled)[0][1]
    
    
    
    return jsonify(
        {
        
        'Prediction': int(prediction),
        'Probability': round(float(pred_probab),3)
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
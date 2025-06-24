import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app = application



ridge_model = pickle.load(open("models/ridge.pkl","rb"))
scaler = pickle.load(open("models/scaler.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction", methods = ["GET","POST"])
def prediction():
    if request.method == "POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        input_df = pd.DataFrame([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
                        columns=["Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "ISI", "Classes", "Region"])
        new_scaled_data = scaler.transform(input_df)

        result = ridge_model.predict(new_scaled_data)
        return render_template("home.html", result=result[0])
    else:
        return render_template("home.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5000)
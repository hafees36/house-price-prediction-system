from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("models/house_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    stories = int(request.form["stories"])
    mainroad = int(request.form["mainroad"])
    guestroom = int(request.form["guestroom"])
    basement = int(request.form["basement"])
    hotwaterheating = int(request.form["hotwaterheating"])
    airconditioning = int(request.form["airconditioning"])
    parking = int(request.form["parking"])
    prefarea = int(request.form["prefarea"])
    furnishing_semi = int(request.form["furnishing_semi"])
    furnishing_un = int(request.form["furnishing_un"])

    # Create dataframe
    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus_semi-furnished": furnishing_semi,
        "furnishingstatus_unfurnished": furnishing_un
    }])

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=f"₹ {prediction:,.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)
# 🏠 House Price Prediction System

A Machine Learning-powered web application that predicts the estimated price of a house based on various property features. The project uses **Linear Regression** for prediction and **Flask** for the web interface, allowing users to estimate house prices through an intuitive and responsive web application.

---

## 🚀 Features

* Predicts house prices based on user inputs
* Interactive and user-friendly web interface
* Machine Learning model trained using Scikit-learn
* Real-time predictions using Flask
* Responsive design with HTML and CSS
* Easy to deploy on platforms like Render

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3

### Backend

* Flask

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn (Linear Regression)
* Joblib

---

## 📂 Project Structure

```text
house-price-pred-tool/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── Housing.csv
│
├── models/
│   └── house_price_model.pkl   
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## 📊 Dataset

The project is trained using the **Housing.csv** dataset.

### Features Used

* Area (sq.ft)
* Bedrooms
* Bathrooms
* Stories
* Main Road Access
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Parking Spaces
* Location Category (Premium / Normal Area)
* Furnishing Type

### Target

* House Price

---

## 📈 Model Performance

* **Algorithm:** Linear Regression
* **R² Score:** ~0.65 (may vary depending on the dataset split)
* **Evaluation Metric:** Mean Absolute Error (MAE)

---

## 📸 Application Workflow

1. Enter the house details.
2. Click **Predict Price**.
3. The trained machine learning model processes the input.
4. The estimated house price is displayed instantly.

---

## 🔮 Future Improvements

* Random Forest and XGBoost models
* Model comparison dashboard
* Interactive data visualizations
* Prediction history
* Explainable AI (SHAP)
* Location-based predictions using maps
* Improved UI with Bootstrap or Tailwind CSS
* Docker support
* Cloud deployment

---

## 💡 Learning Outcomes

This project demonstrates:

* Data preprocessing
* Feature engineering
* Machine Learning model training
* Model evaluation
* Model serialization with Joblib
* Flask web application development
* Frontend and backend integration
* End-to-end Machine Learning deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is intended for educational and learning purposes.

Just try out my project: https://house-price-prediction-system-38qf.onrender.com

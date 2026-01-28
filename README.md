

# 🔌 Customer Churn Prediction API

<p align="center">
  <img src="https://img.shields.io/badge/Python-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI%20%2F%20Flask-API-success" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Classification-orange" />
  <img src="https://img.shields.io/badge/Deployment-Render-brightgreen" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-live-success" />
  <img src="https://img.shields.io/badge/API-RESTful-blue" />
  <img src="https://img.shields.io/badge/license-educational-lightgrey" />
</p>

---

## 🌐 Live API

🚀 **Deployed API Endpoint**
👉 [https://churn-api-8zci.onrender.com](https://churn-api-8zci.onrender.com)

📁 **GitHub Repository**
👉 [https://github.com/Sahilkumar8084/Churn-Api.git](https://github.com/Sahilkumar8084/Churn-Api.git)

---

## 🧠 Introduction

The **Customer Churn Prediction API** is a **RESTful machine learning API** that predicts whether a customer is likely to **churn** or **stay** based on customer-related attributes.

This API is designed to be **consumed by frontend applications**, dashboards, or other services (such as Streamlit apps), making it ideal for **production-style ML deployment**.

---

## 📌 Project Overview

Customer churn prediction is widely used in:

* 📞 Telecom companies
* 💻 SaaS platforms
* 📦 Subscription-based businesses

This API enables developers to integrate **churn prediction capabilities** into any application via simple HTTP requests.

---

## 🎯 Objective

To build a **scalable, production-ready ML API** that:

* Accepts customer data in JSON format
* Applies the same preprocessing used during training
* Returns accurate churn predictions
* Can be easily integrated with any frontend or service

---

## 🧠 Machine Learning Approach

### 🔹 Problem Type

* **Binary Classification**

  * `0` → Customer Will Stay
  * `1` → Customer Will Churn

### 🔹 Model Used

* **Classification Model** (e.g., Logistic Regression / Tree-based model)

  * Trained on structured customer data
  * Optimized for fast inference
  * Suitable for real-time predictions

---

## 📊 Input Features

| Feature          | Description                       |
| ---------------- | --------------------------------- |
| Age              | Customer age                      |
| Gender           | Male / Female                     |
| Tenure           | Duration of customer relationship |
| Monthly_Charges  | Monthly billing amount            |
| Total_Charges    | Total billed amount               |
| Contract_Type    | Contract duration                 |
| Payment_Method   | Mode of payment                   |
| Internet_Service | Service type                      |
| Tech_Support     | Support availability              |
| Online_Security  | Security services                 |

*(Exact features depend on the trained model)*

---

## 🔄 Data Preprocessing

The API applies the following preprocessing steps internally:

* Categorical feature encoding
* Numerical feature scaling
* Handling missing values
* Feature alignment with the trained model

✔️ Ensures **training–inference consistency**

---

## 🔗 API Endpoints

### 🟢 Health Check

```http
GET /
```

**Response**

```json
{
  "status": "API is running"
}
```

---

### 🔵 Predict Churn

```http
POST /predict
```

#### Request Body (JSON)

```json
{
  "age": 35,
  "gender": "Male",
  "tenure": 12,
  "monthly_charges": 70.5,
  "total_charges": 845.3,
  "contract_type": "Month-to-month",
  "payment_method": "Electronic check",
  "internet_service": "Fiber optic",
  "tech_support": "No",
  "online_security": "Yes"
}
```

#### Response

```json
{
  "prediction": "Customer Likely to Churn"
}
```

---

## 🧪 API Flow

```text
Client Request (JSON)
   ↓
Input Validation
   ↓
Preprocessing
   ↓
Feature Scaling
   ↓
ML Model
   ↓
Churn Prediction (JSON Response)
```

---

## 📁 Project Structure

```text
Churn-Api/
│
├── model/
│   ├── scaler.pkl
│   └── churn_model.pkl
│
├── app.py                 # API application
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── venv/                  # Virtual environment (optional)
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sahilkumar8084/Churn-Api.git
cd Churn-Api
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the API

```bash
python app.py
```

API runs locally at:

```
http://localhost:5000
```

---

## 📦 Requirements

* `flask` / `fastapi`
* `pandas`
* `scikit-learn`
* `joblib`
* `numpy`
* `uvicorn` (if FastAPI)

---

## ☁️ Deployment

* Deployed using **Render**
* Supports continuous deployment from GitHub
* Suitable for production testing and demos

---

## 🚀 Future Improvements

* Add prediction probability scores
* JWT authentication
* API rate limiting
* Logging & monitoring
* Dockerize the API
* Swagger / OpenAPI documentation

---

## 🏆 Learning Outcomes

* Building RESTful ML APIs
* Model deployment without UI
* Handling production inference pipelines
* Integrating ML with backend services
* Cloud deployment using Render

---

## 👨‍💻 Author

**Sahil Kumar**
Machine Learning Enthusiast
India 🇮🇳

---

## 📜 License

This project is intended for **educational and learning purposes**.


⭐ **Live, production-style ML API ready for integration!**


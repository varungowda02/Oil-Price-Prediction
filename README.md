````markdown
# 🛢️ Oil Price Prediction App

## 🎯 Objective

Oil prices are unpredictable! A single market event can send prices soaring or plummeting. Unlike other commodities, oil prices often move based on external factors rather than real-time supply-demand data.  

This project helps **customers, businesses, and stakeholders** understand price trends and make smarter decisions using predictive modeling. 📈

---

## ✨ Features

- 🔮 **Predict Future Prices:** Predict `Close/Last` based on historical `High` and `Low` prices.  
- 📊 **Interactive Forecasting:** Input the number of months to see future price forecasts.  
- 📉 **RMSE Display:** Model’s prediction accuracy displayed dynamically.  
- 🟢 **Colorful Interface:** Predictions highlighted inside green boxes for clarity.  
- 🧠 **Exponential Regression Model:** Uses log transformation for better accuracy.

---

## 📊 Dataset

The dataset (`df2`) contains daily oil prices:

| Column       | Description                   |
|-------------|--------------------------------|
| `High`       | Daily highest price           |
| `Low`        | Daily lowest price            |
| `Open`       | Daily opening price (optional)|
| `Close/Last` | Daily closing price           |

> ⚡ Only `High` and `Low` are used in the model to reduce multicollinearity.

---

## 🛠️ Model Details

- **Type:** Exponential regression with log-transformed features  
- **Formula:** `LogClose ~ LogHigh + LogLow`  
- **Performance:** RMSE ≈ `0.785`  
- **Tools:** Python, Pandas, NumPy, Statsmodels  

---

## 📥 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/oil-price-prediction.git
cd oil-price-prediction

# Install dependencies
pip install -r requirements.txt
````

---

## 🚀 Running the Streamlit App

```bash
# Run the app
streamlit run app.py
```

> 💡 You can run this on Google Colab or locally. The app supports interactive predictions and forecasts.

---

## 🖥️ Usage

1. Enter **High** and **Low** values in the input fields.
2. Click **Predict** to see the **predicted Close/Last** inside a green box 🟢.
3. Enter the number of months to forecast future prices 📅.
4. View:

   * Predicted closing price
   * RMSE of the model
   * Forecasted prices for the next `n` months

---

## 📸 Screenshots

<img width="811" height="507" alt="image" src="https://github.com/user-attachments/assets/e0a4b709-68a2-4a03-9a31-9fc9acf15cdd" />

<img width="1002" height="1390" alt="image" src="https://github.com/user-attachments/assets/eff8e4ba-b93a-4c30-8090-482d406f6c5e" />


---

## 🗂️ Folder Structure

```
├── app.py                 # Streamlit app
├── model.pkl              # Dumped exponential regression model
├── requirements.txt       # Python dependencies
├── README.md
└── data/                  # Historical oil price dataset (optional)
```

---

## 💡 Future Improvements

* 📈 Integrate market indicators for robust forecasting
* ⏱️ Add real-time price updates using APIs
* 🔍 Visualize historical trends and anomalies
* 🤖 Explore advanced models (Prophet, ARIMA, LSTM) for comparison

---

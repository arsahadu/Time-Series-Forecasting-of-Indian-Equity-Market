
# Time Series Forecasting of Indian Equity Market using Machine Learning

A complete ML pipeline to forecast Indian stock prices using ARIMA, Prophet, and LSTM. This project showcases real-time forecasting, dashboard visualization, and multi-model comparisons for 9 major Indian stocks.

---

## 🚀 Project Overview

This project aims to predict future stock prices for selected Indian companies using:
1. Statistical Modeling (ARIMA)
2. Additive Models (Facebook Prophet)
3. Deep Learning (LSTM)

It covers data collection, preprocessing, modeling, evaluation, and dashboard visualization — an end-to-end pipeline from raw data to insights.

---

## Team Members:

- **Alahadu** 
- **Ajay**
- **Aravind**
---

## 📂 Folder Structure

Time-Series-Forecasting-of-Indian-Equity-Market/
├── app.py # Dash dashboard to visualize predictions
├── Time_Series_Forecasting.ipynb # Main Colab notebook
├── lstm_results/ # Output CSVs: forecast + future_forecast for 9 stocks
├── requirements.txt # Python dependencies
└── README.md # You're here!


## Data Sources

- Historical Stock Prices: `yfinance`, `nsepy`, `Alpha Vantage`
- Macro Indicators: Inflation, GDP from public datasets


## 🛠️ Tools & Libraries Used

| Category         | Tools                                      |
|------------------|---------------------------------------------|
| Language         | Python 3.11                                 |
| Data Processing  | pandas, numpy                               |
| Visualization    | matplotlib, seaborn, plotly                 |
| Models           | statsmodels (ARIMA), Prophet, LSTM (Keras)  |
| Dashboard        | Dash (Python Framework)                     |
| Deployment       | Google Colab + GitHub                       |

---

## Models Built

| Model   | Description                                      |
|---------|--------------------------------------------------|
| ARIMA   | Classical time series model                      |
| Prophet | Trend-seasonality based forecasting              |
| LSTM    | Deep learning model for sequence prediction      |

Each model is evaluated using:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

---

## 📈 Output

- Future predictions for each of the 9 selected stocks
- Visualized using Dash web app
- CSV files saved in `/lstm_results/` as:
  - `STOCK_forecast.csv` (train/test/prediction)
  - `STOCK_future_forecast.csv` (next N days prediction)

---

## Dash App Usage

To run the dashboard locally:

```bash
python app.py
⚠️Make sure your lstm_results/ folder is in the same directory as app.py.

How to Use:
Clone this repo

Run the notebook (Time_Series_Forecasting.ipynb) in Google Colab

Forecasts will be saved in lstm_results/

Launch app.py to explore the results visually

🔭 Future Enhancements:
Add evaluation for future_forecast using post-hoc data

Deploy dashboard using Streamlit Cloud or Render

Integrate financial news and sentiment analysis

 License
MIT License © 2025 Prinz Ahad

Acknowledgements:
Yahoo Finance (via yfinance)

NSE India API

Facebook Prophet team

Keras / TensorFlow community

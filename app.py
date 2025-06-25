
import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

DATA_DIR = "/content"

# Read all CSVs
stock_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith("_forecast.csv")])
stock_names = [f.replace("_forecast.csv", "") for f in stock_files]

app = Dash(__name__)
app.title = "Stock Forecast Dashboard"

app.layout = html.Div([
    html.H1("📈 LSTM Stock Forecast Dashboard", style={"textAlign": "center"}),
    html.Div([
        dcc.Dropdown(
            id='stock-dropdown',
            options=[{"label": name, "value": name} for name in stock_names],
            value=stock_names[0]
        )
    ], style={"width": "50%", "margin": "auto"}),

    dcc.Graph(id="stock-graph")
])

@app.callback(
    Output("stock-graph", "figure"),
    Input("stock-dropdown", "value")
)
def update_graph(stock):
    forecast_path = os.path.join(DATA_DIR, f"{stock}_forecast.csv")
    df = pd.read_csv(forecast_path)
    df['Date'] = pd.to_datetime(df['Date'])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Actual'], name="Actual"))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Predicted'], name="Predicted"))

    fig.update_layout(title=f"{stock} Stock Price Forecast", xaxis_title="Date", yaxis_title="Price")
    return fig

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8051)

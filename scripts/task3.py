import pandas as pd
import dash
from dash import dcc, html, Dash
import plotly.express as px

df = pd.read_csv("data/output.csv")
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"] = df["price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date", as_index=False)["sales"].sum().sort_values("date")

fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    labels={"date": "Date", "sales": "Total Sales ($)"},
)

app = Dash(__name__)

colors = {
    "background": "#f9f9f9",
    "text": "#333333",
}

app.layout = html.Div(style={"backgroundColor": colors["background"]}, children=[
    html.H1(
        children = "Pink Morsel Sales Overview",
        style = {
            "color": colors["text"], "textAlign": "center", "padding": "20px", "margin": "0 auto", "fontSize": "72px"
        }
    ),

    html.Div(
        children = "A line chart showing total daily sales for Pink Morsel.",
        style = {
            "color": colors["text"], "textAlign": "center", "paddingBottom": "20px", "fontSize": "45px"
        }
    ),

    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)

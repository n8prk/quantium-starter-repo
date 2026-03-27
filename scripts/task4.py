import pandas as pd
import dash
from dash import dcc, html, Dash, Input, Output
import plotly.express as px

df = pd.read_csv("data/output.csv")
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"] = df["price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f0f2f5",
        "minHeight": "100vh",
        "fontFamily": "'Segoe UI', Arial, sans-serif",
        "padding": "40px 60px",
    },
    children=[
        # Header card
        html.Div(
            style={
                "backgroundColor": "#1a1a2e",
                "borderRadius": "12px",
                "padding": "32px 40px",
                "marginBottom": "28px",
                "boxShadow": "0 4px 16px rgba(0,0,0,0.18)",
            },
            children=[
                html.H1(
                    "Pink Morsel Sales Overview",
                    style={
                        "color": "#ffffff",
                        "textAlign": "center",
                        "margin": "0 0 10px 0",
                        "fontSize": "42px",
                        "letterSpacing": "1px",
                    },
                ),
                html.P(
                    "A line chart showing total daily sales for Pink Morsel.",
                    style={
                        "color": "#a0aec0",
                        "textAlign": "center",
                        "margin": "0",
                        "fontSize": "16px",
                    },
                ),
            ],
        ),

        # Radio Button card
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "12px",
                "padding": "20px 32px",
                "marginBottom": "28px",
                "boxShadow": "0 2px 8px rgba(0,0,0,0.07)",
                "display": "flex",
                "alignItems": "center",
                "gap": "16px",
            },
            children=[
                html.Span(
                    "Filter by Region:",
                    style={
                        "fontWeight": "600",
                        "fontSize": "15px",
                        "color": "#2d3748",
                        "whiteSpace": "nowrap",
                    },
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "6px", "cursor": "pointer"},
                    labelStyle={
                        "marginRight": "24px",
                        "fontSize": "15px",
                        "color": "#4a5568",
                        "cursor": "pointer",
                    },
                ),
            ],
        ),

        # Chart card
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "12px",
                "padding": "24px",
                "boxShadow": "0 2px 8px rgba(0,0,0,0.07)",
            },
            children=[
                dcc.Graph(id="sales-chart"),
            ],
        ),
    ],
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    daily_sales = filtered.groupby("date", as_index=False)["sales"].sum().sort_values("date")
    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        color_discrete_sequence=["#4f46e5"],
    )
    fig.update_traces(line={"width": 2.5})
    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font={"family": "'Segoe UI', Arial, sans-serif", "color": "#2d3748"},
        xaxis={
            "gridcolor": "#e2e8f0",
            "linecolor": "#cbd5e0",
            "title_font": {"size": 13},
        },
        yaxis={
            "gridcolor": "#e2e8f0",
            "linecolor": "#cbd5e0",
            "title_font": {"size": 13},
        },
        margin={"t": 20, "b": 40, "l": 60, "r": 20},
        hovermode="x unified",
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)

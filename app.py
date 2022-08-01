import dash
from dash import dcc
from dash import html 
import plotly.express as px
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

app.layout = html.Div(
    [   
        # Dropdown to filter developing/developed country.
        html.Div(
            [
                dcc.Dropdown(
                    id="status-dropdown",
                    options=[{"label": s, "value": s} for s in df.Status.unique()], # Create available options from the dataset
                ),
            ]
        ),
        # Dropdown to filter countries with average schooling years.
        html.Div(
            [
                dcc.Dropdown(
                    id="schooling-dropdown",
                    options=[
                        {"label": y, "value": y}
                        for y in range(
                            int(df.Schooling.min()), int(df.Schooling.max()) + 1
                        )
                    ], # add options from the dataset.
                ),
            ]
        ),
        # Placeholder to render teh chart.
        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),

        # Slider to select year.
        dcc.Slider(
            "year-slider",
            min=df.Year.min(), # dynamically select minimum and maximum years from the dataset.
            max=df.Year.max(),
            step=None,
            marks={year: str(year) for year in range(df.Year.min(), df.Year.max() + 1)}, # set markers at one year interval.
            value=df.Year.min()
        ),
    ],
)



if __name__ == "__main__":
    app.run_server(debug=True)


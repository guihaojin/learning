from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', n=100),
    dict(Task="Job A", Start='2008-01-01', Finish='2010-02-28', n=10),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', n=50),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', n=20),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="n",)
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()

app.layout = html.Div(children=[
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)

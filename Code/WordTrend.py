import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("philosophy_data.csv") 

def count_word_occurrences(word):
    word_counts = df[df["sentence_str"].str.contains(word, case=False, na=False)]
    return word_counts.groupby("original_publication_date").size().reset_index(name="count")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Philosophical Evolution Over Time"),
    dcc.Input(id="word-input", type="text", value="truth", debounce=True),
    dcc.Graph(id="word-trend"),
])

@app.callback(
    dash.Output("word-trend", "figure"),
    [dash.Input("word-input", "value")]
)
def update_graph(word):
    word_data = count_word_occurrences(word)
    fig = px.line(word_data, x="original_publication_date", y="count", title=f"Occurrences of '{word}' Over Time")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

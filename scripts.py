import plotly.express as px
import pandas as pd

def generate_scatter_plotly_graph(data, title):
    df = pd.DataFrame(data)
    fig = px.scatter(df, x='x', y='y', title=title)
    div = fig.to_html(full_html=False)
    return div
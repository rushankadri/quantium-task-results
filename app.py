from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_output.csv')
df = df.sort_values(by="date")

app = Dash(__name__)

# Layout with styling
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'fontFamily': 'sans-serif', 'padding': '40px'}, children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Filter by Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', # Default value
            inline=True,
            style={'display': 'inline-block'}
        ),
    ]),

    dcc.Graph(id='sales-graph', style={'borderRadius': '15px', 'overflow': 'hidden', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'})
])

# Callback to update the graph based on radio button selection
@callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales Trend: {selected_region.capitalize()}")
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#2c3e50'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
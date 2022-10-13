import base64
import datetime
import io
from multiprocessing.sharedctypes import Value

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

external_stylesheets=[dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  
#,suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),index_col=False)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    fig = px.bar(df, x="Period Start", y=["Electricity Day Consumption","Electricity Night Consumption"], barmode="stack") # or  barmode="group"

    
    return html.Div([    
        html.H5(datetime.datetime.fromtimestamp(date)),
        dbc.Button(
            children="Show table", id="button-to-show_or_hide-table", className="me-2", value="show"),
        html.Div([
        html.H6(filename),
        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr()  # horizontal line
        ],id = 'table-to-hide',style= {'display': 'block'}),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ],style= {'display': 'block'})

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)] 
        return children

#@app.callback(Output(component_id='element-to-hide', component_property='style'),
#                [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])
#def show_hide_element(visibility_state):
#    if visibility_state == 'on':
#        return {'display': 'block'}
#    if visibility_state == 'off':
#        return {'display': 'none'}

@app.callback(Output(component_id='table-to-hide', component_property='style'),
                Output("button-to-show_or_hide-table", "children"),
                Output("button-to-show_or_hide-table", "value"),
                Input("button-to-show_or_hide-table", "value"))
def on_button_click(value):
    print(f"callback {value}")
    if value == 'show':
        return ({'display': 'block'}, 'Hide table', 'hide')
    else:
        return ({'display': 'none'}, 'Show table', 'show')

if __name__ == '__main__':
    app.run_server(debug=False,host='0.0.0.0',port=80)


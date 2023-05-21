from dash import Dash, html, dash_table
from datetime import datetime, date
import pandas as pd
app = Dash(__name__)
lnk = 'https://raw.githubusercontent.com/geversde/python-github-action-template/main/rho_output/mlbrho' + datetime.today().strftime("%Y%m%d") +'.csv'
server = app.server

def serve_layout():
    return dash_table.DataTable(data = pd.read_csv(lnk).to_dict("records"),page_size=20)

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)


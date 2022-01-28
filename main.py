# import dash
# import dash_core_components as dcc
# import dash_html_components as html
import dash
from os import sep
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json



# Manter apenas os dados dos Estados (Removendo onde o Estado é NAN e onde possui valore dos Municípios)
# df = pd.read_csv('HIST_PAINEL_COVIDBR_13mai2021.csv',sep=';')
# df_states = df[(~df['estado'].isna()) & (df['codmun'].isna())]
# df_brasil = df[df['regiao'] == 'Brasil']
# df_states.to_csv('df_states.csv')
# df_brasil.to_csv('df_brasil.csv')

# brasil_states = json.load(open('geojson/brazil_geo.json','r'))

# print(type(brasil_states['features']))
# print(brasil_states['features'][0].keys())

# {'type': 'Feature', 'id': 'AC', 'properties': {'name': 'Acre'}, 'geometry': {'type': 'Polygon', 'coordinates':

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

fig = px.choropleth_mapbox()

from cProfile import label
from math import trunc
from unicodedata import name
from matplotlib.axis import XAxis
from matplotlib.pyplot import text, title
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

import os

import plotly.graph_objects as go

df = pd.read_csv(os.getcwd()+r'\plotly\dados\Caste.csv',
                 encoding='UTF-8', sep=',')

df_ = df.groupby(['year', 'gender'], as_index=False)[
    ['detenues', 'under_trial', 'convicts', 'others']].sum()
print(df_[:5])


# Build graph with Express

# barchart = px.bar(
#     data_frame=df_,
#     x="year",
#     y="convicts",
#     color="gender",

#     # Possibilidades de paleta de cores

#     # color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"],
#     color_discrete_map={
#         'Female': 'red',
#         'Male': 'blue'
#     },
#     # color_discrete_sequence=px.colors.sequential.Blackbody,

#     labels={"convicts": "Convicts in Maharashtra",
#             "gender": "Gender"},           # map the labels of the figure

#     title='Estatística de prisioneiros na India',  # figure title
#     width=1400,                   # figure width in pixels
#     height=800,                   # figure height in pixels
#     # ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"],
#     template='plotly_dark',

#     text='convicts',  # values appear in figure as text labels

#     # values appear as extra data in the hover tooltip
#     hover_data=['detenues'],

#     animation_frame='year',     # assign marks to animation frames

# )

# pio.show(barchart)

# Build same graph but with GO (another way, more complexity but more power)

# fig = go.Figure()

# fig.add_trace(
#     go.Bar(
#         x=df_['year'],
#         y=df_['convicts'],
#         name='Convicts',
#     )
# )
# fig.add_trace(
#     go.Bar(
#         x=df_['year'],
#         y=df_['detenues'],
#         name='Detenues'
#     )
# )

# fig.show()

fig = go.Figure()

list_cores = []
list_cores_line = []
for i in range(0, int(len(df_)/2)):
    list_cores.extend(["rgba(255, 0, 0, 0.6)", "rgba(55, 128, 191, 0.6)"])
    list_cores_line.extend(
        ["rgba(255, 0, 0, 1.0)", "rgba(55, 128, 191, 1.0)"])

graph_convicts = {
    'x': df_['year'],
    'y': df_['convicts'],
    'type': 'bar',
    'name': 'Convicts',
    "marker": {
        "line": {
            "color": list_cores_line,
            "width": 1
        },
        "color": list_cores
    }
}


list_cores_others = []
list_cores_line_others = []
for i in range(0, int(len(df_)/2)):
    list_cores_others.extend(
        ["rgba(255, 0, 0, 0.6)", "rgba(11, 156, 49, 0.6)"])
    list_cores_line_others.extend(
        ["rgba(255, 0, 0, 1.0)", "rgba(11, 156, 49, 1.0)"])

graph_others = {
    'x': df_['year'],
    'y': df_['others'],
    'type': 'bar',
    'name': 'Others',
    "marker": {
        "line": {
            "color": list_cores_line_others,
            "width": 1
        },
        "color": list_cores_others
    }
}

graphcs = [graph_convicts, graph_others]

# fig.add_traces(graphcs)
fig.add_trace(graph_convicts)
fig.add_trace(graph_others)

fig.update_layout(
    title='Estatística de prisioneiros na India',
    xaxis_title='Anos',
    yaxis_title='Quantidade',
)

fig.show()

import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1(children='Dash Simples'),
        dcc.Graph(
            id='Gráfico X',
            figure={
                'data': [
                    {'x': ['Jan', 'Fev', 'Mar'], 'y':[
                        20, 12, 50], 'type':'line', 'name':2020},
                    {'x': ['Jan', 'Fev', 'Mar'], 'y':[
                        10, 6, 25], 'type':'bar', 'name':2021}
                ],
                'layout':{'title': 'Consumo de Energia'}
            }
        ),
        dcc.Graph(
            id='Gráfico X2',
            figure={
                'data': [
                    {'x': ['Jan', 'Fev', 'Mar'], 'y':[
                        20, 12, 50], 'type':'line', 'name':2020},
                    {'x': ['Jan', 'Fev', 'Mar'], 'y':[
                        10, 6, 25], 'type':'bar', 'name':2021}
                ],
                'layout':{'title': 'Consumo de Energia'}
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

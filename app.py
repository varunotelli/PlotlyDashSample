import dash
import dash_bootstrap_components as dbc

dash_app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions = True,
                
                )
server = dash_app.server
dash_app.title = "Car Friction"
#dash_app._favicon = 'favicon.png'
user = None




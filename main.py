from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from flask import redirect
from app import dash_app
from app import server
#from app import user
import app
import index
#import auth
import login
import json
import create_account


navbar = dbc.NavbarSimple(
	brand="CAR FRICTION",
	brand_href="#",
	color="primary",
	dark="true",
	brand_style={'font-size':'25px'},
	className='me-0',
	style={'margin-right':'0px'}
	)


footer = html.Footer(
	className="footer",
	children="Developed by Varun Suresh(vsuresh1@uncc.edu) at the University of North Carolina at Charlotte",
	style={
	"justify-content": "center",
	
	"background-color":"#1a1a1a",
	"color":"white",
	"padding": "2em 6em 2em 6em",
	"font-size": "14px"}
        )

dash_app.layout = html.Div(children= [
	dcc.Location(id='url', refresh=False),
	navbar,
	html.Div(id='hidden-div', style={"display": "None"}),
	dbc.Row([html.Div(id='page-content', children=[], style={'height':"100vh"})], style={'height':"100vh"}),
	footer,
	dcc.Store('user-data','session')
	])
	#html.Div(id="graph-div", children=viz),
	#dcc.Store(id="data-store"),
	#dcc.Store(id="graph-store")])
#print(user)

@dash_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),Input('hidden-div','children')], [State('user-data','data')])
def display_page(path, user_data, user_data1):
	#print(path)
	print('hidden-div')
	print(user_data)
	if user_data is not None and user_data.startswith('/'):
		path = user_data
		#print("path="+path) 
	if path == '/' or path == '':
		return login.layout

	elif path == '/content':
		#print(path)
		
		#print(user_data1)
		try:
			app.user = json.loads(user_data1)
		#print(app.user)
			if app.user is not None:
				return index.layout
		except:
			return login.layout
	elif path == '/create-account':
		return create_account.layout



if __name__ == "__main__":
	dash_app.run_server(debug = True)
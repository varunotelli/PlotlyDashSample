from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import index
import auth
import app
#from app import app.user
from app import dash_app
from flask import redirect
import json
#import main

temp = html.Div(
	[
	dbc.Label("Email", html_for="create-email"),
	dbc.Input(type="email", id="create-email", placeholder="Enter email"),
	
	],
	
	)

email_input= html.Div([dbc.Row(
	[
	dbc.Col(
		temp,
		md=5, align='center')
	], 
	align='center',justify='center')
],className="pad-row mt-3")

password_input = html.Div(
	[
	dbc.Row(
		[
		dbc.Col(
			html.Div(
				[
				dbc.Label("Password", html_for="create-password"),
				dbc.Input(
					type="password",
					id="create-password",
					placeholder="Enter password",
					),]
				),
			md=5,
			align='center'
			)
		],align='center', justify="center")
	],
	className="pad-row mt-3",
	)
submit_button = html.Div(
	[
	dbc.Button(
		"Create Account",
		className='mt-3',
		type='submit',
		color="primary",
		id="submit_btn_create"
		),
	]
	)

submit_div = html.Div([dbc.Row(
	[
	dbc.Col(
		submit_button,
		md=5, align='center')
	], 
	align='center',justify='center')
],className="mt-2 me-0")

randomDiv =  html.Div(id='container-button-basic',
             children=[])

form = dbc.Container([dbc.Form([email_input, password_input, submit_div])],  className='h-50',style={"height": "100vh"})

create_link = html.Div([dbc.Row(
	[
	dbc.Col(
		dcc.Link("Already have an account? Sign in!", href='/login', style={"text-align": "center", 
			"margin-left":"60px"}),
		md=5, )
	], 
	align='center',justify='center')
],className="mt-3 ml-5")

layout = html.Div(children= [form,randomDiv,create_link, dcc.Store('user-data1', 'session') ])

@dash_app.callback(
	Output('hidden-div', 'children'),
	
	[Input('submit_btn_create', 'n_clicks')],
	[State('create-email','value'),
	State('create-password','value')])

def update(n_clicks, email_value, pwd):
	#print(n_clicks)
	if n_clicks is not None:
		#print(pwd)
		app.user = auth.create_account(email_value, pwd)
		print('app.user logged in=')
		#print(app.user)
		if app.user is None:
			return 'Error in login'
		
		
		#app.layout = index.layout
		

		return '/content' #, json.dumps(app.user)
	return '/'
	


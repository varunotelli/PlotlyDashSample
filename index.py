from dash import no_update, dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import data
import graph
import columns as cols
from app import dash_app
import csv
import io

df = pd.read_csv('./test.csv')
data_table = data.make_data_table(df)

G = graph.init_graph(df)
elements = graph.convert_nx_to_cyto(G)
viz = graph.visualize_graph(elements)

temp = html.Div(
	[
	dbc.Label("ID", html_for="example-id"),
	dbc.Input(type="text", id="example-id", placeholder="Enter factor id"),
	
	],
	
	)

id_input= html.Div([dbc.Row(
	[
	dbc.Col(
		temp,
		md=5, align='center')
	], 
	align='center',justify='center')
],className="pad-row mt-3")

outcome_input = html.Div(
	[
	dbc.Row(
		[
		dbc.Col(
			html.Div(
				[
				dbc.Label("Outcome", html_for="outcome"),
				dbc.Input(
					type="text",
					id="outcome",
					placeholder="Enter outcome",
					),]
				),
			md=5,
			align='center'
			)
		],align='center', justify="center")
	],
	className="pad-row mt-3",
	)

corr_input = html.Div(
	[
	dbc.Row(
		[
		dbc.Col(
			html.Div(
				[
				dbc.Label("Correlation", html_for="correlation"),
				dbc.Input(
					type="number",
					id="correlation",
					placeholder="Enter correlation",
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
		"Submit",
		className='mt-3',
		type='submit',
		color="primary",
		id="submit_btn_csv"
		),
	]
	)

submit_div = html.Div([dbc.Row(
	[
	dbc.Col(
		submit_button,
		md=5, align='left')
	], 
	align='center',justify='center')
],className="mt-2 me-0")

randomDiv =  html.Div(id='container-button-basic',
			 children=[])

tablediv = html.Div([dbc.Row(
	[
	dbc.Col(
		html.Div(id="table-div", children=data_table),
		width={"size": 8, "offset": 2},
		className="mt-5"
		)
	])])

graphdiv = html.Div(
	html.Div([dbc.Row(
	[
	dbc.Col(
		html.Div(id="graph-div", children=viz),
		width={"size": 8, "offset": 2},
		className="my-5"
		)
	])]))

form = dbc.Container([dbc.Form([id_input, outcome_input, corr_input, submit_div])],  className='h-50',style={"height": "100vh"})

layout = html.Div(children= [
	html.H2("Knowledge Graph Input", style={"margin-top":"15px", "margin-bottom": "10px", "text-align":"center"}),
	form,
	tablediv,	
	graphdiv,
	dcc.Store(id="data-store"),
	dcc.Store(id="graph-store")])

@dash_app.callback(
	
		Output("data-store", "data"),
		Output("graph-store", "data"),
		Output("table-div", "children"),
		Output("graph-div", "children"),
		
		Input("submit_btn_csv","n_clicks"),
		State("example-id","value"),
		State("outcome","value"),
		State("correlation","value"),
		prevent_initial_call=True
	)
def update_data(n_clicks, col_id, outcome, correlation):
	
	filename = './test.csv'
	with open(filename,'a',newline='') as f:
		writer=csv.writer(f)
		writer.writerow([col_id, outcome, correlation])
	
	try:
		if "csv" in filename:
			df = pd.read_csv(filename)
			
		else:
			print("error1")
			return no_update, no_update, no_update, no_update
	except Exception as e:
		print(e)
		return no_update, no_update, no_update, no_update

	data_table = data.make_data_table(df)
	G = graph.init_graph(df)
	elements = graph.convert_nx_to_cyto(G)
	viz = graph.visualize_graph(elements)
	preds = data.make_preds_dropdown(df)
	outcomes = data.make_outcome_dropdown(df)

	return df.to_dict("records"), elements, data_table, viz


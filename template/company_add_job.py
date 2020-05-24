import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from template.datafiles import plot_files,data_gen
from template.datafiles import cb
from template.datafiles import db



job_id_input = dbc.Input(placeholder = 'Enter job Id',id = 'add-job-job-id', type = 'text')
job_title_input = dbc.Input(placeholder = 'Enter job Title',id = 'add-job-job-title',type = 'text')
job_term_input = dcc.Dropdown(
    id = 'add-job-job-term',
    placeholder = 'Select job term',
    options=[
        {'label': 'Full Time','value':'fulltime'},
        {'label': 'Part Time','value':'parttime'},
        {'label': 'Other','value':'other'}
    ])
job_location_input = dbc.Input(placeholder = 'Enter job location',id = 'add-job-job-location',type = 'text')
job_requirement_input = dbc.Textarea(placeholder = 'Enter job requirement',id = 'add-job-job-requirement')
def add_job_layout():
    
    return dbc.Container([
                html.Br(),
                dbc.Row([dbc.Col(dbc.Alert('Job Id'),width = 2),dbc.Col(job_id_input)],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Job Title'),width = 2),dbc.Col(job_title_input)],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Term'),width = 2),dbc.Col(job_term_input)],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Location'),width = 2),dbc.Col(job_location_input)],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Job Requirment'),width = 2),dbc.Col(job_requirement_input)],justify = 'center'),
                dbc.Button("Submit",id = 'add-job-submit'),
                html.Div(id = 'add-job-msg')  #used for entering values to database            
])





from company_navbar import Navbar
nav = Navbar()
def ret_body():
    body = html.Div(children=[add_job_layout()])
    return body

def Company_add_job():
    layout = html.Div([nav,ret_body()])
    return layout



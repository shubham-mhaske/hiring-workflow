
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from template.login_navbar import Navbar
import dash_bootstrap_components as dbc

from template.datafiles import data_gen



nav = Navbar()
form = dbc.Container([
    html.Br(),
    dbc.Row(
        dbc.Col([
        dbc.Input(id='candidate-signup-email', type='email', placeholder = 'Enter Email Id'),
        html.Br(),
        dbc.Input(id='candidate-signup-pass', type='password', placeholder = 'Enter password'),
        html.Br(),
        dbc.Input(id='candidate-signup-name', type='text', placeholder = 'Enter Your Name'),
        html.Br(),
        dcc.Dropdown(

                id = 'candidate-signup-state-dropdown',
                options = data_gen.get_state_dropdown(),
                placeholder =  'Select State'
        ),
        html.Br(),
        dcc.Dropdown(

                id = 'candidate-signup-city-dropdown',
                placeholder =  'Select City'
        ),
        html.Br(),
        dbc.Row([ dbc.Col(dbc.Alert('Skills'),width = 4),dbc.Col(dbc.Textarea(id = 'candidate-signup-skills-input'))]),
        dbc.Row([ dbc.Col(dbc.Alert('Education'),width = 4),dbc.Col(dbc.Textarea(id = 'candidate-signup-education-input'))]),
        dbc.Row([ dbc.Col(dbc.Alert('Experience'),width = 4),dbc.Col(dbc.Textarea(id = 'candidate-signup-experience-input'))]),
        dbc.Button("Sign Up",id= 'candidate-signup-button'),
        html.Br(),
        html.Div(id='candidate-signup-success-msg'),
        html.Br()
        ], width = 6),
        
        justify = 'center'
    )
])




def Candidate_signup():
    layout = html.Div([nav,form])
    return layout



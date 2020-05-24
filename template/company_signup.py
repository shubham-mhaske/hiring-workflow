
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
        dbc.Input(id='company-signup-email', type='email', placeholder = 'Enter Email Id'),
        html.Br(),
        dbc.Input(id='company-signup-pass', type='password', placeholder = 'Enter password'),
        html.Br(),
        dbc.Input(id='company-signup-name', type='text', placeholder = 'Company Name'),
        html.Br(),
        dcc.Dropdown(

                id = 'company-signup-state-dropdown',
                options = data_gen.get_state_dropdown(),
                placeholder =  'Select State'
        ),
        html.Br(),
        dcc.Dropdown(

                id = 'company-signup-city-dropdown',
                placeholder =  'Select City'
        ),
        html.Br(),
        dbc.Row([ dbc.Col(dbc.Alert('About Company'),width = 4),dbc.Col(dbc.Textarea(id = 'company-signup-about-input'))]),
        dbc.Button("Sign Up",id= 'company-signup-button'),
        html.Br(),
        html.Div(id='company-signup-success-msg'),
        html.Br()
        ], width = 6),
        
        justify = 'center'
    )
])




def Company_signup():
    layout = html.Div([nav,form])
    return layout



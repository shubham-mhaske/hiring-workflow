import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from template.login_navbar import Navbar
import dash_bootstrap_components as dbc
nav = Navbar()
form = dbc.Container([
    html.Br(),
    dbc.Row(
        dbc.Col([
        dbc.Input(id='user-login-email', type='email', placeholder = 'Enter email'),
        html.Br(),
        dbc.Input(id='user-login-pass', type='password', placeholder = 'Enter password'),
        html.Br(),
        dcc.Dropdown(

                id = 'user-type-dropdown',
                options = [
                    {'label': 'Candidate', 'value': 'Candidate'},
                    {'label': 'Admin', 'value': 'Admin'},
                    {'label': 'Company', 'value': 'Company'}
                ],
                placeholder =  'Select User Type',
                value='Candidate'
        ),
        html.Br(),
        dbc.Button(id='login-submit-button', n_clicks=0, children='Login'),
        
        html.Br(),
        html.Div(id='login-success-msg'),
        html.Br()
        ], width = 6),
        
        justify = 'center'
    )
])




def Login():
    layout = html.Div([nav,form])
    return layout
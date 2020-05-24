import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from template.datafiles import db,plot_files,data_gen


def get_analytics_container():
    company_dropdown = dcc.Dropdown(

                id = 'analytics-candidate-select-dropdown',
                options = data_gen.get_candidate_dropdown_list(),
                placeholder =  'candidate',
                value='not selected',
                
                
    )
    
    return dbc.Container([
            html.Br(),

            dbc.Row([
                dbc.Col(company_dropdown),
                ],
                justify = 'start'
            ),
            html.Br(),
            html.Div(id = 'analytics-candidate-details-card')                 
    ])





from admin_navbar import Navbar

nav = Navbar()


def Analytics_candidate_details():
    layout = html.Div([nav,get_analytics_container()])
    return layout
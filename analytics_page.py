import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import  Input,Output,State


from template.datafiles import db,plot_files,data_gen


def get_analytics_container():
    company_dropdown = dcc.Dropdown(

                id = 'analytics-company-select-dropdown',
                options = data_gen.get_company_dropdown_options(),
                placeholder =  'Company',
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
            html.Div(id = 'analytics-company-details-card')                 
    ])

from company_navbar import Navbar
nav = Navbar()


def Company():
    layout = html.Div([nav,get_analytics_container()])
    return layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY ])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False,pathname='/login'),
    html.Div(id = 'page-content',children=[Company()])
])


'''
callbacks
'''
@app.callback(Output('analytics-company-details-card', 'children'),
              [Input('analytics-company-select-dropdown', 'value')])
def display_job_details(userid):
    
    time_spent_card = dbc.Card([
                        dbc.CardHeader('Time Spent'),
                        dbc.CardBody([
                            dbc.Alert(db.get_time_spent_from_id(userid,'0')[0][0])])
                        ]
                    )
    

    info = plot_files.display_company_details(userid)          
    return dbc.Container([
        html.Br(),
        time_spent_card,
        html.Br(),
        info
    ]) 


if __name__ == '__main__':
    app.run_server(debug=True,port=5153)



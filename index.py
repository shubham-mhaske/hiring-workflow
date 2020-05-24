import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from template.homepage import Homepage

from template.datafiles.cb import register_callback
from template.datafiles import db
from template.login import Login
from template.jobs import Jobs
from template.company_page import Company
from template.candidate_my_profile import Candidate_my_profile
from template.company_add_job import Company_add_job
from template.company_signup import Company_signup
from template.candidate_signup import Candidate_signup
from analytics_candidate_details import Analytics_candidate_details
from admin_company_details import Analytics_company_details
 
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False,pathname='/login'),
    html.Div(id = 'page-content')
])




register_callback(app)
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    from template.datafiles import cb
    if cb.login_flag:
        
        
        if pathname == '/jobs':
            return Jobs() 
        elif pathname == '/applications':
            return Company()
        elif pathname == "/add-new-job":
            return Company_add_job()
        elif pathname == '/logout':
            cb.login_flag_updater('logout',0)
            db.add_session(cb.login_userid,cb.login_flag,int(cb.signout_time-cb.signin_time))
            pathname = '/login'
            return Login()
        elif pathname == '/login-to-home':
            if cb.login_rights == 0:
                return Jobs()
            elif cb.login_rights == 1:
                return Company()
            elif cb.login_rights == 2:
                return Analytics_candidate_details()
        elif pathname == '/candidate-my-profile':
            return Candidate_my_profile()
        elif pathname == '/analytics-company-info':
            return Analytics_company_details()
        elif pathname == '/analytics-candidate-info':
            return Analytics_candidate_details()  
        else:
            return Homepage() 
    else:
        if pathname == '/login':
            return Login()
        elif pathname == '/company-signup':
            return Company_signup()
        elif pathname == '/candidate-signup':
            return Candidate_signup()
        else:  
            return Login()

if __name__ == '__main__':
    app.run()

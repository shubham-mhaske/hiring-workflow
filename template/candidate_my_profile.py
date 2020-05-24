import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from template.datafiles import plot_files,cb

from navbar import Navbar
nav = Navbar()
def get_body(uid):
    body = dbc.Container(
        [
            plot_files.get_candidate_my_profile(uid)
        ],
    className="mt-4",
    )
    return body

def Candidate_my_profile():
    layout = html.Div([nav,get_body(cb.login_userid)])
    return layout

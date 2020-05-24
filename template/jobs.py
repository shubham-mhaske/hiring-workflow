import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from template.datafiles import plot_files


from navbar import Navbar
nav = Navbar()
body = html.Div(children=[plot_files.get_job_cards()])


def Jobs():
    layout = html.Div([nav,body])
    return layout



'''
    for i in range(9):
        lst.append(
            dbc.Card([
                dbc.CardHeader(jobs.iloc[i,4]),
                dbc.CardBody([
                    jobs.iloc[i,2],
                    
                ])
            ])
        )
    candidate_info = dbc.CardColumns(lst)
    '''
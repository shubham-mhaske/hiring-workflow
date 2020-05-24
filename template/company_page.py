import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from template.datafiles import plot_files,data_gen
from template.datafiles import cb
from template.datafiles import db


def get_posted_job_dropdown_list(company_id):
    job_id_dropdown_options= []
    all_jobs = db.get_company_job_ids(company_id)
    for i in all_jobs:
        tmp = {}
        
        tmp['label'] = i[0]
        tmp['value'] =  i[0]   #jobid
        job_id_dropdown_options.append(tmp)
    return job_id_dropdown_options

    


applied_candidate_info_space = dbc.Col(dbc.Container( [html.Div(id = 'applied-candidate-msg')]),width = 6)
applied_job_info_space = dbc.Col(dbc.Container( [html.Div(id = 'applied-job-msg')]),width = 6)
applied_process_info_space = dbc.Row(dbc.Container( [html.Div(id = 'applied-process-msg')]))


'''
returns applied candidates for a company
'''
def get_applied_candidates(temp):
    applied_candidate_dropdown = dcc.Dropdown(

                id = 'applied-candidate-select-dropdown',
                placeholder =  'Candidate',
                value='not selected',
                
                
    )

    job_id_dropdown = dcc.Dropdown(

                id = 'posted_job-select-dropdown',
                options = get_posted_job_dropdown_list(temp),
                placeholder =  'Job',
                value='not selected',
                
                
    )
    
    return dbc.Container([
            
            html.Br(),

            dbc.Row([
                dbc.Col(job_id_dropdown),
                dbc.Col(dbc.Button('Job Details',id = 'job-selected-view-button'),width = 4)
                ],justify = 'start'),
            html.Br(),
            dbc.Row([
                dbc.Col(applied_candidate_dropdown),
                dbc.Col(dbc.Button('Candidate Details',id = 'candidate-selected-view-button'),width = 4)
                ],justify = 'start'),
            


            html.Br(),
            
            dbc.Row([
                        dbc.Col(dbc.Button('View Process Options',id = 'candidate-selected-contact-button')),
                        dbc.Col(dbc.Button("Submit",id = 'selection-submit-button'))
                        
            ],justify = 'start'),
                
            
            html.Br(),
            applied_process_info_space,
            html.Br(),html.Br(),
            dbc.Row([applied_candidate_info_space,applied_job_info_space]),
            
            html.Div(id = 'temp1')  #used for entering values to database            
])





from company_navbar import Navbar
nav = Navbar()
def ret_body(temp):
    body = html.Div(children=[get_applied_candidates(cb.login_userid)])
    return body

def Company():
    layout = html.Div([nav,ret_body(cb.login_userid)])
    return layout



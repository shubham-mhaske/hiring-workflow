import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from template.datafiles import data_gen,db
import plotly.graph_objs as go


from template.datafiles import cb



job_info_space = dbc.Card( [
        
        dbc.CardBody(
            [
                html.Div(id = 'job-select-action-msg')
         
            ]
        )
    ],  
)


##used in jobs.py 
def get_job_cards():
    
    
    jobs_dropdown = dcc.Dropdown(

                id = 'job-select-dropdown',
                options = data_gen.get_job_dropdown_options(),
                placeholder =  'Select job',
                value='not selected',
                style=dict(
                    width='40%',
                   
                )
            )
    
    return dbc.Container([
            
            html.Br(),
            dbc.Row([
                jobs_dropdown,
                dbc.Button('Apply for job',id = 'job-apply-button')
            ],justify = 'start'),
            html.Br(),
            html.Div(id = 'job-appy-success-alert'),
            html.Br(),
            job_info_space
        
        
])
    
##used in company page

def get_interview_process():
    selection_stage_dropdown = dcc.Dropdown(

                id = 'selection-stage-select-dropdown',
                options = [
                    {'label': 'Shortlisted', 'value': 'Shortlisted'},
                    {'label': 'Interview - 1', 'value': 'Interview1'},
                    {'label': 'Interview - 2', 'value': 'Interview2'},
                    {'label': 'Placed', 'value': 'Placed'},
                    {'label': 'Rejected', 'value': 'Rejected'}
                ],
                placeholder =  'Select job',
                style=dict(
                    width='40%',
                   
                )
            )
    interview_process_form = dbc.Card([
        dbc.CardHeader("Hiring Process Form"),
        dbc.CardBody([
            dbc.Row([ dbc.Col(dbc.Alert('Select date'),width = 4),dcc.DatePickerSingle(id = 'selection-submit-date')]),
            dbc.Row([ dbc.Col(dbc.Alert('Selection Stage'),width = 4),selection_stage_dropdown]),
            
            
        ])
    ])

    return interview_process_form

# Candidate My profile
def get_candidate_my_profile(uid):
    data = db.get_job_of_users(uid)
    lst = []
    for i in data:
        cbody = []
        
        
                
        cbody.append(dbc.Alert("Company Id  :  {} ".format(i[2])))
        cbody.append(dbc.Alert("Status  :  {} ".format(i[3])))
        if i[3] == 'Interview1 ':
            cbody.append(dbc.Alert("Scheduled Date  :  {} ".format(i[4])))
        if i[3] == 'Interview2 ':
            cbody.append(dbc.Alert("Scheduled Date  :  {} ".format(i[5])))
        
        lst.append(dbc.Card([dbc.CardHeader("Job Id  :  {} ".format(i[1])),
                    dbc.CardBody(cbody)]))
    return dbc.CardColumns(lst)



def display_job_details(companyid,jobid):
        job = db.get_company_job_details(companyid,jobid)
        return [
                dbc.Card([
                    dbc.CardHeader(dbc.Row([dbc.Col(['Job Id : ',jobid])],justify = 'center')),
                    dbc.CardBody([
                        dbc.Row([dbc.Col(dbc.Alert('Job Title')),dbc.Col(job[0][2])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('Company')),dbc.Col(companyid)],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('Term')),dbc.Col(job[0][3])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('Location')),dbc.Col(job[0][4])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('Job Requirment')),dbc.Col(job[0][5])],justify = 'center'),
                    ])
                
            ])
        ]

def get_candidate_info_representation(userid):
    candidate = db.get_candidate_details(userid)
    candidate_info = dbc.Card([
        dbc.CardHeader(candidate[0][1]),
        dbc.CardBody([
            dbc.Row([ dbc.Col(dbc.Alert('State')),dbc.Col(candidate[0][2]),dbc.Col(dbc.Alert('City')),dbc.Col(candidate[0][3])]),
            dbc.Row([ dbc.Col(dbc.Alert('Skills')),dbc.Col(candidate[0][4])]),
            dbc.Row([ dbc.Col(dbc.Alert('Education')),dbc.Col(candidate[0][5])]),
            dbc.Row([ dbc.Col(dbc.Alert('Experience')),dbc.Col(candidate[0][6])])
        ])
    ])

    return candidate_info

def display_company_details(companyid):
        company = db.get_full_company_details(companyid)
        return dbc.Card([
                    dbc.CardHeader("Comany Details"),
                    dbc.CardBody([
                        dbc.Row([dbc.Col(dbc.Alert('Company Id'),width = 4),dbc.Col(company[0][0])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('Company Name'),width = 4),dbc.Col(company[0][1])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('State'),width = 4),dbc.Col(company[0][2])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('City'),width = 4),dbc.Col(company[0][3])],justify = 'center'),
                        dbc.Row([dbc.Col(dbc.Alert('About'),width = 4),dbc.Col(company[0][4])],justify = 'center'),
                    ])
                
            ])
                
        


 

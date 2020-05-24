import dash
from dash.dependencies import  Input,Output,State

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from template.datafiles import data_gen,plot_files
from template.datafiles import db
import time

import json
with open('template/datafiles/state_cities.json', 'r') as fp:
        state_cities_dict = json.load(fp)


login_flag =0
login_userid= ''
login_rights = 0  # 0-candidate, 1-company, 2-admin


signin_time = 0     #used for calculating time spent
signout_time = 0

def login_flag_updater(status,flag):
    global login_flag,signin_time,signout_time
    if(status =='login'):
        login_flag = flag
        signin_time = time.time()
    elif(status == 'logout'):
        signout_time = time.time()
        login_flag = flag



colors = {
    'text' : '#F0F0F0',
    'paper_color': '#161a28',
    'plot_color': '#161a28' ,
    'transperent': 'rgba(0,0,0,0.0)'
}


def register_callback(app):

    @app.callback(dash.dependencies.Output('candidate-info','children'),
                    [Input('candidate-search-button', 'n_clicks')],
                    [State('candidate-name-input', 'value')])

    def display_candidate_bio(n_clicks,value):
        if (n_clicks):    
                candidate_bio =  data_gen.get_candidate_bio(value)
                if (candidate_bio):
                    return plot_files.get_candidate_info_representation(value,candidate_bio)
                else:
                    return 'No records'
    
    #user login callback
    @app.callback(Output('login-success-msg', 'children'),
              [Input('login-submit-button', 'n_clicks')],
              [State('user-login-email', 'value'),
               State('user-login-pass', 'value'),
               State('user-type-dropdown', 'value')])
    def login_func(n_clicks, user_id, user_pass,user_type):
        global login_userid,login_rights
        if(n_clicks):
            login_flag,login_userid,login_rights = db.check_user(user_id,user_pass,user_type)
            if(login_flag):
                login_flag_updater('login',login_flag)
                return dbc.Alert('Login Successful ! Welcome {}.  Go to Home'.format(login_userid))
            else:
                return dbc.Alert(login_userid,color="danger")

    #job details in candidate
    @app.callback(Output('job-select-action-msg', 'children'),
              [Input('job-select-dropdown', 'value')])

    def display_job_details(value):
        job = db.get_job_details_from_id(value.split('-')[0],value.split('-')[1])
        return [
            
                 #columns = 'job_id', 'Title', 'Company', 'Term', 'Location', 'JobDescription','JobRequirment'

                dbc.Row([dbc.Col(dbc.Alert('Job Id'),width = 2),dbc.Col(job[0][1])],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Job Title'),width = 2),dbc.Col(job[0][2])],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Company'),width = 2),dbc.Col(job[0][0])],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Term'),width = 2),dbc.Col(job[0][3])],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Location'),width = 2),dbc.Col(job[0][4])],justify = 'center'),
                dbc.Row([dbc.Col(dbc.Alert('Job Requirment'),width = 2),dbc.Col(job[0][5])],justify = 'center'),
    
        ] 
    
    @app.callback(Output('job-appy-success-alert','children'),
                 [Input('job-apply-button','n_clicks'),Input('job-select-dropdown', 'value')])
    def appply_to_job(n_clicks,jobid):
        if(n_clicks == 1):
            db.insert_job_apply_record(login_userid,jobid.split('-')[1],jobid.split('-')[0])
            return dbc.Alert("Successfully applied for the job")

 
    

    
    # selection process update 
    @app.callback(Output('temp1','children'),
                [Input('selection-submit-button','n_clicks'),
                Input('applied-candidate-select-dropdown', 'value'),
                Input('posted_job-select-dropdown', 'value'),
                Input('selection-submit-date','date'),
              Input('selection-stage-select-dropdown', 'value'),
              ]
              )
    def insert_process_info(n_clicks,uid,jobid,data,stage):  #insert to candidate_stat after selection process
        return db.update_candidate_selection(uid,data,jobid,stage)


    # add new job in company_add_job
    @app.callback(Output('add-job-msg', 'children'),
              [Input('add-job-submit', 'n_clicks')],
              [State('add-job-job-id', 'value'),
               State('add-job-job-title', 'value'),
               State('add-job-job-term', 'value'),
               State('add-job-job-location', 'value'),
               State('add-job-job-requirement', 'value')])
    def add_job(n_clicks,jobid,title,term,location,requirement):
        companyid = login_userid
        if(n_clicks == 1):
            db.add_new_job(companyid,jobid,title,term,location,requirement)
            return dbc.Alert('New Job Added')


    
    #signup page state wise cities dropdown
    @app.callback(Output('company-signup-city-dropdown', 'options'),
              [Input('company-signup-state-dropdown', 'value')])
    def get_cities_dropdown(state):
        
        city_lst = []
        cities = state_cities_dict[state]
        for i in cities:
            tmp = {}
            tmp['label']= i
            tmp['value'] = i
            city_lst.append(tmp)
        return city_lst
    
    @app.callback(Output('candidate-signup-city-dropdown', 'options'),
              [Input('candidate-signup-state-dropdown', 'value')])
    def get_cities_dropdown(state):
        
        city_lst = []
        cities = state_cities_dict[state]
        for i in cities:
            tmp = {}
            tmp['label']= i
            tmp['value'] = i
            city_lst.append(tmp)
        return city_lst


    #company signup add to database
    @app.callback(Output('company-signup-success-msg', 'children'),
              [Input('company-signup-button', 'n_clicks')],
              [State('company-signup-email', 'value'),
               State('company-signup-pass', 'value'),
               State('company-signup-name', 'value'),
               State('company-signup-state-dropdown', 'value'),
               State('company-signup-city-dropdown', 'value'),
               State('company-signup-about-input', 'value')])
    def signup_company(n_clicks,email,password,name,state,city,about):
        if(n_clicks == 1):
            db.company_signup(email,password,name,state,city,about)
            return dbc.Alert('Signup Successful')
            
   #company signup add to database
    @app.callback(Output('candidate-signup-success-msg', 'children'),
              [Input('candidate-signup-button', 'n_clicks')],
              [State('candidate-signup-email', 'value'),
               State('candidate-signup-pass', 'value'),
               State('candidate-signup-name', 'value'),
               State('candidate-signup-state-dropdown', 'value'),
               State('candidate-signup-city-dropdown', 'value'),
               State('candidate-signup-skills-input', 'value'),
               State('candidate-signup-education-input', 'value'),
               State('candidate-signup-experience-input', 'value')])
    def signup_company(n_clicks,email,password,name,state,city,skills,education,experience):
        if(n_clicks == 1):
            db.candidate_signup(email,password,name,state,city,skills,education,experience)
            return dbc.Alert('Signup Successful')


    # company get candidates according to job id
    @app.callback(Output('applied-candidate-select-dropdown', 'options'),
              [Input('posted_job-select-dropdown', 'value')])
    def get_cities_dropdown(jobid):
        
        applied_candidate_dropdown_options = []
        all_candidates = db.get_userid_from_jobid(login_userid,jobid)
        for i in all_candidates:
            tmp = {}
            tmp['label'] = all_candidates[0][0]
            tmp['value'] =  all_candidates[0][0] #userid

            applied_candidate_dropdown_options.append(tmp)
        return applied_candidate_dropdown_options

    '''
    Company Page Callbacks
    '''
    #show job
    @app.callback(Output('applied-candidate-msg', 'children'),
                [Input('candidate-selected-view-button','n_clicks')],
              [State('applied-candidate-select-dropdown', 'value'),
              State('posted_job-select-dropdown', 'value')]
              )
    def display_selected_candidate_details(candidate_view,userid,jobid):
        if candidate_view:
            
            return plot_files.get_candidate_info_representation(userid)


    #show process
    @app.callback(Output('applied-process-msg', 'children'),
                [Input('candidate-selected-contact-button','n_clicks')],
              [State('applied-candidate-select-dropdown', 'value'),
              State('posted_job-select-dropdown', 'value')]
              )
    def display_selected_candidate_details(n_clicks_contact,userid,jobid):

            if(n_clicks_contact):
                return plot_files.get_interview_process()
            
        #show job
    @app.callback(Output('applied-job-msg', 'children'),
                [Input('job-selected-view-button','n_clicks')],
              [State('applied-candidate-select-dropdown', 'value'),
              State('posted_job-select-dropdown', 'value')]
              )
    def display_selected_candidate_details(view_job,userid,jobid):
            if(view_job):
                return plot_files.display_job_details(login_userid,jobid)


    '''
    Analytics
    '''
    #candidate-page
    @app.callback(Output('analytics-candidate-details-card', 'children'),
              [Input('analytics-candidate-select-dropdown', 'value')])
    def display_job_details(userid):
        
        time_spent_card = dbc.Card(
            [dbc.CardHeader('Time Spent'),
            dbc.CardBody([
                db.get_time_spent_from_id(userid,'0')[0][0]
            ])]
        )
        

        info = dbc.Card(
                    dbc.CardBody([
                    plot_files.get_candidate_info_representation(userid)
                    ])
                )
                   
        return dbc.Container([
            html.Br(),
            time_spent_card,
            html.Br(),
            info
        ])


    #company_page
    @app.callback(Output('analytics-company-details-card', 'children'),
              [Input('analytics-company-select-dropdown', 'value')])
    def display_job_details(userid):
        
        time_spent_card = dbc.Card([
                            dbc.CardHeader('Time Spent'),
                            dbc.CardBody([
                                db.get_time_spent_from_id(userid,'0')[0][0]])
                            ],
                            className = "card border-info"
                        )
        no_of_jobs = dbc.Card(
            [dbc.CardHeader('Jobs posted'),
            dbc.CardBody([
                len(db.get_jobs_posted_by_company(userid))
            ])],
            className = "card border-info"
        )

        #get hiring metrics from db
        company_hiring_metric = db.get_company_hiring_stats(userid)  #[placed, interviewed, rejected]
        no_of_placed = dbc.Card(
            [dbc.CardHeader('Placed'),
            dbc.CardBody([
                company_hiring_metric[0],
                
            ])],
            className = "card border-info"
        )

        no_of_interviewed = dbc.Card(
            [dbc.CardHeader('Interviewed'),
            dbc.CardBody([
                company_hiring_metric[1]
            ])],
            className = "card border-info"
        )

        no_of_rejected = dbc.Card(
            [dbc.CardHeader('Rejected'),
            dbc.CardBody([
                company_hiring_metric[2]
            ])],
            className = "card border-info"
        )

        

        info = plot_files.display_company_details(userid)          
        return dbc.Container([
            html.Br(),
            dbc.Row([
                dbc.Col(time_spent_card),
                dbc.Col(no_of_jobs),
                dbc.Col(no_of_placed),
                dbc.Col(no_of_interviewed),
                dbc.Col(no_of_rejected)
                ]),
                
            html.Br(),
            info
        ])



        
    
    

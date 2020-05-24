
import json
from datetime import datetime
from template.datafiles import db
from template.datafiles import cb



import json

with open('template/datafiles/state_cities.json', 'r') as fp:
    state_cities_dict = json.load(fp)

#get state dropdown options
def get_state_dropdown():
    state_lst = []
    for i in state_cities_dict.keys():
        tmp = {}
        tmp['label']= i
        tmp['value'] = i
        state_lst.append(tmp)
    return state_lst



def get_job_info(id):
    if(id == 'not selected'):
        return 'Not found'
    else:
        return dict(jobs.loc[id])

#get job dropdown in candidate apply
def get_job_dropdown_options(): #original attributes
    job_dropdown_options = []
    jobs = db.get_all_jobs()
    for i in jobs:
        tmp = {}
        tmp['label'] = i[2] #job title
        tmp['value'] =  i[0]+'-'+i[1]  #companiid - jobid
        job_dropdown_options.append(tmp)
    return job_dropdown_options

#used in analytics
def get_company_dropdown_options():
    company_dropdown_options= []
    companies = db.get_all_companies_id()
    for i in companies:
        tmp = {}
        
        tmp['label'] = i[1]
        tmp['value'] =  i[0]   #companyid
        company_dropdown_options.append(tmp)
    return company_dropdown_options

#used in analytics candidate info
def get_candidate_dropdown_list():
    user_dropdown_options = []
    users = db.get_all_candidate_id()
    for i in users:
        tmp = {}
        tmp['label'] = i[1]
        tmp['value'] =  i[0]   #userid
        user_dropdown_options.append(tmp)
    return user_dropdown_options
    








    

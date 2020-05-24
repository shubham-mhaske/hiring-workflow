import sqlite3

def start_db():

    try:
        sqliteConnection = sqlite3.connect('template/datafiles/appliedJobs.db')
        cursor = sqliteConnection.cursor()
        return sqliteConnection,cursor
        

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def check_user(uid,upass,utype):
    sqliteConnection,cursor = start_db()
    if(utype == 'Candidate'):
        cursor.execute(("SELECT * FROM users WHERE userid=?"),(uid,))
        record = cursor.fetchall()
        if(record):
            cursor.execute(("SELECT * FROM users WHERE userid=? AND password=?"),(uid,upass,))
            record = cursor.fetchall()
            if(record):
                return True,uid,0
            else:
                return False,'incorrect password',0
        else:
            return False,'incorrect userid',0
    elif(utype == 'Company'):
        cursor.execute(("SELECT * FROM users_company WHERE userid=?"),(uid,))
        record = cursor.fetchall()
        if(record):
            cursor.execute(("SELECT * FROM users_company WHERE userid=? AND password=?"),(uid,upass,))
            record = cursor.fetchall()
            if(record):
                return True,uid,1
            else:
                return False,'incorrect password',1
        else:
            return False,'incorrect userid',1
    else:
        cursor.execute(("SELECT * FROM users_admin WHERE userid=?"),(uid,))
        record = cursor.fetchall()
        if(record):
            cursor.execute(("SELECT * FROM users_admin WHERE userid=? AND password=?"),(uid,upass,))
            record = cursor.fetchall()
            if(record):
                return True,uid,2
            else:
                return False,'incorrect password',2
        else:
            return False,'incorrect userid',2

    

def insert_job_apply_record(userid,jobid,companyid):
    sqliteConnection,cursor = start_db()
    cursor.execute('insert into candidate_stat(userid,jobid,companyid) values("{}","{}","{}")'.format(userid,jobid,companyid))
    sqliteConnection.commit()

def get_candidates_for_company(companyid):
    sqliteConnection,cursor = start_db()
    cursor.execute(("SELECT userid,jobid FROM candidate_stat WHERE companyid=? "),(companyid,))
    record = cursor.fetchall()
    return record

def update_candidate_selection(uid,date,jobid,status):
    sqliteConnection,cursor = start_db()
    if(status == 'Interview1'):
        query = 'UPDATE candidate_stat SET Interview1 = "{}", Status = "{} " WHERE userid ="{}" AND jobid ="{}" '.format(date,status,uid,jobid)
        cursor.execute(query)
        sqliteConnection.commit()
    elif(status == 'Interview2'):
        query = 'UPDATE candidate_stat SET Interview2 = "{}", Status = "{} " WHERE userid ="{}" AND jobid ="{}" '.format(date,status,uid,jobid)
        cursor.execute(query)
        sqliteConnection.commit()
    else:
        query = 'UPDATE candidate_stat SET Status = "{}" WHERE userid ="{}" AND jobid ="{}" '.format(status,uid,jobid)
        cursor.execute(query)
        sqliteConnection.commit()
    


def get_job_of_users(uid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM candidate_stat WHERE userid = "{}"'.format(uid)
    cursor.execute(query)
    record = cursor.fetchall()
    return record
    
def add_new_job(companyid,jobid,title,term,location,requirement):
    sqliteConnection,cursor = start_db()
    query = 'insert into company_jobs values("{}","{}","{}","{}","{}","{}")'.format(companyid,jobid,title,term,location,requirement)
    cursor.execute(query)
    sqliteConnection.commit()

def company_signup(email,password,name,state,city,about):
    sqliteConnection,cursor = start_db()
    users_company_query = 'insert into users_company values("{}","{}")'.format(email,password)
    company_details_query = 'insert into company_details values("{}","{}","{}","{}","{}")'.format(email,name,state,city,about)

    cursor.execute(users_company_query)
    cursor.execute(company_details_query)
    sqliteConnection.commit()

def candidate_signup(email,password,name,state,city,skills,education,experience):
    sqliteConnection,cursor = start_db()
    users_query = 'insert into users values("{}","{}")'.format(email,password)
    candidate_details_query = 'insert into candidate_details values("{}","{}","{}","{}","{}","{}","{}")'.format(email,name,state,city,skills,education,experience)

    cursor.execute(users_query)
    cursor.execute(candidate_details_query)
    sqliteConnection.commit()


def get_company_job_ids(uid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT jobid FROM company_jobs WHERE companyid = "{}"'.format(uid)
    cursor.execute(query)
    record = cursor.fetchall()

    return record

#get candidates applied to  company according to job id
def get_userid_from_jobid(companyid,jobid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT userid FROM candidate_stat WHERE jobid = "{}" AND companyid = "{}"'.format(jobid,companyid)
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_company_job_details(companyid,jobid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM company_jobs WHERE jobid = "{}" AND companyid = "{}"'.format(jobid,companyid)
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_candidate_details(id):
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM candidate_details WHERE id = "{}"'.format(id)
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_all_jobs():
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM company_jobs'
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_job_details_from_id(companyid,jobid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM company_jobs where companyid = "{}" and jobid = "{}"'.format(companyid,jobid)

    cursor.execute(query)
    record = cursor.fetchall()
    return record

def add_session(id,user_type,timespent):
    sqliteConnection,cursor = start_db()
    query = 'insert into session_details values("{}","{}",{})'.format(id,user_type,timespent)
    cursor.execute(query)
    sqliteConnection.commit()

def get_all_companies_id():
    sqliteConnection,cursor = start_db()
    query = 'SELECT id,name FROM company_details'
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_full_company_details(companyid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM company_details where id = "{}"'.format(companyid)
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_all_candidate_id():
    sqliteConnection,cursor = start_db()
    query = 'SELECT id,name FROM candidate_details'
    cursor.execute(query)
    record = cursor.fetchall()
    return record

def get_time_spent_from_id(id,utype):
    sqliteConnection,cursor = start_db()
    query = 'SELECT timespent FROM session_details where id="{}" and type="{}"'.format(id,utype)
    cursor.execute(query)
    record = cursor.fetchall()
    if(len(record)):
        return record
    else:
        return [(0,)]
    
def get_jobs_posted_by_company(cid):
    sqliteConnection,cursor = start_db()
    query = 'SELECT * FROM company_jobs where companyid="{}"'.format(cid)
    cursor.execute(query)
    record = cursor.fetchall()
    if(len(record)):
        return record
    else:
        return []

def get_company_hiring_stats(cid):
    sqliteConnection,cursor = start_db()
    query_placed_count = 'SELECT COUNT(*) FROM candidate_stat WHERE companyid = "{}" AND Status = "Placed"'.format(cid)
    query_interviewed_count = 'SELECT COUNT(*) FROM candidate_stat WHERE companyid = "{}" AND Status LIKE "Interview%"'.format(cid)
    query_rejected_count = 'SELECT COUNT(*) FROM candidate_stat WHERE companyid = "{}" AND Status = "Rejected"'.format(cid)
    
    count_list = []  #placed,interviewed,rejected
    cursor.execute(query_placed_count)
    placed_record = cursor.fetchall()
    cursor.execute(query_interviewed_count)
    interviewed_record = cursor.fetchall()
    cursor.execute(query_rejected_count)
    rejected_record = cursor.fetchall()
    if(len(placed_record)):
        count_list.append(placed_record[0][0])
    else:
        count_list.append(0)
    
    if(len(interviewed_record)):
        count_list.append(interviewed_record[0][0])
    else:
        count_list.append(0)
    if(len(rejected_record)):
        count_list.append(rejected_record[0][0])
    else:
        count_list.append(0)
    return count_list
   


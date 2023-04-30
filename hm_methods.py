init_ttl_value=600

# creating database connectivity
def check_db_connectivity():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    # from mysql.connector import Error
    
       
    try:
        cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
        crsr = cnx.cursor()
        if cnx.is_connected():
            # print(type(cnx))                  #debug
            # st.write("cnx_mysql", type(cnx))  #debug
            # st.write("crsr", type(crsr))      #debug
            st.sidebar.success("user 'root' connected to 'hospitalDB' successfully", icon="🔥")
            
            crsr.execute("SELECT DATABASE()")       #debug
            db_fetchone=crsr.fetchone()             #debug
            st.write("using DB:", db_fetchone[0])   #debug

            crsr.execute("SELECT DATE(now()), TIME(now())")    #debug
            db_fetchone=crsr.fetchone()     #debug
            st.write("Date, Time:", db_fetchone)           #debug
        else:
            print("Error: unable to connect to database")
        return 0
    except Exception as err:
        st.exception(err)
    finally:
        cnx.commit()
        crsr.close()
        cnx.close()

# show db 
def show_db():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()

    crsr.execute("USE hospitalDB")
    crsr.execute("SELECT DATABASE()")       #debug
    db_fetchone=crsr.fetchone()             #debug
    st.write("using DB:", db_fetchone[0])   #debug

    crsr.execute("SELECT DATE(now())")    #debug
    db_fetchone=crsr.fetchone()     #debug
    st.write("Date:", db_fetchone)           #debug

    cnx.commit()
    crsr.close()
    cnx.close()


# create_table method
def create_table():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()
    
    create_tableq={}
    create_tableq['user_data']='''CREATE TABLE IF NOT EXISTS user_data(
        unm VARCHAR(30),
        pword VARCHAR(30) DEFAULT '000',
        PRIMARY KEY(unm)
        )'''
    create_tableq['doctor_details']='''CREATE TABLE IF NOT EXISTS doctor_details(
        d_id INT AUTO_INCREMENT,
        d_name VARCHAR(30) NOT NULL,
        d_spec VARCHAR(50) DEFAULT "General",
        d_age INT,
        d_addrs VARCHAR(70),
        d_contact VARCHAR(15),
        d_fees DECIMAL(6,0) DEFAULT "1000",
        d_msalary DECIMAL(6, 0) DEFAULT "45000",
        PRIMARY KEY (d_id)
        )'''
    create_tableq['nurse_details']='''CREATE TABLE IF NOT EXISTS nurse_details(
        n_id INT AUTO_INCREMENT,
        n_name VARCHAR(30),
        n_age INT,
        n_address VARCHAR(30),
        n_contact VARCHAR(15),
        n_msalary INT DEFAULT '25000',
        PRIMARY KEY (n_id)
        )'''
    create_tableq['patient_details']='''CREATE TABLE IF NOT EXISTS patient_details(
        p_id INT AUTO_INCREMENT,
        p_name VARCHAR(30),
        p_gender VARCHAR(15),
        p_age INT,
        p_addrs VARCHAR(50),
        p_contact VARCHAR(15),
        d_id INT,
        n_id INT,
        PRIMARY KEY (p_id),
        FOREIGN KEY (d_id) REFERENCES doctor_details(d_id),
        FOREIGN KEY (n_id) REFERENCES nurse_details(n_id)
        )'''
    ## st.write("type of create_table", type(create_table))     #debug
    crsr.execute(create_tableq['user_data'])
    crsr.execute(create_tableq['doctor_details'])
    crsr.execute(create_tableq['nurse_details'])
    crsr.execute(create_tableq['patient_details'])
    
    #cnx.commit()
    crsr.close()
    cnx.close()

def insert_default_doctors_nurses():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()
    
    ## insert three doctors to initialize
    qry_str='''INSERT INTO doctor_details(d_name, d_spec, d_age, d_addrs, d_contact, d_fees, d_msalary) VALUES
    (%s, %s, %s, %s, %s, %s, %s)'''
    #
    qry_params=('doc1_name', 'ENT', 26, 'Mumbai', '7897897890', 2000, 51000)
    st.write('Doctor Inserted:', qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    #
    qry_params=('doc2_name', 'Cardiology', 27, 'Delhi', '4564564560', 2500, 52000)
    st.write('Doctor Inserted:', qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    #
    qry_params=('doc3_name', 'Neurology', 28, 'Pune', '1231231230', 3000, 53000)
    st.write('Doctor Inserted:', qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    ## insert three nurses to initialize
    qry_str='''INSERT INTO nurse_details(n_name, n_age, n_address, n_contact, n_msalary) VALUES
    (%s, %s, %s, %s, %s)'''
    #
    qry_params=('nur1_name', 22, 'Mumbai', '9879879870', 26000)
    st.write("Nurse Inserted:", qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    #
    qry_params=('nur2_name', 23, 'Delhi', '6546546540', 27000)
    st.write("Nurse Inserted:", qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    #
    qry_params=('nur3_name', 23, 'Pune', '3213213210', 28000)
    st.write("Nurse Inserted:", qry_params)    #debug
    crsr.execute(qry_str, qry_params)

    cnx.commit()
    crsr.close()
    cnx.close()
    
def initialize_users():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()
    
    ## users initialization / insertor
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('admin','admin123'))
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('surya','surya123'))
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('swapnil','swapnil123'))
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('vaibhav','vaibhav123'))
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('tejaswini','tejaswini123'))
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('usha','usha123'))
    crsr.execute('''INSERT INTO user_data(unm,pword) VALUES(%s, %s)''', ('ushashree','ushashree'))
    
    cnx.commit()
    crsr.close()
    cnx.close()
    
def show_users():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()
    
    ## user_data table fetch
    crsr.execute("SELECT unm, pword FROM user_data")    #debug
    db_fetchall=crsr.fetchall()                         #debug
    for row in db_fetchall:                             #debug
        st.write("user created:", row[0])               #debug
    cnx.commit()
    crsr.close()
    cnx.close()
    
## show created tables
def show_tables():
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()

    crsr.execute('''SHOW TABLES''')
    db_fetchall=crsr.fetchall()
    for row in db_fetchall:
        st.write("table created:", row[0])
    
    cnx.commit()
    crsr.close()
    cnx.close()

def reset_ttl():
    ttl_value=300
    return ttl_value

def login_action(formuser, formpass):
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()
    
    qry_str="SELECT pword FROM user_data WHERE unm = %s"
    qry_params=(formuser,)
    st.write(qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    db_fetchone=crsr.fetchone()
    #if st.session_state.formpass in db_fetchone[0]:
    if formpass in db_fetchone[0]:
        st.success(body='Logn_action(): user authenticated', icon='🤖')
        st.session_state['login_valid']=True
    else:
        st.error("INCORRECT Credentials !!", icon='💥')

    cnx.commit()
    crsr.close()
    cnx.close()


# close_db_connection method
def close_db_connection(cnx1, cursor1):
    if cnx1.is_connected():
        cursor1.close()
        cnx1.close()
        return True
    else:
        return False
    
def insert_doctor(d_name, d_spec, d_age, d_addr, d_contact, d_fees, d_msalary):
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()

    #st.write(d_name, d_spec, d_age, d_addr, d_contact, d_fees, d_msalary)   #debug
    qry_str='''INSERT INTO doctor_details(d_name, d_spec, d_age, d_addrs, d_contact, d_fees, d_msalary) VALUES
    (%s, %s, %s, %s, %s, %s, %s)'''
    qry_params=(d_name, d_spec, d_age, d_addr, d_contact, d_fees, d_msalary)
    st.write(qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    db_fetchone=crsr.fetchone()
    if db_fetchone == None:
        st.success("Doctor record inserted successfully", icon="🔥")
    else:
        st.error("Error while inserting doctor record", icon="🚨")

    cnx.commit()
    crsr.close()
    cnx.close()

def insert_nurse(n_name, n_age, n_addr, n_contact, n_msalary):
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()\
    
    #st.write(n_name, n_age, n_addr, n_contact, n_msalary)   #debug
    qry_str='''INSERT INTO nurse_details(n_name, n_age, n_address, n_contact, n_msalary) VALUES
    (%s, %s, %s, %s, %s)'''
    qry_params=(n_name, n_age, n_addr, n_contact, n_msalary)
    st.write(qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    db_fetchone=crsr.fetchone()
    if db_fetchone == None:
        st.success("Nurse record inserted successfully", icon="🔥")
    else:
        st.error("Error while inserting nurse record", icon="🚨")
    
    cnx.commit()
    crsr.close()
    cnx.close()


def insert_patient(p_name, p_gender, p_age, p_addr, p_contact, p_d_id, p_n_id):
    import streamlit as st
    import streamlit_authenticator as stauth
    import mysql.connector
    cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
    crsr = cnx.cursor()

    #st.write(d_name, d_spec, d_age, d_addr, d_contact, d_fees, d_msalary)   #debug
    qry_str='''INSERT INTO patient_details(p_name, p_gender, p_age, p_addrs, p_contact, d_id, n_id) VALUES
    (%s, %s, %s, %s, %s, %s, %s)'''
    qry_params=(p_name, p_gender, p_age, p_addr, p_contact, p_d_id, p_n_id)
    st.write(qry_params)    #debug
    crsr.execute(qry_str, qry_params)
    db_fetchone=crsr.fetchone()
    if db_fetchone == None:
        st.success("Patint record inserted successfully", icon="🔥")
    else:
        st.error("Error while inserting patient record", icon="🚨")
    
    cnx.commit()
    crsr.close()
    cnx.close()
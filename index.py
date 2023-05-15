# installing mysql-connector-python module using pip
# pip install mysql-connector-python streamlit streamlit-authenticator SQLAlchemy Cython PyMySQL mysqlclient yaml

import streamlit as st
import streamlit_authenticator as stauth
import mysql.connector
import hm_methods as hmm
import sqlalchemy
import yaml

st.set_page_config(page_title="Login page", page_icon=":hospital:", layout="wide")
st.title(':hospital: Hospital Management App')
st.write('Login page')

#st.write(st.session_state)     #debug

## connection & cursor snippet, to be used at start of each callback
# cnx=mysql.connector.connect(host="localhost", database="hospitalDB", user="root", password="mysql")
# crsr = cnx.cursor(buffered=True)

## connection & cursor closing snippet, to be used at end of each callback
# crsr.close()
# cnx.close()
# st.success("Index: Connection Closed Successfully") #debug


#if "shared" not in st.session_state:
#   st.session_state["shared"] = True
    
## check DB connectivity
# hmm.check_db_connectivity() #un-comment to enable checking db connectivity

## selct DB
# hmm.show_db()               #un-comment to enable printing db

## create tables
hmm.create_table()

## initialize users
# hmm.initialize_users()     #un-comment to enable creating users

## show created tables
# hmm.show_users()           #un-comment to enable printing users

## initialize doctors
# hmm.insert_default_doctors_nurses()   #un-comment to enable inserting default doctors & nurses

## show created tables
# hmm.show_tables()          #un-comment to enable printing tables
    
# login authentication logic
login_col1, login_col2 = st.columns(2)
with login_col1:
    formuser=st.text_input('Enter Username', placeholder="username", key='fmuser')
    
with login_col2:
    formpass=st.text_input('Enter Password', placeholder="password", key='fmpass', type='password')

login_btn=st.button('Login', help="Click here to login")
    
if login_btn:
    # st.write(st.session_state)  #debug
    # st.write("DEBUG", formuser, formpass)  #debug
    hmm.login_action(formuser, formpass)

    

# conx=st.experimental_connection('hospitalDB','sql', ttl=300)
# st.write(conx)
# fetched_pass = conx.query("SELECT pword FROM user_data WHERE uname = :uname", params={"uanme":st.session_state.usnam})
# st.write(fetched_pass)

#st.write(st.session_state.usnam)
#st.write(st.session_state.passw)
#st.write(st.session_state.shared)

#st.sidebar.success('this is success message at index page')
#st.sidebar.button('submit')
#st.button('Submit')
#st.text_area('enter text', height=200, placeholder='place holder for textbox')
#st.


## DB credentials initilization with SQLAlchemy
# db_user='root'
# db_password='mysql'
# db_host='localhost'
# db_port=3306
# db_name='hospitalDB'
# if __name__=='__main__':
#    try:
#         Engine = sqlalchemy.create_engine(url="mysql+pymysql://{0}:{1}@{2}/{4}".format(db_user, db_password, db_host, db_port, db_name))
#         st.success("user '"+db_user+"' connected to '"+db_name+"' successfully", icon="🔥")
#     except Exception as err:
#         st.exception(err)
# st.experimental_connection('sql')



#from yaml.loader import SafeLoaderwith open('config.yaml') as file:
#    config = yaml.load(file, Loader=SafeLoader)


st.markdown("""    © Evaluation Nerds Mar-2023""" )
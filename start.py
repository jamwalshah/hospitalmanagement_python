# installing mysql-connector-python module using pip
# pip install mysql-connector-python streamlit streamlit-authenticator SQLAlchemy Cython PyMySQL mysqlclient yaml

import streamlit as st
import streamlit_authenticator as stauth
import sqlalchemy
import cython
import hm_methods as hmm
import db_connectivity as dbc
import table_create as tc
import close_db_conn as cdc

cnx_val=hmm.make_connectivity()
if cnx_val==0:
    # connection error logic
    print("START: Error encountered while creating DB connection.")
else:
    # connection success logic
    # print server info
    db_info=cnx_val.get_server_info()
    print("START: connected to MySQL Server version", db_info)
    # create cursor for connection
    cursor_val=cnx_val.cursor()
    # fetch DB name
    cursor_val.execute("SELECT DATABASE();")
    dbname=cursor_val.fetchone()
    print("START: You're connected to database: ", dbname)
    # call create_table()
    print(cursor_val)
    print(type(cursor_val))
    cursor_val.execute("SHOW TABLES")
    for ele in cursor_val.fetchall():
        ele_str=list(ele)
        print(ele_str[0])
    '''
    if hmm.create_table(cursor_val):
        print("START: tables initialized successfully")
    else:
        print("START: ERROR: Failed to initialize tables")
    '''
    # close connection logic
    if hmm.close_db_connection(cnx_val, cursor_val):
        print("START: MySQL connection closed")
        
    else:
        print("START: ERROR: Failed to disconnect DB ", dbname)
print("START: Exiting App !!")

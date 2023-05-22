import streamlit as st
import hm_methods as hmm
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Welcome page", page_icon=":house:", layout="wide")
hmm.session_check()
hmm.logout_band()
st.title(':house: Welcome to Hospital Management App')
st.write('Hospital Management App')

#st.write(st.session_state)     #debug
# st.write("DEBUG: reg_name : ", st.session_state.reg_name) #debug
# st.write("DEBUG: urole    : ", st.session_state.urole)    #debug



# st.write("DEBUG: ", st.session_state['urole'])  #debug
# if st.session_state['urole'] == 'admin':
coldoctor, colnurse, colpatient = st.columns(3)
with coldoctor:
    # st.write("DEBUG: Doctor Widget")        #debug
    gotodoctorbtn = st.button("Doctor Widget")
    if gotodoctorbtn:
        switch_page('doctor')

with colnurse:
    # st.write("DEBUG: Nurse Widget")     #debug
    gotonursebtn = st.button("Nurse Widget")
    if gotonursebtn:
        switch_page('nurse')

with colpatient:
    # st.write("DEBUG: Patient Widget")   #debug
    gotopatientbtn = st.button("Patient Widget")
    if gotopatientbtn:
        switch_page('patient')



st.write("""© Evaluation Nerds Mar-2023""" )

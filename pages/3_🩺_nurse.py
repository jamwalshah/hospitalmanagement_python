import streamlit as st
import hm_methods as hmm
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Nurse Manager", page_icon=":stethoscope:", layout="wide")
hmm.session_check()
hmm.logout_band()
st.title(':stethoscope: Nurse Manager')
st.write('Nurse Management Widget')
#st.write(st.session_state)     #debug



tab1, tab2, tab3 = st.tabs(["Insert Nurse's details", "Fetch Nurse's details", "Delete Nurse's details"])
with tab1:
    if st.session_state.urole == 'admin' :
        n_name = st.text_input("Enter Nurse's Name", placeholder="Nurse's Name", key='fmn_name')
        n_age = st.number_input("Enter Nurse's Age", step=1, min_value=20, max_value=60, key='fmn_age')
        n_addr = st.text_input("Enter Nurse's Address", placeholder="Nurse's Address", max_chars=65, key='fmn_addr')
        n_contact = st.text_input("Enter Nurse's contact", placeholder="Nurse's contact", max_chars=10, key='fmn_contact')
        n_msalary = st.number_input("Enter Nurse's Monthly Salary", step=500, min_value=25000, key='fmn_msalary')

        insert_nurse_btn = st.button("Insert Nurse record")
        if insert_nurse_btn:
            hmm.insert_nurse(n_name, n_age, n_addr, n_contact, n_msalary)
    else:
        st.error("You're not allowed to On-board nurse", icon= "🚨")

with tab2:
    if st.session_state.urole == 'admin' or st.session_state.urole == 'manager' or st.session_state.urole == 'receptionist':
        n_id = st.text_input("Enter Nurse's ID to fetch details", placeholder="Nurse's ID", key='fmn_id')
        fetch_nurse_btn = st.button("Fetch Nurse records", key="fmfetch_nurse_btn")
        if fetch_nurse_btn:
            hmm.fetch_nurse(n_id)
    else:
        st.error("You're not allowed to check Nurse details", icon= "🚨")
    
with tab3:
    fetch_all_nurses_btn = st.button("Fetch all nurses", key="fmdfetch_all_nurses_btn")
    if fetch_all_nurses_btn:
        hmm.fetch_all_nurses()
    if st.session_state.urole == 'admin':
        n_id = st.text_input("Enter Nurse's ID to fire🎇 the nurse", placeholder="Nurse's ID", key='fmdn_id')
        fire_nurse_btn = st.button("Fire the Nurse", key="fmdfire_nurse_btn")
        if fire_nurse_btn:    
                hmm.fire_nurse(n_id)
    else:
        st.warning("You're not allowed to Fire Nurse", icon= "🤖")
    

st.write("""© Evaluation Nerds Mar-2023""" )

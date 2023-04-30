import streamlit as st
import hm_methods as hmm
st.set_page_config(page_title="Doctor Manager", page_icon="👨‍⚕️")
st.title('👨‍⚕️ Doctor Manager')
st.write('Doctor Management Widget')

#st.write(st.session_state)     #debug



tab1, tab2, tab3 = st.tabs(["Insert Doctor's details", "Fetch Doctor's details", "Delete Doctor's details"])
with tab1:
    d_name = st.text_input("Enter Doctor's Name", placeholder="Doctor's Name", key='fmd_name')
    d_spec = st.multiselect("Enter Doctor's Specialization", ['General','ENT','Cardiology', 'Neurology', 'Nephrology','Urology','Surgery','Orthopedics','Radiology'], max_selections=1, key='fmd_spec')
    d_age = st.number_input("Enter Doctor's Age", step=1, min_value=25, max_value=60, key='fmd_age')
    d_addr = st.text_input("Enter Doctor's Address", placeholder="Doctor's Address", max_chars=65, key='fmd_addr')
    d_contact = st.text_input("Enter Doctor's contact", placeholder="Doctor's contact", max_chars=10, key='fmd_contact')
    d_fees = st.number_input("Enter Doctor's Fees", step=500, min_value=1000, key='fmd_fees')
    d_msalary = st.number_input("Enter Doctor's Monthly Salary", step=500, min_value=45000, key='fmd_msalary')

    insert_doctor_btn = st.button("Insert Doctor record", key="fminsert_doctor_btn")
    if insert_doctor_btn:
        hmm.insert_doctor(d_name, d_spec[0], d_age, d_addr, d_contact, d_fees, d_msalary)

with tab2:
    d_id = st.text_input("Enter Doctor's ID to fetch details", placeholder="Doctor's ID", key='fmd_id')
    fetch_doctor_btn = st.button("Fetch Doctor records", key="fmfetch_doctor_btn")
    if fetch_doctor_btn:
        hmm.fetch_doctor(d_id)
    
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



st.markdown("""    © Evaluation Nerds Mar-2023""" )

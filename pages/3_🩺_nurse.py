import streamlit as st
import hm_methods as hmm
st.set_page_config(page_title="Nurse Manager", page_icon=":stethoscope:")
st.title(':stethoscope: Nurse Manager')
st.write('Nurse Management Widget')

#st.write(st.session_state)     #debug



tab1, tab2, tab3 = st.tabs(["Insert Nurse's details", "Fetch Nurse's details", "Delete Nurse's details"])
with tab1:
    n_name = st.text_input("Enter Nurse's Name", placeholder="Nurse's Name", key='fmn_name')
    n_age = st.number_input("Enter Nurse's Age", step=1, min_value=20, max_value=60, key='fmn_age')
    n_addr = st.text_input("Enter Nurse's Address", placeholder="Nurse's Address", max_chars=65, key='fmn_addr')
    n_contact = st.text_input("Enter Nurse's contact", placeholder="Nurse's contact", max_chars=10, key='fmn_contact')
    n_msalary = st.number_input("Enter Nurse's Monthly Salary", step=500, min_value=25000, key='fmn_msalary')
    
    insert_nurse_btn = st.button("Insert Nurse record")
    if insert_nurse_btn:
        #st.write(type(d_name)) # str
        #st.write(type(d_spec[0])) # list[str]
        #st.write(type(d_age))  # int
        #st.write(d_name) # str
        #st.write(d_spec[0]) # list
        #st.write(d_age)  # int
        hmm.insert_nurse(n_name, n_age, n_addr, n_contact, n_msalary)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)





st.markdown("""    © Evaluation Nerds Mar-2023""" )

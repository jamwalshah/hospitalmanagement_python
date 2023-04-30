import streamlit as st
import hm_methods as hmm
st.set_page_config(page_title="Patient Manager", page_icon="🛌")
st.title('🛌 Patient Manager')
st.write('Patient Management Widget')

#st.write(st.session_state)     #debug


tab1, tab2, tab3 = st.tabs(["Insert Patient's details", "Fetch Patient's details", "Delete Patient's details"])
with tab1:
    p_name = st.text_input("Enter Patient's Name", placeholder="Patient's Name", key='fmp_name')
    p_gender = st.multiselect("Enter Patient's Gender", ['Male','Female','Others'], max_selections=1, key='fmp_gender')
    p_age = st.number_input("Enter Patient's Age", step=1, min_value=0, max_value=110, key='fmp_age')
    p_addr = st.text_input("Enter Patient's Address", placeholder="Patient's Address", max_chars=65, key='fmp_addr')
    p_contact = st.text_input("Enter Patient's contact", placeholder="Patient's contact", max_chars=10, key='fmp_contact')
    # To-Do add functionality to fetch [{d_id, d_name}] and [{n_id, n_name}] and load in fields below
    # p_d_id = st.multiselect("Enter Patient's Doctor", ['Doc1','Doc2','Doc3','Doc4'], max_selections=1, key='fmp_d_id') 
    # p_n_id = st.multiselect("Enter Patient's Nurse", ['Nur1','Nur2','Nur3','Nur4'], max_selections=1, key='fmp_n_id')
    p_d_id = st.text_input("Enter Patient's Doctor ID", placeholder="Enter valid Doctor ID only", max_chars=65, key='fmp_d_id')
    p_n_id = st.text_input("Enter Patient's Nurse ID", placeholder="Enter valid Nurse ID only", max_chars=65, key='fmp_n_id')

    insert_patient_btn = st.button("Insert Patient record")
    if insert_patient_btn:
        #st.write(type(d_name)) # str
        #st.write(type(d_spec[0])) # list[str]
        #st.write(type(d_age))  # int
        #st.write(d_name) # str
        #st.write(d_spec[0]) # list
        #st.write(d_age)  # int
        hmm.insert_patient(p_name, p_gender[0], p_age, p_addr, p_contact, p_d_id, p_n_id)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



st.markdown("""    © Evaluation Nerds Mar-2023""" )

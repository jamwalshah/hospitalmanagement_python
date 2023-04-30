import streamlit as st
st.set_page_config(page_title="Nurse Manager", page_icon=":stethoscope:")
st.title(':stethoscope: Nurse Manager')
st.write('Nurse Management Widget')

#st.write(st.session_state)     #debug



tab1, tab2, tab3 = st.tabs(["Insert Nurse's details", "Fetch Nurse's details", "Delete Nurse's details"])
with tab1:
    st.text_input("Enter Nurse's Name", placeholder="Nurse's Name", key='n_name')
    st.number_input("Enter Nurse's Age", step=1, min_value=20, max_value=60, key='n_age')
    st.text_input("Enter Nurse's Address", placeholder="Nurse's Address", key='n_addr')
    st.text_input("Enter Nurse's contact", placeholder="Nurse's contact", key='n_contact')
    st.number_input("Enter Nurse's Monthly Salary", step=500, min_value=25000, key='n_msalary')

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)





st.markdown("""    © Evaluation Nerds Mar-2023""" )

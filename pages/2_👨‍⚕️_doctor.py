import streamlit as st
st.set_page_config(page_title="Doctor Manager", page_icon="👨‍⚕️")
st.title('👨‍⚕️ Doctor Manager')
st.write('Doctor Management Widget')

#st.write(st.session_state)     #debug



tab1, tab2, tab3 = st.tabs(["Insert Doctor's details", "Fetch Doctor's details", "Delete Doctor's details"])
with tab1:
    st.text_input("Enter Doctor's Name", placeholder="Doctor's Name", key='d_name')
    st.multiselect("Enter Doctor's Specialization", ['General','ENT','Cardiology', 'Neurology', 'Nephrology','Urology','Surgery','Orthopedics','Radiology'], max_selections=1, key='d_spec')
    st.number_input("Enter Doctor's Age", step=1, min_value=25, max_value=60, key='d_age')
    st.text_input("Enter Doctor's Address", placeholder="Doctor's Address", key='d_addr')
    st.text_input("Enter Doctor's contact", placeholder="Doctor's contact", key='d_contact')
    st.number_input("Enter Doctor's Fees", step=500, min_value=1000, key='d_fees')
    st.number_input("Enter Doctor's Monthly Salary", step=500, min_value=45000, key='d_msalary')

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



st.markdown("""    © Evaluation Nerds Mar-2023""" )

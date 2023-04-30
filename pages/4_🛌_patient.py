import streamlit as st
st.set_page_config(page_title="Patient Manager", page_icon="🛌")
st.title('🛌 Patient Manager')
st.write('Patient Management Widget')

#st.write(st.session_state)     #debug



tab1, tab2, tab3 = st.tabs(["Insert Patient's details", "Fetch Patient's details", "Delete Patient's details"])
with tab1:
    st.text_input("Enter Patient's Name", placeholder="Patient's Name", key='p_name')
    st.multiselect("Enter Patient's Gender", ['Male','Female','Others'], max_selections=1, key='p_gender')
    st.number_input("Enter Patient's Age", step=1, min_value=0, max_value=110, key='p_age')
    st.text_input("Enter Patient's Address", placeholder="Patient's Address", key='p_addr')
    st.text_input("Enter Patient's contact", placeholder="Patient's contact", key='p_contact')
    # To-Do add functionality to fetch [{d_id, d_name}] and [{n_id, n_name}] and load in fields below
    st.multiselect("Enter Patient's Doctor", ['Doc1','Doc2','Doc3','Doc4'], max_selections=1, key='p_d_id') 
    st.multiselect("Enter Patient's Doctor", ['Nur1','Nur2','Nur3','Nur4'], max_selections=1, key='p_n_id')

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



st.markdown("""    © Evaluation Nerds Mar-2023""" )

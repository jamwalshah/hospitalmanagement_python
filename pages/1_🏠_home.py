import streamlit as st
st.set_page_config(page_title="Welcome page", page_icon=":house:")
st.title(':house: Welcome to Hospital Management App')
st.write('Hospital Management App')

#st.write(st.session_state)     #debug



col1, col2, col3, col4 = st.columns(4)
with col1:
    st.success("success message")
with col2:
    st.error("Error message")
with col3:
    st.warning("Warning message")
with col4:
    st.info("info message")
    

st.markdown("""    © Evaluation Nerds Mar-2023""" )

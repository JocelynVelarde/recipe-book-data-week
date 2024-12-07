import streamlit as st

st.title("Find all of your recipes in one page")

search_query = st.text_input("Search for a recipe by name or ingredient")
if search_query:
    st.write({search_query})

    # Example results
    st.write('- Enchildas')
    st.write('- Tacos')
import streamlit as st

st.title("Add a new dish as you wish")

recipe_name = st.text_input("Recipe Name")
ingredients = st.text_area("Ingredients")
instructions = st.text_area("Instructions")
cook_time = st.number_input("Cooking Time", step=1)
difficulty = st.selectbox("Difficulty", ['Easy', 'Medium', 'Hard'])
image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

if st.button("Send recipe"):
    if recipe_name and ingredients and instructions:
        st.success("Recipe was sent correctly")
    else: 
        st.error('Please fill the missing fields')

        


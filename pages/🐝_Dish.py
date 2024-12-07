import streamlit as st

# Page configuration
st.set_page_config(page_title="Add a New Dish", page_icon="🍽️", layout="wide")

# Header
st.title("🍽️ Add a New Dish")
st.subheader("Share your favorite recipes with the community")

# Sidebar
st.sidebar.header("Recipe Submission")
st.sidebar.write("Fill out the form to add a new recipe.")

# Main form
st.markdown("### Recipe Details")

recipe_name = st.text_input("Recipe Name", placeholder="e.g., Spaghetti Carbonara")
ingredients = st.text_area("Ingredients", placeholder="List all ingredients here")
instructions = st.text_area("Instructions", placeholder="Step-by-step cooking instructions")
cook_time = st.number_input("Cooking Time (minutes)", min_value=1, step=1)
difficulty = st.selectbox("Difficulty", ['Easy', 'Medium', 'Hard'])
image = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

# Progress bar
progress = 0
if recipe_name:
    progress += 20
if ingredients:
    progress += 20
if instructions:
    progress += 20
if cook_time:
    progress += 20
if difficulty:
    progress += 10
if image:
    progress += 10

st.progress(progress)

# Submit button
if st.button("Send recipe"):
    if recipe_name and ingredients and instructions:
        st.success("Recipe was sent correctly")
    else: 
        st.error('Please fill the missing fields')

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
import streamlit as st

# Page configuration
st.set_page_config(page_title="Home", page_icon="🍴", layout="wide")

# Header
st.title("🍴 Recipe Book Project")
st.subheader("Discover and share amazing recipes")

# Banner Image
st.image("assets/dish1.jpg", width=200)

# Introduction
st.markdown("### Welcome to the Recipe Book Project")
st.write("This is a nice recipe book to generate cool cooking ideas using AI. Explore a variety of recipes, share your own, and get inspired by others.")

# Call to Action
st.markdown("### Get Started")
st.write("Ready to dive into the world of delicious recipes?")
if st.button("Add a New Recipe"):
    st.write("Navigate to the 'Add Recipe' page to share your culinary creations!")

# Divider
st.divider()

# Featured Recipes
st.markdown("### Featured Recipes")
st.write("Check out some of our most popular recipes:")

rows = 2
columns = 2

for row in range(rows):
    cols = st.columns(columns)
    for col_index, col in enumerate(cols):
        with col:
            container = st.container(border=True)
            with container:
                if row == 0 and col_index == 1:
                    st.write("🍲 **Recipes**")
                    st.write("1. Add new recipes with detailed instructions and images.")
                    st.write("2. Browse through a variety of recipes shared by the community.")
                    st.write("3. Get personalized recipe recommendations based on your preferences.")
                    st.write("4. Rate and review recipes to help others find the best dishes.")
                elif row == 0 and col_index == 0:
                    st.write("🍽️ **Add a New Recipe**")
                    st.write("1. Share your favorite recipes with the community.")
                    st.write("2. Fill out the form with the recipe name, ingredients, and instructions.")
                    st.write("3. Upload an image of the dish to make it visually appealing.")
                    st.write("4. Submit your recipe and inspire others to try it out.")
                elif row == 1 and col_index == 0:
                    st.write("📚 **My Recipe Book**")
                    st.write("1. Save your favorite recipes for easy access.")
                    st.write("2. Organize recipes into categories like breakfast, lunch, dinner, and desserts.")
                    st.write("3. Create a shopping list based on the ingredients of your saved recipes.")
                    st.write("4. Share your recipe book with friends and family.")
                   
                elif row == 1 and col_index == 1:
                    st.write("👀 **Search**")
                    st.write("1. Find recipes by name, ingredient, or category.")
                    st.write("2. Filter recipes by difficulty level, cooking time, and more.")
                    st.write("3. Explore recipes from around the world.")
                    st.write("4. Discover new recipes based on your dietary preferences.")
            
# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
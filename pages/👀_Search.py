import streamlit as st
from pymongo import MongoClient
from urllib.parse import quote_plus

username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['recipe-book']
collection = db['recipes']

# Page configuration
st.set_page_config(page_title="Recipe Finder", page_icon="🍲", layout="wide")

# Header
st.title("🍲 Recipe Finder")
st.subheader("Find all of your recipes in one place")

# Sidebar
st.sidebar.header("Search Filters")
difficulty = st.sidebar.selectbox("Difficulty", ['Any', 'Easy', 'Medium', 'Hard'])
cook_time = st.sidebar.slider("Maximum Cooking Time (minutes)", 0, 120, 60)

# Search bar
search_query = st.text_input("Search for a recipe by name or ingredient", placeholder="e.g., Enchiladas, Chicken")

# Search button
if st.button("Search"):
    query = {}
    if search_query:
        query['$or'] = [
            {"name": {"$regex": search_query, "$options": "i"}},
            {"ingredients": {"$regex": search_query, "$options": "i"}}
        ]
        st.write(f"Searching for recipes with: {search_query}")

    else:
        st.error("Please enter a search query")

    recipes = list(collection.find(query, {"_id": 0, "name": 1, "image": 1, "ingredients": 1, "instructions": 1, "cook_time": 1, "difficulty": 1}))
    if recipes:
        for recipe in recipes:
            st.write(recipe['name'])
            st.write(recipe['ingredients'])
# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
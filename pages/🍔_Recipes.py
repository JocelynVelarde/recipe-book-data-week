import streamlit as st
from urllib.parse import quote_plus
from pymongo import MongoClient
import base64


username = quote_plus(st.secrets["mongo"]["username"])
password = quote_plus(st.secrets["mongo"]["password"])
cluster_url = st.secrets["mongo"]["cluster_url"]

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client['recipe-book']
collection = db['recipes']

# Page configuration
st.set_page_config(page_title="Recipes", page_icon="🍔", layout="wide")

# Header
st.title("🍔 Visualize Your Current Recipes")
st.subheader("Explore the delicious recipes you have added")

recipes = list(collection.find({}, {"name": 1, "image": 1}))

def get_image_base64(binary_image):
    return base64.b64encode(binary_image).decode('utf-8')


# Grid layout for recipes
for i in range(0, len(recipes), 2):
    cols = st.columns(2)
    for col, recipe in zip(cols, recipes[i:i+2]):
        with col:
            image_base64 = get_image_base64(recipe['image'])
            st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px;">
                    <img src="data:image/jpeg;base64, {image_base64}" alt="{recipe['name']}" style="width:100%; border-radius: 10px;">
                    <h3 style="text-align: center;">{recipe['name']}</h3>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
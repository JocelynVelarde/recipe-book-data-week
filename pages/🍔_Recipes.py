import streamlit as st

# Page configuration
st.set_page_config(page_title="Recipes", page_icon="🍔", layout="wide")

# Header
st.title("🍔 Visualize Your Current Recipes")
st.subheader("Explore the delicious recipes you have added")

# Sample recipes data
recipes = [
    {"name": "Chile en Nogada", "image": "https://www.tastingtable.com/img/gallery/traditional-mexican-dishes/l-intro-1683731770.jpg"},
    {"name": "Enfrijoladas", "image": "https://blog.amigofoods.com/wp-content/uploads/2020/12/enfrijoladas-mexican-food.jpg"},
    {"name": "Pozole", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnlTy5mUhFTAeDonihkTM2plqukb-1iLekwQ&s"},
    {"name": "Tamales", "image": "https://media.cnn.com/api/v1/images/stellar/prod/230321110034-03-body-mexican-foods-tamales.jpg?q=w_1110,c_fill"},
]

# Grid layout for recipes
for i in range(0, len(recipes), 2):
    cols = st.columns(2)
    for col, recipe in zip(cols, recipes[i:i+2]):
        with col:
            st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px;">
                    <img src="{recipe['image']}" alt="{recipe['name']}" style="width:100%; border-radius: 10px;">
                    <h3 style="text-align: center;">{recipe['name']}</h3>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
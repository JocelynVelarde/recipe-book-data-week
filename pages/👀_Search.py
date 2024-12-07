import streamlit as st

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
    if search_query:
        st.write(f"Searching for recipes with: {search_query}")
        
        # Example results
        st.markdown("### Search Results")
        st.write("- **Enchiladas**")
        st.write("- **Tacos**")
        st.write("- **Chicken Curry**")
        st.write("- **Pasta Alfredo**")
    else:
        st.error("Please enter a search query")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
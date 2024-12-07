import streamlit as st

st.title("Visualize your current recipes")

recipes = [
    {"name": "Enchiladas", "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmasdemx.com%2Fwp-content%2Fuploads%2F2016%2F04%2FVM0402H_chicken-enchiladas_s4x3.jpg&f=1&nofb=1&ipt=8489ab4326812aa082c4ec06c13e5516858dcbffef936a0587dea7d70c4cc89f&ipo=images"},
    {"name": "Tacos", "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmasdemx.com%2Fwp-content%2Fuploads%2F2016%2F04%2FVM0402H_chicken-enchiladas_s4x3.jpg&f=1&nofb=1&ipt=8489ab4326812aa082c4ec06c13e5516858dcbffef936a0587dea7d70c4cc89f&ipo=images"},
    {"name": "Sopes", "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmasdemx.com%2Fwp-content%2Fuploads%2F2016%2F04%2FVM0402H_chicken-enchiladas_s4x3.jpg&f=1&nofb=1&ipt=8489ab4326812aa082c4ec06c13e5516858dcbffef936a0587dea7d70c4cc89f&ipo=images"},
    {"name": "Empanadas", "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmasdemx.com%2Fwp-content%2Fuploads%2F2016%2F04%2FVM0402H_chicken-enchiladas_s4x3.jpg&f=1&nofb=1&ipt=8489ab4326812aa082c4ec06c13e5516858dcbffef936a0587dea7d70c4cc89f&ipo=images"}
]

for recipe in recipes:
    col = st.columns([1, 2])
    with col[0]:
        st.image(recipe["image"], width=100)
    with col[1]:
        st.subheader(recipe["name"])
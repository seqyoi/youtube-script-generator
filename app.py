import streamlit as st
from script_generator import generate_script

st.title("YouTube Script Generator")

topic = st.text_input("Enter video topic")
tone = st.selectbox("Select tone", ["Informative", "Casual", "Funny", "Motivational"])
duration = st.slider("Video length (minutes)", 1, 10, 5)

if st.button("Generate Script"):
    if topic:
        with st.spinner("Generating..."):
            script = generate_script(topic, tone, duration)
            st.subheader("Generated Script")
            st.write(script)
    else:
        st.warning("Please enter a topic")
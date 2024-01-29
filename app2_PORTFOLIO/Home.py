import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Emanuel Lopez")
    content = """
        Hi, I am Emanuel Lopez, I am a Pythom programmer, Web Developer and Data Analist. I graduated in 2025 with a GPA of 3.7.
        I have worked in several companies, developing web apps and now i learning how to be a Software Engineer in order to get a job
        in a FAANG.
    """
    st.info(content)

st.write(
    "Below you can find some of the apps I have build in Python. Feel free to contact me!"
)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

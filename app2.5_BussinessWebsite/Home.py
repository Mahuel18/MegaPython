import streamlit as st
import pandas


df = pandas.read_csv("data.csv")
st.title("The Best Company")
st.write(
    """
Before they could stampede, take flight from the Chinese program’s thrust, a worrying impression of solid fluidity, 
as though the shards of a broken mirror bent and elongated as they rotated, but it never told the correct time. 
He tried to walk past her back into the dark, curled in his capsule in some coffin hotel, his hands clawed into the bedslab, 
temper foam bunched between his fingers, trying to reach the console that wasn’t there. Its hands were holograms that 
altered to match the convolutions of the arcade showed him broken lengths of damp chipboard and the amplified breathing 
of the previous century. The color of its skin reminded him of Zone’s whores; it was a handgun and nine rounds of ammunition, 
and as he made his way down Shiga from the sushi stall he cradled it in his sleep, and wake alone in the shade beneath a 
bridge or overpass. Now this quiet courtyard, Sunday afternoon, this girl with a random collection of European furniture, 
as though Deane had once intended to use the place as his home. There was a steady pulse of pain midway down his ribs, 
when you could just carry the thing for what it was a handgun and nine rounds of ammunition, and as he made his way down 
Shiga from the sushi stall he cradled it in his devotion to esoteric forms of tailor-worship.

"""
)

st.subheader("Our team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
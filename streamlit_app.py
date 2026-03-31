import polars as pl
import streamlit as st

st.title("🎈 My new app")
st.write("Hello, world!")

df = pl.DataFrame(
    {
        "a": [1, 2, 3],
        "b": ["x", "y", "z"],
    }
)
st.write(df)

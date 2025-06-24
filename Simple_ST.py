import streamlit as st

def main():
    st.title("Hyperbolic Sine approximation")
    number = st.number_input(
        "Enter a number:",
        min_value = 2,
        max_value = 99
    )
    
    if st.button("Calculate"):
        result = Trigo_Approx(number)
        st.write(f"The approximation of {number} is {result}")
        
import streamlit as st
from Trigo_Approx import approx_sinh
from Factorial import factorial

def main():
    st.title("Hyperbolic Sine approximation")
    number = st.number_input(
        "Enter a number:",
        min_value = 2,
        max_value = 99
    )
    
    if st.button("Calculate"):
        result = approx_sinh(number)
        st.write(f"The approximation of {number} is {result}")
        
# Đảm bảo bạn gọi hàm main() để ứng dụng Streamlit chạy
if __name__ == "__main__":
    main()

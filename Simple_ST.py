import streamlit as st
from Trigo_Approx import approx_sinh
from Factorial import factorial

def main():
    st.title("Hyperbolic Sine approximation")
    number = st.slider(
        "Enter a number:",
        min_value=2,
        max_value=99,
        value=2
    )

    nums = st.slider(
        "Enter a number of loop:",
        min_value=10,
        max_value=1000,
        value=2
    )
    
    if st.button("Calculate"):
        result = approx_sinh(number, nums)
        st.write(f"The approximation of {number} is {result}")
        
# Đảm bảo bạn gọi hàm main() để ứng dụng Streamlit chạy
if __name__ == "__main__":
    main()

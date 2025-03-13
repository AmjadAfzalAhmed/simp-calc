import streamlit as st

# Custom theme configuration
st.set_page_config(
    page_title="A Simple Calculator",
    page_icon="🧮",
    layout="centered",
)

st.markdown("""
    <style>
    * {
        font-family: 'Big Shoulders', cursive !important;
        color: blue !important;
    }
    
    .stApp {
        background-color: #FFE53B;
        background-image: linear-gradient(147deg, #FFE53B 0%, #FF2525 74%);
    }
    
    h1 {
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }
    
    .stButton>button {
        width: 100%;
        border: 2px solid #4CAF50 !important;
        background-color: #45a049 !important;
        padding: 15px 32px;
        text-align: center;
        font-size: 16px;
        border-radius: 12px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #4CAF50 !important;
        transform: scale(1.05);
    }
    
    /* result container */
    .result-box {
        background: linear-gradient(135deg, #e0f7fa, #80deea);
        border-left: 5px solid dodgerblue;
        border-right: 5px solid dodgerblue;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        font-size: 20px;
        color: #000;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders:opsz,wght@10..72,100..900&display=swap" rel="stylesheet">', unsafe_allow_html=True)

def main():
    st.title("🧮 Simple Calculator")

    # Input fields arranged in two columns
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
    
    # Operation selection 
    operation = st.selectbox("Select operation", ["Addition(+)", "Subtraction(-)", "Multiplication(x)", "Division(/)"])

    # Perform calculation when the button is clicked
    if st.button("Calculate"):
        try:
            if operation == "Addition(+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction(-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication(x)":
                result = num1 * num2
                symbol = "x"
            else:
                if num2 == 0:
                    st.error("Error: Division by Zero!")
                    return
                result = num1 / num2
                symbol = "/"

            # Show the result in a fancy container with gradient and dodgerblue borders
            st.markdown(f"""
                <div class="result-box">
                    <h2>{num1} {symbol} {num2} = {result:.4f}</h2>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        except Exception as e:
                st.error(f"An Error occured : {e}")


if __name__ == "__main__":
    main()

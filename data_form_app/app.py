import streamlit as st

st.title("Hello World")
st.header("This is header")

st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
        color: gray;
    }
    </style>
    """, unsafe_allow_html=True)

with st.container():
    user_input = st.text_input("Enter your Name:")
    user_input_f = st.text_input("Enter your Father Name:")
    user_input_age = st.text_input("Enter your Age:")
    user_input_religion = st.text_input("Enter your Religion:")
    user_input_box = st.selectbox("Enter your class:", ["1th", "2th", "3th", "4th", "5th", "6th", "7th", "8th", "9th", "10th"])
    gender = st.radio("Select Gender:", ["Male", "Female"])


st.write("Debug Info (Current Values):")
st.write(f"Name length: {len(user_input)}")
st.write(f"Father Name length: {len(user_input_f)}")
st.write(f"Age length: {len(user_input_age)}")
st.write(f"Education length: {len(user_input_religion)}")

if st.button("Submit", type="primary"):
    st.success("Form Submitted Successfully!")
    st.markdown(f"""
    ### 📋 Your Data
    ----------------------------------------
    **👤 Name:** {user_input}  
    **👨 Father Name:** {user_input_f}  
    **🎂 Age:** {user_input_age}  
    **🎓 Religion:** {user_input_religion}  
    **🏫 Class:** {user_input_box}  
    **⚧ Gender:** {gender}
    ----------------------------------------
    """)

    
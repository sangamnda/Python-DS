import streamlit as st
# streamlit ko run krne ke liye terminal me command run krna hoga "streamlit run calculator.py"

st.title('Simple Calculator')
# st.subheader('This is a basic streamlit application')
# st.markdown('This is a basic streamlit application')

# fnum = st.number_input('Enter the first number', value = 0)
# snum = st.number_input('Enter the second number', value = 0)

c1, c2 = st.columns(2)
fnum = c1.number_input('Enter the first number', value = 0)
snum = c2.number_input('Enter the second number', value = 0)

st.subheader('Options')
choice = ['Add', 'Sub', 'Mul', 'Div']
option = st.radio('Select any one Operaion', choice)

button = st.button('Calculate')

result = 0
if button:
 
    if option == 'Add':
        result = fnum + snum
    if option == 'Sub':
        result = fnum - snum
    if option == 'Mul':
        result = fnum * snum
    if option == 'Div':
        result = fnum / snum
        
st.success(f"result is {result}")
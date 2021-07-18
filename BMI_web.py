#streamlit run BMI_web.py
import streamlit as st
st.header(' **_BMI計算_**.:sunglasses:')
h = st.number_input('請輸入身高(cm):',value=160,step=5)
w = st.number_input('請輸入體重(kg):',value=60,step=5)
#waist = st.number_input('請輸入腰圍(cm):',value=30,step=5)
gender = st.radio('', ('男性', '女性'))
waist = st.slider('腰圍(吋):', 10, 120, 20)
#gender=st.selectbox('',('男性', '女性'))
st.write('你的性別是:',gender)                    
if st.button('點我>>>BMI計算'):
    
    BMI = w / (h/100) ** 2

    st.write('BMI='+ str(round(BMI, 2)))
    a=BMI
    if a >30 and waist >50:
        st.write('胖子注意,你擁有',waist,'的水桶腰,BMI太大異常,快快減肥去!')
    elif a >25 and waist >40 and gender=='男性':
        st.write('嗨~man~你擁有',waist,'的腰身,BMI偏高異常,飲食該節制了~快點運動運動')
    elif a >25 and waist >35 and gender=='女性':
        st.write('嗨~美女~你擁有',waist,'的腰身,BMI偏高異常,飲食該節制了~快點運動運動')
    elif a >25 and 25<=waist <35 and gender=='男性':
        st.write('嗨~man~你擁有',waist,'的腰身還算正常,但是BMI偏高異常,飲食該節制了~快點運動運動')  
    elif a >25 and 25<=waist <35 and gender=='女性':
        st.write('嗨~正妹~你擁有',waist,'的腰身頗粗,但是BMI偏高異常,飲食該節制了~快點運動運動') 
    elif a <25 and waist >50:
        st.write('嗨~BMI正常,但是腰圍',waist,'腰很粗趕快起來扭腰運動')
    elif a <25 and 25<=waist <35 and gender=='男性':
        st.write('嗨~man,你的BMI正常,身材適中,好好維持喔')
    elif a <25 and 25<=waist <35 and gender=='女性':
        st.write('嗨~正妹,你的BMI正常,身材適中~~請加油努力往水蛇腰邁進喔~')
    elif a <25 and waist <25 and gender=='女性':
        st.write('嗨~正妹,你的BMI正常,身材也不錯喔~')
    else:
        st.write('嗨~帥哥,你的BMI正常~身材也不錯喔')
#option = st.selectbox(
#...     'How would you like to be contacted?',
#...     ('Email', 'Home phone', 'Mobile phone'))
#>>>
#>>> st.write('You selected:', option)
#st.markdown('Streamlit is **_really_ cool**.')

import streamlit as st

# Initialize session state for HSK progress tracking
if 'hsk_completed' not in st.session_state:
    st.session_state.hsk_completed = {
        'hsk1': False,
        'hsk2': False,
        'hsk3': False,
        'hsk4': False,
        'hsk5': False
    }

st.title("🎓 HSK 5 - Advanced Fluency")
st.subheader("Mastery level - You're almost native!")

st.write("HSK 5 represents near-native proficiency.")

st.info("Content coming soon...")

# Completion Section
st.subheader("✅ Mark as Completed")

st.write("Congratulations on reaching HSK 5! This is the highest level of Mandarin proficiency.")

if st.button("🎉 I have completed HSK 5!", type="primary", use_container_width=True):
    st.session_state.hsk_completed['hsk5'] = True
    st.success("🏆 INCREDIBLE! You have mastered HSK 5! You are now fluent in Mandarin Chinese!")
    st.balloons()

# Current Status
if st.session_state.hsk_completed['hsk5']:
    st.success("✅ HSK 5 Status: **COMPLETED** - You are a Mandarin master!")
else:
    st.info("📚 HSK 5 Status: **IN PROGRESS**")

# Navigation
st.subheader("🚀 Congratulations!")
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Back to HSK 4", use_container_width=True):
        st.switch_page("pages/8_HSK_4.py")

with col2:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("streamlit_app.py")

# Achievement Celebration
if st.session_state.hsk_completed['hsk5']:
    st.subheader("🎖️ Achievement Unlocked!")
    st.write("**🏆 HSK 5 MASTER**")
    st.write("You can now:")
    st.write("• ✅ Understand TV shows and movies in Mandarin")
    st.write("• ✅ Read Chinese newspapers and books")
    st.write("• ✅ Write formal documents and essays")
    st.write("• ✅ Engage in sophisticated conversations")
    st.write("• ✅ Communicate fluently in academic/professional settings")

    st.success("🎊 You have achieved the highest level of Mandarin proficiency! 恭喜! (Congratulations!)")
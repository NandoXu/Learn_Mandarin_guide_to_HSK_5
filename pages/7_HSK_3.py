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

st.title("🎓 HSK 3 - Intermediate Level")
st.subheader("Expanding your communication skills!")

st.write("HSK 3 focuses on practical communication.")

st.info("Content coming soon...")

# Completion Section
st.subheader("✅ Mark as Completed")

st.write("When you've mastered HSK 3 concepts, mark this level as complete to unlock HSK 4!")

if st.button("🎉 I have completed HSK 3!", type="primary", use_container_width=True):
    st.session_state.hsk_completed['hsk3'] = True
    st.success("🎊 Congratulations! HSK 3 completed! HSK 4 is now unlocked.")
    st.balloons()

# Current Status
if st.session_state.hsk_completed['hsk3']:
    st.success("✅ HSK 3 Status: **COMPLETED**")
else:
    st.info("📚 HSK 3 Status: **IN PROGRESS**")

# Navigation
st.subheader("🚀 Next Steps")
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Back to HSK 2", use_container_width=True):
        st.switch_page("pages/6_HSK_2.py")

with col2:
    if st.session_state.hsk_completed['hsk3']:
        if st.button("➡️ Continue to HSK 4", use_container_width=True):
            st.switch_page("pages/8_HSK_4.py")
    else:
        st.button("🔒 HSK 4 (Complete HSK 3 first)", disabled=True, use_container_width=True)
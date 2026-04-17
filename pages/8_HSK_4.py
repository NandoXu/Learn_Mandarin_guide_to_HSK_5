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

st.title("🎓 HSK 4 - Upper Intermediate")
st.subheader("Mastering complex expressions!")

st.write("HSK 4 requires understanding of complex sentences and abstract concepts.")

st.info("Content coming soon...")

# Completion Section
st.subheader("✅ Mark as Completed")

st.write("When you've mastered HSK 4 concepts, mark this level as complete to unlock HSK 5!")

if st.button("🎉 I have completed HSK 4!", type="primary", use_container_width=True):
    st.session_state.hsk_completed['hsk4'] = True
    st.success("🎊 Congratulations! HSK 4 completed! HSK 5 is now unlocked.")
    st.balloons()

# Navigation
st.subheader("🚀 Next Steps")
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Back to HSK 3", use_container_width=True):
        st.switch_page("pages/7_HSK_3.py")

with col2:
    if st.session_state.hsk_completed['hsk4']:
        if st.button("➡️ Continue to HSK 5", use_container_width=True):
            st.switch_page("pages/9_HSK_5.py")
    else:
        st.button("🔒 HSK 5 (Complete HSK 4 first)", disabled=True, use_container_width=True)
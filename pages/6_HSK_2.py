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

st.title("🎓 HSK 2 - Elementary Level")
st.subheader("Building on your foundation!")

st.write("HSK 2 introduces more vocabulary and basic sentence patterns.")

st.info("Content coming soon...")

# Completion Section
st.subheader("✅ Mark as Completed")

st.write("When you've mastered HSK 2 concepts, mark this level as complete to unlock HSK 3!")

if st.button("🎉 I have completed HSK 2!", type="primary", use_container_width=True):
    st.session_state.hsk_completed['hsk2'] = True
    st.success("🎊 Congratulations! HSK 2 completed! HSK 3 is now unlocked.")
    st.balloons()

# Navigation
st.subheader("🚀 Next Steps")
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Back to HSK 1", use_container_width=True):
        st.switch_page("pages/1_HSK_1.py")

with col2:
    if st.session_state.hsk_completed['hsk2']:
        if st.button("➡️ Continue to HSK 3", use_container_width=True):
            st.switch_page("pages/7_HSK_3.py")
    else:
        st.button("🔒 HSK 3 (Complete HSK 2 first)", disabled=True, use_container_width=True)
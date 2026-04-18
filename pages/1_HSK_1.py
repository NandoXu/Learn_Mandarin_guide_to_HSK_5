
import streamlit as st

# Initialize session state for HSK progress tracking
# if 'hsk_completed' not in st.session_state:
#     st.session_state.hsk_completed = {
#         'hsk1': False,
#         'hsk2': False,
#         'hsk3': False,
#         'hsk4': False,
#         'hsk5': False
#     }

st.title("🎓 HSK 4 - Upper Intermediate")
st.subheader("Mastering complex expressions!")


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

st.title("🎓 HSK 1 - Beginner Level")
st.subheader("Welcome to your Mandarin learning journey!")

st.write("HSK 1 is the foundation level. You'll learn basic greetings, numbers, and simple sentences.")

st.info("Content coming soon...")

# Completion Section
st.subheader("✅ Mark as Completed")

st.write("When you've mastered the basics of HSK 1, mark this level as complete to unlock HSK 2!")

if st.button("🎉 I have completed HSK 1!", type="primary", use_container_width=True):
    st.session_state.hsk_completed['hsk1'] = True
    st.success("🎊 Congratulations! HSK 1 completed! HSK 2 is now unlocked.")
    st.balloons()

# Navigation
st.subheader("🚀 Next Steps")
if st.session_state.hsk_completed['hsk1']:
    if st.button("➡️ Continue to HSK 2", use_container_width=True):
        st.switch_page("pages/6_HSK_2.py")
else:
    st.button("🔒 HSK 2 (Complete HSK 1 first)", disabled=True, use_container_width=True)
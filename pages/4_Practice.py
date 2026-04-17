import streamlit as st
import random

st.title("🎯 Practice Exercises")
st.subheader("Test your HSK 5 knowledge")

st.write("Interactive exercises to help you practice and reinforce your learning.")

# Exercise 1: Vocabulary Quiz
st.subheader("📝 Vocabulary Quiz")

vocab_questions = [
    {"question": "What does '会议' mean?", "options": ["meeting", "contract", "manager", "development"], "answer": "meeting"},
    {"question": "What does '环境' mean?", "options": ["environment", "pollution", "protection", "climate"], "answer": "environment"},
    {"question": "What does '研究' mean?", "options": ["research", "degree", "course", "knowledge"], "answer": "research"},
    {"question": "What does '投资' mean?", "options": ["meeting", "contract", "investment", "development"], "answer": "investment"}
]

if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_attempted' not in st.session_state:
    st.session_state.quiz_attempted = False

col1, col2 = st.columns(2)

with col1:
    selected_answers = []
    for i, q in enumerate(vocab_questions):
        answer = st.radio(f"**{q['question']}**", q['options'], key=f"q{i}")
        selected_answers.append(answer)

    if st.button("Check Answers"):
        correct = 0
        for i, (q, answer) in enumerate(zip(vocab_questions, selected_answers)):
            if answer == q['answer']:
                correct += 1
        st.session_state.quiz_score = correct
        st.session_state.quiz_attempted = True

with col2:
    if st.session_state.quiz_attempted:
        score_percentage = (st.session_state.quiz_score / len(vocab_questions)) * 100
        st.metric("Your Score", f"{st.session_state.quiz_score}/{len(vocab_questions)}", f"{score_percentage:.1f}%")

        if score_percentage >= 80:
            st.success("🎉 Excellent! You're ready for HSK 5!")
        elif score_percentage >= 60:
            st.warning("👍 Good job! Keep practicing.")
        else:
            st.error("📚 Keep studying! You can do it!")

# Exercise 2: Sentence Building
st.subheader("🔨 Sentence Builder")

st.write("Build sentences using the correct grammar patterns:")

sentence_parts = {
    "subject": ["我", "他", "我们", "他们"],
    "verb": ["学习", "工作", "吃饭", "睡觉"],
    "object": ["中文", "作业", "会议", "合同"],
    "time": ["昨天", "今天", "明天", "现在"]
}

col1, col2, col3, col4 = st.columns(4)

with col1:
    subject = st.selectbox("Subject (主语)", sentence_parts["subject"])
with col2:
    verb = st.selectbox("Verb (动词)", sentence_parts["verb"])
with col3:
    obj = st.selectbox("Object (宾语)", sentence_parts["object"])
with col4:
    time = st.selectbox("Time (时间)", sentence_parts["time"])

if st.button("Build Sentence"):
    sentence = f"{time}{subject}{verb}{obj}"
    st.success(f"**Your sentence:** {sentence}")
    st.info("💡 This follows the basic SVO (Subject-Verb-Object) word order in Chinese!")

# Exercise 3: Reading Comprehension
st.subheader("📖 Reading Practice")

reading_text = """
在中国，环境保护越来越重要。政府出台了很多政策来保护环境。
比如，减少污染、节约资源、保护野生动物等。每个人都应该参与环境保护。
"""

st.write("**Read the following text:**")
st.write(reading_text)

comprehension_questions = [
    "What is becoming more important in China?",
    "What policies has the government introduced?",
    "What should everyone do?"
]

for i, question in enumerate(comprehension_questions):
    answer = st.text_input(f"Question {i+1}: {question}", key=f"comp_q{i}")
    if answer:
        st.write("✅ Answer recorded!")

st.info("🎓 These exercises will help you prepare for the HSK 5 exam. Practice regularly!")
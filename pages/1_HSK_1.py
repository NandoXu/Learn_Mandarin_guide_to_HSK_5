import streamlit as st

st.title("🎓 HSK 1 - Beginner Level")
st.subheader("Welcome to your Mandarin learning journey!")

st.write("HSK 1 is the foundation level. You'll learn basic greetings, numbers, and simple sentences.")

# Basic Vocabulary
st.subheader("📝 Basic Vocabulary")

basic_vocab = {
    "Greetings": [
        "你好 (nǐ hǎo) - Hello",
        "谢谢 (xiè xiè) - Thank you",
        "不客气 (bú kè qì) - You're welcome",
        "再见 (zài jiàn) - Goodbye"
    ],
    "Numbers": [
        "一 (yī) - One",
        "二 (èr) - Two",
        "三 (sān) - Three",
        "四 (sì) - Four",
        "五 (wǔ) - Five"
    ],
    "Family": [
        "爸爸 (bà ba) - Father",
        "妈妈 (mā ma) - Mother",
        "哥哥 (gē ge) - Older brother",
        "姐姐 (jiě jie) - Older sister"
    ]
}

for category, words in basic_vocab.items():
    with st.expander(f"📖 {category}"):
        for word in words:
            st.write(f"• {word}")

# Basic Grammar
st.subheader("🔤 Basic Grammar")

st.write("**Subject + Verb + Object**")
st.info("Example: 我吃苹果 (I eat apple)")

st.write("**是 (shì) - To be**")
st.info("Example: 我是学生 (I am a student)")

# Practice Section
st.subheader("🎯 Practice Time")

st.write("Try these simple exercises:")

# Exercise 1: Greetings
st.write("**1. Match the English to Chinese:**")
greetings_quiz = {
    "Hello": "你好",
    "Thank you": "谢谢",
    "Goodbye": "再见"
}

for english, chinese in greetings_quiz.items():
    answer = st.text_input(f"What is '{english}' in Chinese?", key=f"greet_{english}")
    if answer:
        if answer.strip() == chinese:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Try again. Hint: {chinese}")

# Exercise 2: Numbers
st.write("**2. Count from 1-5:**")
numbers = ["一", "二", "三", "四", "五"]
user_numbers = []
for i in range(5):
    num = st.text_input(f"Number {i+1}:", key=f"num_{i}")
    user_numbers.append(num)

if st.button("Check Numbers"):
    correct = 0
    for i, (user_num, correct_num) in enumerate(zip(user_numbers, numbers)):
        if user_num.strip() == correct_num:
            correct += 1
    st.metric("Score", f"{correct}/5")

# Next Steps
st.subheader("🚀 Next Steps")

st.info("""
Great job starting your Mandarin journey! 🎉

**What's next:**
- Practice these words daily
- Try speaking them out loud
- Move to HSK 2 when you're comfortable

Remember: Consistency is key! Practice a little every day.
""")

if st.button("🎯 Ready for HSK 2?"):
    st.success("Coming soon! Keep practicing HSK 1 first.")
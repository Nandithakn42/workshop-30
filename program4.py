# pip install streamlit groq python-dotenv
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY is missing. Please add it to your .env file.")
    st.stop()

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-20b"

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Study Assistant")
st.write("Learn any topic with Generative AI!")

topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Python Lists"
)

difficulty = st.selectbox(
    "Choose difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

option = st.selectbox(
    "What do you want AI to do?",
    [
        "Explain",
        "Summarize",
        "Generate Quiz",
        "Give Real-World Examples"
    ]
)

if st.button("Generate", type="primary"):
    
    if not topic.strip():
        st.warning("Please enter a topic.")
    
    else:
        prompt = f"""
Topic: {topic}
Difficulty: {difficulty}
Task: {option}

Explain everything clearly using simple language.
Follow these instructions:

If explaining:
- Give a simple definition
- Give 3 key points
- Give one real-world example

If summarizing:
- Give a short summary
- Give the most important points
- Use simple language

If generating a quiz:
- Create 5 multiple-choice questions
- Give 4 options for each question
- Give the correct answer
- Give a short explanation for each answer

If giving real-world examples:
- Give at least 3 practical examples
- Explain each example clearly
- Relate the examples to everyday life when possible.
"""

        with st.spinner("🤖 AI is thinking..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a friendly, clear, and helpful AI study assistant."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7
                )

                answer = response.choices[0].message.content

                st.subheader("📚 AI Response")
                st.write(answer)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
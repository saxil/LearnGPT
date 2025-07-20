import streamlit as st
import json
import os
import sys

# Define project root and add it to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PROJECT_ROOT)

from llm.tutor_agent import create_vectorstore, get_tutor_chain

@st.cache_data
def load_module(module_name):
    """Load module content and quiz from files."""
    module_path = os.path.join(PROJECT_ROOT, "modules", f"{module_name}.md")
    quiz_path = os.path.join(PROJECT_ROOT, "quizzes", f"{module_name}.json")

    with open(module_path, "r", encoding="utf-8") as f:
        module_content = f.read()

    with open(quiz_path, "r", encoding="utf-8") as f:
        quiz_data = json.load(f)

    return module_content, quiz_data

@st.cache_resource
def get_tutor(module_path):
    """Get the AI tutor chain."""
    vectorstore = create_vectorstore(module_path)
    return get_tutor_chain(vectorstore)

def main():
    st.title("LearnGPT")

    # Module selection
    st.sidebar.title("Modules")
    modules_dir = os.path.join(PROJECT_ROOT, 'modules')
    module_files = [f.split(".")[0] for f in os.listdir(modules_dir) if f.endswith(".md")]
    selected_module = st.sidebar.selectbox("Choose a module", module_files)

    if selected_module:
        module_content, quiz_data = load_module(selected_module)

        # Display module content
        st.markdown(module_content)

        # Display quiz
        st.header("Quiz")
        user_answers = {}
        for i, q in enumerate(quiz_data["questions"]):
            st.subheader(f"Question {i+1}: {q['question']}")
            user_answers[i] = st.radio(f"Options for Question {i+1}", q["options"], key=f"q{i}_{selected_module}")

        if st.button("Submit Quiz"):
            score = 0
            for i, q in enumerate(quiz_data["questions"]):
                if user_answers[i] == q["answer"]:
                    score += 1
            
            st.success(f"Your score: {score}/{len(quiz_data['questions'])}")
            if score == len(quiz_data['questions']):
                st.balloons()
                st.success("Congratulations! You passed the quiz.")
            else:
                st.error("You did not pass the quiz. Please review the material and try again.")

        # AI Tutor
        st.header("AI Tutor")
        qa_chain = get_tutor(os.path.join(modules_dir))

        user_question = st.text_input("Ask the tutor a question:")
        if user_question:
            answer = qa_chain.invoke(user_question)
            st.write(answer['result'])

if __name__ == "__main__":
    main()

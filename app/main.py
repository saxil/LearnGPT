import streamlit as st
import json
import os

def load_module(module_name):
    """Load module content and quiz from files."""
    base_path = os.path.join(os.getcwd())
    module_path = os.path.join(base_path, "modules", f"{module_name}.md")
    quiz_path = os.path.join(base_path, "quizzes", f"{module_name}.json")

    with open(module_path, "r") as f:
        module_content = f.read()

    with open(quiz_path, "r") as f:
        quiz_data = json.load(f)

    return module_content, quiz_data

def main():
    st.title("LearnGPT")

    # Module selection
    st.sidebar.title("Modules")
    module_files = [f.split(".")[0] for f in os.listdir("modules") if f.endswith(".md")]
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
            user_answers[i] = st.radio(f"Options for Question {i+1}", q["options"], key=f"q{i}")

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


if __name__ == "__main__":
    main()

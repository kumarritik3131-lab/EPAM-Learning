# app.py
# Main Streamlit Graphical Interface for AI Study Buddy

import streamlit as st
from learning_content import PYTHON_TOPICS, AI_TOPICS
from quiz import get_all_questions, calculate_score
from agent import run_agent

# Page configuration
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------------------------------------
# Sidebar Navigation
# -------------------------------------------------------------
st.sidebar.title("🎓 AI Study Buddy")
st.sidebar.caption("EPAM Learning Program • Beginner Project")

nav_choice = st.sidebar.radio(
    "Choose a Section:",
    [
        "🏠 Welcome Page",
        "🐍 Python Learning",
        "🧠 AI Foundations",
        "📝 AI Quiz",
        "🤖 Rule-Based AI Agent"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "💡 **Beginner Note:** This app demonstrates core Python programming, "
    "AI fundamentals, and a simple 3-tool rule-based AI agent without external APIs."
)


# -------------------------------------------------------------
# Section 1: Welcome Page
# -------------------------------------------------------------
if nav_choice == "🏠 Welcome Page":
    st.title("Welcome to AI Study Buddy! 🚀")
    st.subheader("Your simple, interactive companion for Python and AI Foundations")
    
    st.markdown("""
    Welcome to **AI Study Buddy**! This application was created to demonstrate basic Python programming, 
    fundamental AI concepts, and how an AI agent works behind the scenes.
    
    ### 📌 What you can explore:
    - **🐍 Python Learning:** Learn basic programming building blocks with clear explanations and runnable code snippets.
    - **🧠 AI Foundations:** Understand terms like AI, ML, Deep Learning, GenAI, LLMs, and Neural Networks with simple definitions and real-world examples.
    - **📝 AI Quiz:** Test your knowledge with a 10-question multiple-choice quiz and get immediate scoring and explanations.
    - **🤖 Rule-Based AI Agent:** See how an AI agent takes user input, detects the intent, selects a tool, and executes it.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✨ **100% Local & Beginner Friendly**\nNo databases, paid APIs, or complex frameworks.")
    with col2:
        st.info("🎯 **Clear Architecture**\nBuilt with clean Python files (`learning_content.py`, `quiz.py`, `agent.py`, `app.py`).")


# -------------------------------------------------------------
# Section 2: Python Learning
# -------------------------------------------------------------
elif nav_choice == "🐍 Python Learning":
    st.title("🐍 Python Learning")
    st.write("Explore core Python concepts with beginner-friendly explanations and simple code snippets.")
    
    selected_python_topic = st.selectbox(
        "Select a Python Topic to Study:",
        list(PYTHON_TOPICS.keys())
    )
    
    topic_data = PYTHON_TOPICS[selected_python_topic]
    
    st.subheader(f"📌 {selected_python_topic}")
    st.write(topic_data["explanation"])
    
    st.markdown("#### 💻 Code Example:")
    st.code(topic_data["code_example"], language="python")


# -------------------------------------------------------------
# Section 3: AI Foundations
# -------------------------------------------------------------
elif nav_choice == "🧠 AI Foundations":
    st.title("🧠 AI Foundations")
    st.write("Understand foundational concepts in Artificial Intelligence with everyday analogies and examples.")
    
    selected_ai_topic = st.selectbox(
        "Select an AI Concept to Explore:",
        list(AI_TOPICS.keys())
    )
    
    ai_data = AI_TOPICS[selected_ai_topic]
    
    st.subheader(f"🔍 {selected_ai_topic}")
    
    st.markdown("**📖 Definition:**")
    st.info(ai_data["definition"])
    
    st.markdown("**🌍 Real-Life Example:**")
    st.success(ai_data["real_life_example"])
    
    st.markdown("**💡 Explanation:**")
    st.write(ai_data["explanation"])


# -------------------------------------------------------------
# Section 4: AI Quiz
# -------------------------------------------------------------
elif nav_choice == "📝 AI Quiz":
    st.title("📝 Python & AI Quiz")
    st.write("Answer the 10 questions below to test your understanding. Click **Submit Quiz** when done.")
    
    questions = get_all_questions()
    
    # Store answers in a dictionary inside a form
    with st.form("quiz_form"):
        user_selections = {}
        
        for q in questions:
            st.markdown(f"**Q{q['id']}. {q['question']}**")
            # Radio button for the 4 options
            choice = st.radio(
                label=f"Options for question {q['id']}:",
                options=q["options"],
                index=None,  # No option pre-selected
                key=f"quiz_q_{q['id']}",
                label_visibility="collapsed"
            )
            user_selections[q["id"]] = choice
            st.write("---")
            
        submitted = st.form_submit_button("Submit Quiz 🚀", use_container_width=True)
        
    if submitted:
        score, total, results = calculate_score(user_selections)
        
        st.subheader(f"📊 Your Score: {score} / {total}")
        percentage = (score / total) * 100
        
        if percentage >= 80:
            st.balloons()
            st.success(f"🎉 Outstanding! You scored {percentage:.0f}%!")
        elif percentage >= 50:
            st.info(f"👍 Good effort! You scored {percentage:.0f}%. Keep practicing!")
        else:
            st.warning(f"📚 You scored {percentage:.0f}%. Review the learning sections and try again!")
            
        st.markdown("### 📋 Detailed Results & Explanations:")
        for r in results:
            if r["is_correct"]:
                st.markdown(f"✅ **Q{r['id']}: Correct!**")
            else:
                st.markdown(f"❌ **Q{r['id']}: Incorrect**")
                
            st.write(f"- **Your Answer:** {r['selected']}")
            st.write(f"- **Correct Answer:** {r['correct_answer']}")
            st.caption(f"💡 *Explanation:* {r['explanation']}")
            st.write("---")


# -------------------------------------------------------------
# Section 5: Rule-Based AI Agent
# -------------------------------------------------------------
elif nav_choice == "🤖 Rule-Based AI Agent":
    st.title("🤖 Rule-Based AI Agent")
    st.caption("A transparent demonstration of an AI Agent decision-making loop.")
    
    st.markdown("""
    > **How this Agent Works:**  
    > `User Input` ➔ `Intent Identification (keyword matching)` ➔ `Tool Selection` ➔ `Tool Execution` ➔ `Response`
    """)
    
    # Showcase the 3 available tools
    with st.expander("🛠️ View Agent Tools Overview", expanded=False):
        st.markdown("""
        1. **Knowledge Tool (`knowledge_tool`)**: Looks up definitions and explanations for AI and Python concepts.
        2. **Quiz Tool (`quiz_tool`)**: Delivers an interactive sample quiz question with spoiler answer.
        3. **Learning Recommendation Tool (`learning_recommendation_tool`)**: Suggests what topic you should study next.
        """)
        
    st.write("Try asking something like:")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.code("What is Machine Learning?")
    with col_b:
        st.code("Give me a quiz question")
    with col_c:
        st.code("What should I learn next?")
        
    user_query = st.text_input("Enter your request for the agent:", placeholder="Type your question or request here...")
    
    if st.button("Ask Agent 🚀"):
        if not user_query.strip():
            st.warning("Please type a message before submitting.")
        else:
            # Run the agent
            trace = run_agent(user_query)
            
            # Show the Agent's internal decision pipeline
            st.markdown("### 🔄 Agent Execution Trace")
            step_col1, step_col2, step_col3 = st.columns(3)
            with step_col1:
                st.metric("1. User Input", f"'{user_query}'")
            with step_col2:
                st.metric("2. Detected Intent", trace["intent"])
            with step_col3:
                st.metric("3. Dispatched Tool", trace["tool_selected"])
                
            st.markdown("### 💬 Agent Response")
            st.markdown(trace["response"])

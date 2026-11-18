# AI Study Buddy – A Simple Learning Assistant 🎓

A beginner-friendly Python learning assistant and rule-based AI agent created to demonstrate foundational concepts in Python, AI, and Agent workflows.

---

## 📖 Project Overview

This project was built to illustrate:
1. **Core Python Concepts**: Variables, condition checks, loops, functions, lists, dictionaries, and classes.
2. **AI Foundations**: Clear explanations of AI, Machine Learning, Deep Learning, Generative AI, Large Language Models, and Neural Networks with real-world examples.
3. **Interactive Quiz**: A 10-question multiple choice quiz with scoring and explanations.
4. **Basic Rule-Based AI Agent**: A transparent, 5-step agent architecture:  
   `User Input ➔ Intent Identification ➔ Tool Selection ➔ Tool Execution ➔ Response`

---

## 📁 Project Structure

```
AI_Study_Buddy/
│
├── learning_content.py   # Dictionaries storing Python & AI concepts and code snippets
├── quiz.py               # 10 quiz questions & scoring evaluation functions
├── agent.py              # Rule-based agent with 3 tools (Knowledge, Quiz, Recommendation)
├── app.py                # Streamlit graphical user interface
├── requirements.txt      # Python dependencies (Streamlit)
└── README.md             # Project documentation and guide
```

---

## 🛠️ Technologies Used

- **Python 3.x**: Pure Python without complex frameworks or external cloud APIs.
- **Streamlit**: For the clean, interactive graphical web interface.
- **Python Dictionaries & Lists**: For in-memory data storage.

---

## 🚀 Installation & Running the Project

### Step 1: Open Terminal / Command Prompt
Navigate to the project directory:
```bash
cd C:\Users\kumar\.gemini\antigravity\scratch\AI_Study_Buddy
```

### Step 2: Install Dependencies
Install Streamlit via pip:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
Launch the Streamlit app:
```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`.

---

## 🤖 How the Rule-Based AI Agent Works

The AI agent in `agent.py` simulates how modern AI agents operate, using clear and explainable logic:

1. **User Input**: Receives text from the user (e.g., *"What is Deep Learning?"*).
2. **Intent Identification**: Checks keywords in the string using simple `if`/`elif` conditions to determine the user's intent:
   - *Quiz Intent*: Keywords like `quiz`, `test`, `question`, `challenge`.
   - *Recommendation Intent*: Keywords like `recommend`, `suggest`, `what next`, `study next`.
   - *Knowledge Intent*: Keywords like `what is`, `explain`, `define`, `ai`, `python`.
3. **Tool Selection**: Directs the query to one of three tool functions:
   - `knowledge_tool(query)`: Looks up definitions and code examples.
   - `quiz_tool(query)`: Selects a challenge question.
   - `learning_recommendation_tool(query)`: Recommends study topics based on interest.
4. **Tool Execution**: The selected Python function executes and generates a formatted response.
5. **Response & Trace**: Returns both the result and an execution trace displayed on the Streamlit interface.

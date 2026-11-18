# quiz.py
# This file contains the 10 quiz questions and helper functions to evaluate answers.

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "Which Python data type is used to store whole numbers without decimals?",
        "options": ["int", "float", "str", "bool"],
        "correct_answer": "int",
        "explanation": "'int' stands for integer, which represents positive or negative whole numbers."
    },
    {
        "id": 2,
        "question": "Which keyword is used in Python to define a function?",
        "options": ["func", "define", "def", "lambda"],
        "correct_answer": "def",
        "explanation": "In Python, the 'def' keyword introduces a function definition."
    },
    {
        "id": 3,
        "question": "How do you access the value associated with key 'age' in a dictionary named `student`?",
        "options": ["student(age)", "student['age']", "student.get_age", "student{age}"],
        "correct_answer": "student['age']",
        "explanation": "Dictionary values are accessed using square brackets with the key name: student['age']."
    },
    {
        "id": 4,
        "question": "What is the primary difference between a list and a dictionary in Python?",
        "options": [
            "Lists store key-value pairs; dictionaries store ordered sequences",
            "Lists store items by index; dictionaries store items by key-value pairs",
            "Lists cannot be changed; dictionaries can be changed",
            "There is no difference between them"
        ],
        "correct_answer": "Lists store items by index; dictionaries store items by key-value pairs",
        "explanation": "Lists are indexed collections starting at index 0, whereas dictionaries look up values using keys."
    },
    {
        "id": 5,
        "question": "What is Artificial Intelligence (AI)?",
        "options": [
            "A specific programming language for web design",
            "Computer systems that mimic human intelligence and problem-solving",
            "A hardware component inside graphics cards",
            "Only robots made of metal and wires"
        ],
        "correct_answer": "Computer systems that mimic human intelligence and problem-solving",
        "explanation": "AI refers to software and systems capable of performing cognitive tasks typically requiring human intelligence."
    },
    {
        "id": 6,
        "question": "How does Machine Learning differ from traditional programming?",
        "options": [
            "Machine Learning requires writing every rule by hand",
            "Machine Learning learns patterns directly from data rather than following hardcoded rules",
            "Traditional programming cannot use mathematical calculations",
            "Machine Learning does not run on computers"
        ],
        "correct_answer": "Machine Learning learns patterns directly from data rather than following hardcoded rules",
        "explanation": "Traditional programming executes programmer-coded rules; ML algorithms infer patterns directly from data."
    },
    {
        "id": 7,
        "question": "What inspired the architecture of Artificial Neural Networks?",
        "options": [
            "Biological networks of neurons in the human brain",
            "The physical wiring of the Internet",
            "The structure of plant roots",
            "Quantum physics equations"
        ],
        "correct_answer": "Biological networks of neurons in the human brain",
        "explanation": "Neural networks are computational models loosely inspired by biological neurons in animal brains."
    },
    {
        "id": 8,
        "question": "What makes Generative AI unique compared to traditional AI?",
        "options": [
            "It can only run offline on calculators",
            "It creates new original content such as text, code, or images from prompts",
            "It never requires any training data",
            "It can only classify numbers into categories"
        ],
        "correct_answer": "It creates new original content such as text, code, or images from prompts",
        "explanation": "Generative AI produces novel artifacts (text, images, code) instead of solely analyzing or categorizing existing data."
    },
    {
        "id": 9,
        "question": "What does LLM stand for in modern AI?",
        "options": [
            "Low Level Machine",
            "Large Language Model",
            "Logical Learning Method",
            "Linear Logic Module"
        ],
        "correct_answer": "Large Language Model",
        "explanation": "LLM stands for Large Language Model, representing deep learning models trained on vast text corpora."
    },
    {
        "id": 10,
        "question": "In a basic AI Agent workflow, what step typically follows 'Intent Identification'?",
        "options": [
            "Shutting down the server",
            "Formatting the hard drive",
            "Tool Selection and Execution",
            "Writing random Python files"
        ],
        "correct_answer": "Tool Selection and Execution",
        "explanation": "In an agent pipeline, after identifying what the user wants (intent), the agent selects and executes the appropriate tool to fulfill the request."
    }
]

def get_all_questions():
    """Returns the list of all quiz questions."""
    return QUIZ_QUESTIONS

def calculate_score(user_answers):
    """
    Calculates the final score based on a dictionary of user answers.
    user_answers format: {question_id: selected_option}
    Returns: (score, total_questions, detailed_results)
    """
    score = 0
    detailed_results = []
    
    for q in QUIZ_QUESTIONS:
        q_id = q["id"]
        selected = user_answers.get(q_id, None)
        is_correct = (selected == q["correct_answer"])
        
        if is_correct:
            score += 1
            
        detailed_results.append({
            "id": q_id,
            "question": q["question"],
            "selected": selected if selected else "Not Answered",
            "correct_answer": q["correct_answer"],
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })
        
    return score, len(QUIZ_QUESTIONS), detailed_results

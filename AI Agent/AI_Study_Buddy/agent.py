# agent.py
# This file implements a simple rule-based AI Agent.
# Workflow: User Input -> Intent Identification -> Tool Selection -> Tool Execution -> Response.

import random
from learning_content import AI_TOPICS, PYTHON_TOPICS
from quiz import QUIZ_QUESTIONS

# -------------------------------------------------------------
# Agent Tools (Simple Python Functions)
# -------------------------------------------------------------

def knowledge_tool(query):
    """
    Tool 1: Knowledge Tool
    Provides information about basic AI or Python concepts from our stored dictionaries.
    """
    query_lower = query.lower()
    
    # 1. Search in AI Topics
    for topic_name, details in AI_TOPICS.items():
        if topic_name.lower() in query_lower:
            return (
                f"🧠 **Knowledge Tool Result for '{topic_name}'**:\n\n"
                f"• **Definition:** {details['definition']}\n\n"
                f"• **Real-Life Example:** {details['real_life_example']}\n\n"
                f"• **Explanation:** {details['explanation']}"
            )
            
    # Check for general keywords like "machine learning" or "deep learning"
    if "machine learning" in query_lower or "ml" in query_lower.split():
        details = AI_TOPICS["Machine Learning"]
        return f"🧠 **Knowledge Tool Result for 'Machine Learning'**:\n\n• **Definition:** {details['definition']}\n\n• **Real-Life Example:** {details['real_life_example']}\n\n• **Explanation:** {details['explanation']}"
        
    if "deep learning" in query_lower or "dl" in query_lower.split():
        details = AI_TOPICS["Deep Learning"]
        return f"🧠 **Knowledge Tool Result for 'Deep Learning'**:\n\n• **Definition:** {details['definition']}\n\n• **Real-Life Example:** {details['real_life_example']}\n\n• **Explanation:** {details['explanation']}"

    if "generative" in query_lower or "genai" in query_lower or "chatgpt" in query_lower:
        details = AI_TOPICS["Generative AI"]
        return f"🧠 **Knowledge Tool Result for 'Generative AI'**:\n\n• **Definition:** {details['definition']}\n\n• **Real-Life Example:** {details['real_life_example']}\n\n• **Explanation:** {details['explanation']}"

    if "llm" in query_lower or "language model" in query_lower:
        details = AI_TOPICS["Large Language Models"]
        return f"🧠 **Knowledge Tool Result for 'Large Language Models'**:\n\n• **Definition:** {details['definition']}\n\n• **Real-Life Example:** {details['real_life_example']}\n\n• **Explanation:** {details['explanation']}"

    if "neural" in query_lower:
        details = AI_TOPICS["Neural Networks"]
        return f"🧠 **Knowledge Tool Result for 'Neural Networks'**:\n\n• **Definition:** {details['definition']}\n\n• **Real-Life Example:** {details['real_life_example']}\n\n• **Explanation:** {details['explanation']}"

    # 2. Search in Python Topics
    for topic_name, details in PYTHON_TOPICS.items():
        if topic_name.lower() in query_lower:
            return (
                f"🐍 **Knowledge Tool Result for '{topic_name}'**:\n\n"
                f"• **Explanation:** {details['explanation']}\n\n"
                f"• **Code Snippet:**\n```python\n{details['code_example']}\n```"
            )

    # General AI summary if general word "ai" is used
    if "ai" in query_lower.split() or "artificial intelligence" in query_lower:
        details = AI_TOPICS["Artificial Intelligence"]
        return f"🧠 **Knowledge Tool Result for 'Artificial Intelligence'**:\n\n• **Definition:** {details['definition']}\n\n• **Real-Life Example:** {details['real_life_example']}\n\n• **Explanation:** {details['explanation']}"

    # Default fallback message if concept is not recognized
    available_concepts = ", ".join(list(AI_TOPICS.keys()))
    return (
        f"I couldn't pinpoint that exact topic in my local knowledge base.\n\n"
        f"💡 **Try asking about one of these concepts:**\n{available_concepts}."
    )


def quiz_tool(query):
    """
    Tool 2: Quiz Tool
    Displays a quick challenge question related to Python or AI.
    """
    sample_question = random.choice(QUIZ_QUESTIONS)
    options_text = "\n".join([f"  - {opt}" for opt in sample_question["options"]])
    
    return (
        f"🎯 **Quiz Tool Sample Question:**\n\n"
        f"**Question:** {sample_question['question']}\n\n"
        f"**Options:**\n{options_text}\n\n"
        f"👉 *Answer Spoiler:* ||{sample_question['correct_answer']}|| ({sample_question['explanation']})\n\n"
        f"*(You can also take the full 10-question quiz in the Quiz section from the sidebar!)*"
    )


def learning_recommendation_tool(query):
    """
    Tool 3: Learning Recommendation Tool
    Suggests what topic the student should study next based on their preference or random rotation.
    """
    query_lower = query.lower()
    
    if "python" in query_lower or "code" in query_lower or "program" in query_lower:
        suggested_topic = random.choice(list(PYTHON_TOPICS.keys()))
        reason = "Building strong Python programming fundamentals makes understanding AI algorithms much easier."
        return (
            f"📚 **Recommended Python Topic to Study Next:**\n\n"
            f"👉 **{suggested_topic}**\n\n"
            f"• **Why study this:** {reason}\n"
            f"• **Action:** Head to the 'Python Learning' tab in the sidebar and check out the code example!"
        )
    elif "ai" in query_lower or "ml" in query_lower or "deep" in query_lower:
        suggested_topic = random.choice(list(AI_TOPICS.keys()))
        reason = "Mastering foundational AI concepts helps you understand modern intelligent systems."
        return (
            f"📚 **Recommended AI Topic to Study Next:**\n\n"
            f"👉 **{suggested_topic}**\n\n"
            f"• **Why study this:** {reason}\n"
            f"• **Action:** Head over to the 'AI Foundations' tab in the sidebar to review the real-life examples!"
        )
    else:
        # Balanced suggestion
        all_topics = list(PYTHON_TOPICS.keys()) + list(AI_TOPICS.keys())
        suggested_topic = random.choice(all_topics)
        return (
            f"📚 **Recommended Topic to Study Next:**\n\n"
            f"👉 **{suggested_topic}**\n\n"
            f"• **Tip:** Steady daily practice with one topic and code snippet will build confidence quickly!"
        )


# -------------------------------------------------------------
# Agent Core: Intent Identification and Tool Dispatcher
# -------------------------------------------------------------

def run_agent(user_input):
    """
    Main rule-based AI Agent runner.
    Workflow:
      1. Accept user input
      2. Identify intent using simple string/condition checks
      3. Select appropriate tool
      4. Execute tool function
      5. Return structured trace showing each step
    """
    # Basic input handling
    if not user_input or user_input.strip() == "":
        return {
            "intent": "Unknown",
            "tool_selected": "None",
            "response": "Please enter a question or command (e.g., 'What is Machine Learning?', 'Give me a quiz question', or 'What should I learn next?')."
        }
        
    cleaned_input = user_input.lower().strip()
    
    # Intent 1: Quiz Intent
    # Keywords indicating the user wants a test or quiz
    quiz_keywords = ["quiz", "test", "question", "challenge", "exam", "practice"]
    if any(keyword in cleaned_input for keyword in quiz_keywords):
        intent = "Quiz Request"
        tool_name = "quiz_tool"
        result = quiz_tool(cleaned_input)
        
    # Intent 2: Recommendation Intent
    # Keywords indicating advice on what to study next
    elif any(keyword in cleaned_input for keyword in ["recommend", "suggest", "what next", "roadmap", "study next", "plan"]):
        intent = "Recommendation Request"
        tool_name = "learning_recommendation_tool"
        result = learning_recommendation_tool(cleaned_input)
        
    # Intent 3: Knowledge / Informational Intent
    # Keywords indicating a search for concepts, explanations, definitions
    elif any(keyword in cleaned_input for keyword in ["what is", "explain", "tell me", "define", "how does", "meaning", "learn", "ai", "python", "neural", "learning"]):
        intent = "Knowledge Lookup"
        tool_name = "knowledge_tool"
        result = knowledge_tool(cleaned_input)
        
    # Fallback / Default Intent: Check Knowledge Tool anyway
    else:
        intent = "General Inquiry (Default Knowledge Search)"
        tool_name = "knowledge_tool"
        result = knowledge_tool(cleaned_input)
        
    return {
        "user_input": user_input,
        "intent": intent,
        "tool_selected": tool_name,
        "response": result
    }

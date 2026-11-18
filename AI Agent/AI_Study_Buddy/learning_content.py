# learning_content.py
# This file stores the educational content for Python and AI Foundations using simple Python dictionaries.

# --- Feature 1: Python Learning Content ---
PYTHON_TOPICS = {
    "Variables and Data Types": {
        "explanation": "Variables are containers used to store data values. Python automatically detects the type of data, such as integers (numbers), floats (decimals), strings (text), and booleans (True/False).",
        "code_example": """# Creating variables of different types
student_name = "Alex"      # String (text)
age = 20                  # Integer (whole number)
gpa = 3.85                # Float (decimal)
is_enrolled = True        # Boolean (True or False)

print("Name:", student_name)
print("Age:", age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)"""
    },
    "Conditional Statements": {
        "explanation": "Conditional statements (if, elif, else) allow your program to make decisions and execute different blocks of code based on whether a condition is True or False.",
        "code_example": """# Checking test score
score = 85

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 75:
    print("Grade: B - Good job!")
elif score >= 50:
    print("Grade: C - Passed.")
else:
    print("Grade: F - Try again.")"""
    },
    "Loops": {
        "explanation": "Loops are used to repeat a block of code multiple times. A 'for' loop iterates over a sequence (like a list or range), while a 'while' loop runs as long as a condition remains True.",
        "code_example": """# 1. For loop over a range of numbers
print("Counting with for loop:")
for i in range(1, 4):
    print("Step", i)

# 2. While loop
print("\\nCounting down with while loop:")
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")"""
    },
    "Functions": {
        "explanation": "A function is a reusable block of code that performs a specific action. You define a function using the 'def' keyword, give it parameters (inputs), and optionally return an output.",
        "code_example": """# Function to greet and calculate study hours per day
def weekly_study_plan(name, total_hours):
    hours_per_day = total_hours / 7
    message = f"Hello {name}, you need to study {hours_per_day:.1f} hours per day."
    return message

# Calling the function
plan = weekly_study_plan("Alex", 14)
print(plan)"""
    },
    "Lists and Dictionaries": {
        "explanation": "Lists are ordered collections of items that can be changed (mutable). Dictionaries store data in key-value pairs, making it easy to look up values using unique keys.",
        "code_example": """# List of study topics
topics = ["Variables", "Loops", "Functions"]
topics.append("Classes")  # Adding an item
print("Study Topics List:", topics)
print("First topic:", topics[0])

# Dictionary representing a student profile
student = {
    "name": "Alex",
    "course": "AI Foundations",
    "progress_percent": 80
}
print("\\nStudent Dictionary:", student)
print("Enrolled Course:", student["course"])"""
    },
    "Classes and Objects": {
        "explanation": "Object-Oriented Programming (OOP) models real-world things. A 'class' is a blueprint or template, and an 'object' is a specific instance created from that class.",
        "code_example": """# Defining a simple Student class
class Student:
    def __init__(self, name, topic):
        self.name = name          # Attribute
        self.topic = topic        # Attribute

    def introduce(self):          # Method (behavior)
        return f"Hi, I am {self.name} and I am currently studying {self.topic}."

# Creating an object (instance) of Student
student1 = Student("Alex", "Python Basics")
print(student1.introduce())"""
    }
}


# --- Feature 2: AI Foundations Content ---
AI_TOPICS = {
    "Artificial Intelligence": {
        "definition": "Artificial Intelligence (AI) refers to computer systems designed to perform tasks that typically require human intelligence.",
        "real_life_example": "Virtual assistants like Siri and Google Assistant that understand spoken questions and set alarms or answer queries.",
        "explanation": "AI is the broad umbrella term for machines mimicking human cognitive abilities such as problem solving, pattern recognition, and learning from experience."
    },
    "Machine Learning": {
        "definition": "Machine Learning (ML) is a subset of AI where systems learn patterns directly from data instead of being explicitly programmed with rules.",
        "real_life_example": "Netflix or Spotify recommending movies and songs based on your past viewing and listening history.",
        "explanation": "Instead of a programmer writing every single 'if-else' rule, an ML algorithm analyzes historical data to find trends and make predictions on new data."
    },
    "Deep Learning": {
        "definition": "Deep Learning is a specialized branch of Machine Learning based on Artificial Neural Networks with many stacked layers (hence 'deep').",
        "real_life_example": "Facial recognition systems that unlock your smartphone by identifying your facial features.",
        "explanation": "Deep Learning algorithms excel at processing complex, unstructured data like images, audio, and raw video by learning intricate features at each layer."
    },
    "Generative AI": {
        "definition": "Generative AI (GenAI) is a category of AI models that can generate new, original content—such as text, code, images, and audio—based on prompts.",
        "real_life_example": "Tools like ChatGPT or Gemini generating an essay, or Midjourney creating digital artwork from a text description.",
        "explanation": "Unlike traditional AI that classifies or predicts existing data, Generative AI models learn data distributions and generate plausible new creations."
    },
    "Large Language Models": {
        "definition": "Large Language Models (LLMs) are massive deep learning models trained on vast amounts of text data to understand and generate human language.",
        "real_life_example": "AI chatbots that can converse naturally, translate foreign languages, summarize lengthy articles, and write code.",
        "explanation": "LLMs use transformer architecture with billions of parameters to predict the most likely next words in a sequence given the context provided."
    },
    "Neural Networks": {
        "definition": "Neural Networks are computational models inspired by the biological structure and communication of neurons in the human brain.",
        "real_life_example": "Handwriting recognition software used by post offices to automatically read zip codes on envelopes.",
        "explanation": "They consist of an input layer, one or more hidden processing layers, and an output layer. Each node (neuron) applies mathematical weights to inputs to produce a prediction."
    }
}

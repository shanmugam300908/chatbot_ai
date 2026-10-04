import tkinter as tk
from tkinter import scrolledtext
internships = [
    {
        "company": "TCS",
        "role": "Python Developer Intern",
        "domain": "Python",
        "location": "Chennai",
        "stipend": 10000,
        "skills": ["python", "sql", "git"]
    },

    {
        "company": "Zoho",
        "role": "AI Intern",
        "domain": "Artificial Intelligence",
        "location": "Chennai",
        "stipend": 15000,
        "skills": ["python", "ai", "machine learning"]
    },

    {
        "company": "Infosys",
        "role": "Data Science Intern",
        "domain": "Data Science",
        "location": "Bangalore",
        "stipend": 12000,
        "skills": ["python", "pandas", "machine learning"]
    },

    {
        "company": "Wipro",
        "role": "Web Development Intern",
        "domain": "Web Development",
        "location": "Coimbatore",
        "stipend": 8000,
        "skills": ["html", "css", "javascript"]
    },

    {
        "company": "Accenture",
        "role": "Machine Learning Intern",
        "domain": "Machine Learning",
        "location": "Bangalore",
        "stipend": 18000,
        "skills": ["python", "machine learning", "tensorflow"]
    },

    {
        "company": "IBM",
        "role": "AI and Data Intern",
        "domain": "Artificial Intelligence",
        "location": "Bangalore",
        "stipend": 20000,
        "skills": ["python", "ai", "data science"]
    },

    {
        "company": "Freshworks",
        "role": "Software Developer Intern",
        "domain": "Software Development",
        "location": "Chennai",
        "stipend": 14000,
        "skills": ["python", "java", "sql"]
    },

    {
        "company": "Cognizant",
        "role": "Data Analyst Intern",
        "domain": "Data Science",
        "location": "Coimbatore",
        "stipend": 9000,
        "skills": ["python", "sql", "excel"]
    }
]
def find_internships(query):

    query = query.lower()

    results = []

    for internship in internships:

        score = 0
        if internship["company"].lower() in query:
            score += 3
        if any(word in query for word in
               internship["role"].lower().split()):
            score += 2
        if internship["domain"].lower() in query:
            score += 3
        if internship["location"].lower() in query:
            score += 3
        for skill in internship["skills"]:
            if skill.lower() in query:
                score += 2

        if score > 0:
            results.append((score, internship))
    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return results
def chatbot_response(query):

    query_lower = query.lower()
    if query_lower in ["hi", "hello", "hey"]:

        return (
            "🤖 Hello! Welcome to Internship Finder AI.\n\n"
            "I can help you find internships based on:\n"
            "• Skills\n"
            "• Location\n"
            "• Domain\n"
            "• Company\n\n"
            "Example:\n"
            "Find Python internships in Chennai"
        )
    if "help" in query_lower:

        return (
            "🤖 You can ask me things like:\n\n"
            "• Find Python internships\n"
            "• Find internships in Chennai\n"
            "• Find AI internships\n"
            "• Find Machine Learning internships in Bangalore\n"
            "• Find internships for Python and SQL"
        )

    results = find_internships(query)

    if not results:

        return (
            "❌ Sorry, I couldn't find a matching internship.\n\n"
            "Try:\n"
            "👉 Find Python internships in Chennai\n"
            "👉 Find AI internships\n"
            "👉 Find Data Science internships"
        )

    response = "🤖 I found these internships for you:\n\n"

    for score, internship in results[:5]:

        response += (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🏢 Company: {internship['company']}\n"
            f"💼 Role: {internship['role']}\n"
            f"🧠 Domain: {internship['domain']}\n"
            f"📍 Location: {internship['location']}\n"
            f"💰 Stipend: ₹{internship['stipend']}\n"
            f"🛠 Skills: {', '.join(internship['skills'])}\n"
            f"⭐ Match Score: {score}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

    return response
def send_message(event=None):

    message = entry.get().strip()

    if message == "":
        return
    chat.insert(
        tk.END,
        "👤 You: " + message + "\n\n"
    )
    response = chatbot_response(message)

    chat.insert(
        tk.END,
        response + "\n\n"
    )
    entry.delete(0, tk.END)

    chat.see(tk.END)

root = tk.Tk()

root.title("AI Internship Finder Chatbot")

root.geometry("750x650")

root.resizable(True, True)

title = tk.Label(
    root,
    text="🤖 AI Internship Finder",
    font=("Arial", 24, "bold")
)

title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Find internships based on your skills and interests",
    font=("Arial", 12)
)

subtitle.pack()

chat = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12)
)

chat.pack(
    padx=20,
    pady=15,
    fill=tk.BOTH,
    expand=True
)
chat.insert(
    tk.END,
    "🤖 Internship Finder AI\n\n"
    "Hello! I can help you find internships.\n\n"
    "Try typing:\n"
    "• Find Python internships in Chennai\n"
    "• Find AI internships\n"
    "• Find internships in Coimbatore\n"
    "• Find Machine Learning internships\n\n"
)
input_frame = tk.Frame(root)

input_frame.pack(
    padx=20,
    pady=10,
    fill=tk.X
)

entry = tk.Entry(
    input_frame,
    font=("Arial", 14)
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    padx=(0, 10)
)
send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 12, "bold"),
    command=send_message
)

send_button.pack(
    side=tk.RIGHT
)

entry.bind(
    "<Return>",
    send_message
)
root.mainloop()

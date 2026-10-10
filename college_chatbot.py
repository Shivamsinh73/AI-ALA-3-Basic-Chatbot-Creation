"""
College Helpdesk Chatbot
------------------------
A simple rule-based chatbot built with Python using if-elif-else conditions.
Topic: College (admissions, courses, fees, library, hostel, exams, contact)

Run:  python college_chatbot.py
Type 'bye' or 'quit' to exit.
"""

import random
import re


def normalize(text: str) -> str:
    """Lowercase and strip punctuation so matching is easier."""
    text = text.lower().strip()
    return re.sub(r"[^\w\s]", "", text)


def get_response(user_input: str) -> str:
    """Rule-based response engine using if-elif-else conditions."""
    msg = normalize(user_input)

    # --- Greetings ---
    if re.search(r"\b(hello|hi|hey|namaste)\b", msg):
        return random.choice([
            "Hello! Welcome to GMIU College Helpdesk. How can I help you today?",
            "Hi there! Ask me about admissions, courses, fees, hostel, library or exams.",
        ])

    # --- Admissions ---
    elif "admission" in msg or "apply" in msg or "enroll" in msg:
        return ("Admissions open in June every year. You can apply online through the "
                "college website or visit the admission cell (Room 101, Admin Block). "
                "Required documents: 10th & 12th marksheets, ID proof, and 4 photos.")

    # --- Courses ---
    elif "course" in msg or "branch" in msg or "program" in msg or "degree" in msg:
        return ("We offer B.Tech (CSE, IT, ECE, ME, CE), BBA, BCA, MBA and MCA. "
                "Which course would you like to know more about?")

    # --- Fees ---
    elif "fee" in msg or "fees" in msg or "cost" in msg or "payment" in msg:
        return ("The annual tuition fee is approximately Rs. 75,000 for B.Tech and "
                "Rs. 45,000 for BBA/BCA. Fees can be paid semester-wise online or at "
                "the accounts office. Scholarships are available for meritorious students.")

    # --- Library ---
    elif "library" in msg or "book" in msg:
        return ("The central library is open Monday–Saturday, 8 AM to 8 PM. "
                "Students can borrow up to 4 books for 15 days using their ID card. "
                "A digital library with e-journals is also available 24x7.")

    # --- Hostel ---
    elif "hostel" in msg or "accommodation" in msg or "room" in msg:
        return ("Separate hostels for boys and girls are available on campus. "
                "Hostel fee is Rs. 60,000 per year including mess. Rooms are allotted "
                "on a first-come, first-served basis. Contact the hostel warden office.")

    # --- Exams ---
    elif "exam" in msg or "result" in msg or "marks" in msg or "grade" in msg:
        return ("Semester exams are held in December and May. Results are published "
                "on the student portal within 30 days. Revaluation forms must be "
                "submitted within 7 days of result declaration.")

    # --- Timings ---
    elif "timing" in msg or "time" in msg or "open" in msg or "hour" in msg:
        return "College timings are 9:00 AM to 4:30 PM, Monday to Friday. The campus is closed on Sundays and public holidays."

    # --- Location / Contact ---
    elif "where" in msg or "location" in msg or "address" in msg or "contact" in msg or "phone" in msg:
        return ("We are located at GMIU Campus, Sector 12, Gandhinagar, Gujarat. "
                "Phone: 079-1234-5678 | Email: info@gmiu.edu.in")

    # --- Faculty ---
    elif "faculty" in msg or "teacher" in msg or "professor" in msg:
        return ("We have 120+ experienced faculty members, most holding PhDs. "
                "You can view department-wise faculty profiles on the college website.")

    # --- Placements ---
    elif "placement" in msg or "job" in msg or "package" in msg or "company" in msg:
        return ("Our placement cell records 85%+ placements. Top recruiters include "
                "TCS, Infosys, Wipro and Reliance. Highest package last year: 12 LPA, "
                "average package: 4.5 LPA.")

    # --- Thanks ---
    elif "thank" in msg:
        return "You're welcome! Feel free to ask anything else about the college."

    # --- Goodbye ---
    elif "bye" in msg or "quit" in msg or "exit" in msg:
        return "Goodbye! Best of luck with your studies. Visit us again!"

    # --- Fallback ---
    else:
        return ("Sorry, I didn't understand that. You can ask me about admissions, "
                "courses, fees, library, hostel, exams, placements, timings or contact details.")


def main():
    print("=" * 55)
    print("       GMIU COLLEGE HELPDESK CHATBOT")
    print("=" * 55)
    print("Bot: Hello! I'm the College Helpdesk Bot.")
    print("Bot: Ask me about admissions, courses, fees, library,")
    print("     hostel, exams, placements, timings or contact.")
    print("Bot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue
        response = get_response(user_input)
        print("Bot:", response)
        if normalize(user_input) in ("bye", "quit", "exit", "goodbye"):
            break


if __name__ == "__main__":
    main()

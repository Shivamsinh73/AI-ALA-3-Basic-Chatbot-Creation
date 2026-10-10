# College Helpdesk Chatbot
# Rule based chatbot using if-elif-else
# Type bye to exit
 
def get_reply(text):
    # make everything lowercase so matching is easy
    msg = text.lower()
 
    # remove some common symbols
    for ch in "?!.,":
        msg = msg.replace(ch, "")
 
    words = msg.split()
 
    if "hello" in words or "hi" in words or "hey" in words:
        return "Hello! Welcome to GMIU College Helpdesk. How can I help you?"
 
    elif "admission" in msg or "apply" in msg:
        return "Admissions start in June. You can apply online on the college website or visit the admission office in the Admin Block. Documents needed: 10th and 12th marksheet, ID proof and photos."
 
    elif "course" in msg or "branch" in msg or "degree" in msg:
        return "We have B.Tech (CSE, IT, ECE, ME, CE), BBA, BCA, MBA and MCA."
 
    elif "fee" in msg or "fees" in msg or "payment" in msg:
        return "B.Tech fee is around Rs. 75,000 per year and BBA/BCA is around Rs. 45,000 per year. You can pay online or at the accounts office."
 
    elif "library" in msg or "book" in msg:
        return "Library is open Monday to Saturday, 8 AM to 8 PM. You can take 4 books for 15 days with your ID card."
 
    elif "hostel" in msg or "accommodation" in msg:
        return "Hostel is available for both boys and girls. Fee is Rs. 60,000 per year with mess."
 
    elif "exam" in msg or "result" in msg or "marks" in msg:
        return "Exams are held in December and May. Results come on the student portal within 30 days."
 
    elif "timing" in msg or "time" in msg or "open" in msg:
        return "College timing is 9:00 AM to 4:30 PM, Monday to Friday."
 
    elif "contact" in msg or "phone" in msg or "address" in msg or "location" in msg:
        return "GMIU Campus, Gandhinagar, Gujarat. Phone: 079-1234-5678, Email: info@gmiu.edu.in"
 
    elif "placement" in msg or "job" in msg or "package" in msg:
        return "Placement is around 85%. Companies like TCS, Infosys and Wipro visit our college. Highest package is 12 LPA."
 
    elif "thanks" in msg or "thank" in msg:
        return "You're welcome! Ask me anything else."
 
    elif "bye" in words or "exit" in words or "quit" in words:
        return "Goodbye! All the best for your studies."
 
    else:
        return "Sorry, I did not understand. You can ask about admission, courses, fees, library, hostel, exams, placement, timing or contact."
 
 
# main program
print("---- GMIU College Helpdesk Chatbot ----")
print("Ask me about admission, courses, fees, library, hostel, exams, placement etc.")
print("Type bye to exit\n")
 
while True:
    user = input("You: ")
 
    if user.strip() == "":
        continue
 
    reply = get_reply(user)
    print("Bot:", reply)
 
    if reply.startswith("Goodbye"):
        break

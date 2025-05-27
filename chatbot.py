import re

faq_dict = {
    r"(hi|hello|hey|hiya|howdy|good (morning|afternoon|evening))": 
        "Hello! How can I help you today?",
    r"(what('s| is) your name\??|who (are|r) you\??|tell me your name)": 
        "I'm FAQBot, here to answer your questions.",
    r"(what services (do you offer|are available)\??|what can you do\??|tell me about your services|your services please)": 
        "We offer web development, app development, and AI solutions.",
    r"(how (do|can) i contact (support|help)\??|i need (support|help)|help me|customer support|reach support team)": 
        "You can contact support via email at support@example.com.",
    r"(what are your working hours\??|when are you open\??|business hours\??|office timings\??)": 
        "Our support team is available from 9 AM to 6 PM, Monday to Friday.",
    r"(where are you located\??|company location\??|your address\??)": 
        "We're based online but our headquarters are in San Francisco, CA.",
    r"(how much does it cost\??|pricing info\??|tell me about pricing|what are your rates\??)": 
        "Pricing varies by service. Please visit example.com/pricing for full details.",
    r"(quit|exit|bye|goodbye|see you|close the chat)": 
        "Goodbye! Have a great day.",
}

def Faq(user_input):
    for pattern, response in faq_dict.items():
        if re.fullmatch(pattern, user_input, re.IGNORECASE):
            return response
    return "INVALID"


while True:
    user_input = input("You: ")
    chat_bot = Faq(user_input)
    print("FAQBot:", chat_bot)


    if any(kw in chat_bot.lower() for kw in ["goodbye", "exit", "quit", "see you", "close the chat"]):
        break
        
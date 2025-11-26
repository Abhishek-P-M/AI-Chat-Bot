import os
import sqlite3
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import List, Tuple

# Load the openAI key from the .env(the api key will be deleted upon upload of the directory to github)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

DB_FILE = os.path.join(os.path.dirname(__file__), "food_delivery.sqlite")

def get_order_status(user_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM Orders WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No order found for this user."

def get_delivery_time(user_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT delivery_time FROM Orders WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No order found for this user."

def get_cancellation_policy(user_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT cancellation_policy FROM Orders WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "No order found for this user."

def get_delivery_partner_info(user_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT dp.name, dp.phone 
        FROM DeliveryPartners dp
        JOIN Orders o ON dp.partner_id = o.partner_id
        WHERE o.user_id = ?""", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return f"{result[0]} ({result[1]})" if result else "No delivery partner found."

def get_restaurant_info(order_id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.name, r.cuisine, r.phone
        FROM Restaurants r
        JOIN Orders o ON r.restaurant_id = o.restaurant_id
        WHERE o.order_id = ?""", (order_id,))
    result = cursor.fetchone()
    conn.close()
    return f"{result[0]} ({result[1]}, {result[2]})" if result else "No restaurant found."

llm = ChatOpenAI(
    model="gpt-5-nano",
    openai_api_key=OPENAI_API_KEY,
    temperature=0
)


def get_response(user_input: str, user_id: int) -> str:
    
    """Invokes the LLM with the user's input and required system instructions.
    The user_id is passed for the LLM to use the database tools effectively."""
    system_message = f"""You are a helpful assistant for a food delivery service. The current user's ID is {user_id}.

You have access to the following tools (functions):
- get_order_status(user_id)
- get_delivery_time(user_id)
- get_cancellation_policy(user_id)
- get_delivery_partner_info(user_id)
- get_restaurant_info(order_id)

Call the appropriate function if needed to answer the user's question.
If the user asks about their order, use the current user ID ({user_id}) for the database functions (except get_restaurant_info)."""

    messages: List[Tuple[str, str]] = [
        ("system", system_message),
        ("human", user_input)
    ]

    try:
        ai_msg = llm.invoke(messages)
        
        
        print(f"LLM Output (user_id {user_id}): {ai_msg.content}") 
        
        return ai_msg.content
    except Exception as e:
        print(f"LLM Invocation Error: {e}")
        return "I encountered an internal processing error."

def main():
    print("Welcome to Food Delivery Chatbot! Type 'exit' to quit.")
    cli_user_id = 1 
    print(f"Note: CLI is using hardcoded User ID: {cli_user_id}")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            break
            
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = get_response(user_input, cli_user_id) 
        print("Bot:", response)

if __name__ == "__main__":
    main()
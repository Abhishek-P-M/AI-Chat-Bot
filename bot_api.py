from fastapi import FastAPI
from pydantic import BaseModel
from chatbot_langchain import get_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    user_id: int = 1 

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    """Receives a message and user ID, calls the GPT-5 chatbot function with both arguments, and returns the response."""
    user_message = request.message
    user_id_from_request = request.user_id
    
    try:
        response = get_response(user_message, user_id_from_request)
        
        return {"response": response}
    
    except Exception as e:
        print(f"Error processing chat request: {e}")
        return {"response": "Sorry, the chatbot service is currently unavailable."}, 500

@app.get("/")
def read_root():
    return {"status": "Chatbot API is running on port 8000"}